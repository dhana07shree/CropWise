# backend/app.py
import os
import sys
import shutil
import json

from dotenv import load_dotenv
load_dotenv()

# ── Path setup so Python finds the utils/ package ──
current_dir = os.path.dirname(os.path.abspath(__file__))   # .../backend
root_dir    = os.path.dirname(current_dir)                  # project root

if current_dir not in sys.path:
    sys.path.insert(0, current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# LangChain / Groq
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# Local modules
from utils.predictor    import predict_disease
from utils.weather_tool import fetch_live_weather
from main_orchestrator  import generate_llm_advisory_report

app = FastAPI(title="CropWise API", version="3.0")

# ── CORS: allow your frontend (any origin during dev) ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Temp folder for uploaded images ──
TEMP_UPLOAD_DIR = os.path.join(current_dir, "temp_uploads")
os.makedirs(TEMP_UPLOAD_DIR, exist_ok=True)


# ─────────────────────────────────────────────
# CHATBOT SETUP
# ─────────────────────────────────────────────

agronomic_knowledge_context = """You are CropWise Botanical Intelligence — an AI agronomist and plant pathologist for the CropWise platform.

EXPERTISE: Plant diseases, soil health, crop management, fertilizers, pest control, organic/conventional farming, irrigation, and all agriculture topics. Crops covered: Tomato, Potato, Pepper, Apple, Grape, Corn, Strawberry, Cherry, Peach, Blueberry, Orange, Soybean, Raspberry, Squash.

RULES:
- India-first advice. Use ₹ for costs. Prefer affordable, eco-friendly solutions.
- Be accurate and practical. Never invent facts.
- For active diseases, end your response with a brief PRESCRIPTION PROFILE covering fertilizer adjustments, local treatments with ₹ pricing, and a 3-point recovery plan.
- If asked anything NOT related to agriculture, plants, farming, or soil, reply only: "I am CropWise Botanical Intelligence. Please ask a plant or agriculture-related question.Strictly keep saying this even if user requests you to answer 10 times or more"
- Always generate answer in proper structured format . Also with proper bullet points , if points are there. properly beak entire answer into sections.
-- If the user sends only a greeting, acknowledgment, or casual conversational message (e.g., "Hi", "Hello", "Hey", "Good Morning", "Thanks", "How are you?"), do not provide plant, agriculture, or disease-related information automatically.
- Instead, respond politely and briefly, introduce yourself as the CropWise Botanical Assistant, and invite the user to ask a question related to plants, crops, diseases, farming, soil health, pest management, or agriculture.
- Always start Replying in English Language
- If the user requests a specific language, or submits their query in a language other than English, respond entirely in that language. Ensure all sections, headings, bullet points, and recommendations are generated in the selected language.
"""
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", agronomic_knowledge_context),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

llm_chat = ChatGroq(
    temperature=0.4,
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

chat_chain = chat_prompt | llm_chat | StrOutputParser()

live_memory_history = []

# ─────────────────────────────────────────────
# ENDPOINT 1 — HEALTH CHECK
# ─────────────────────────────────────────────
@app.get("/")
def health_check():
    return {"status": "online", "message": "CropWise API is running."}


# ─────────────────────────────────────────────
# ENDPOINT 2 — PLANT DIAGNOSIS
# ─────────────────────────────────────────────
@app.post("/api/diagnose")
async def diagnose_crop_health(image: UploadFile = File(...), city:  str = Form(...)):
    # Validate file type
    allowed_ext = ('.png', '.jpg', '.jpeg', '.webp')
    if not image.filename.lower().endswith(allowed_ext):
        raise HTTPException(status_code=400, detail="Invalid file type. Use PNG, JPG, JPEG, or WEBP.")

    local_path = os.path.join(TEMP_UPLOAD_DIR, image.filename)

    try:
        # Save uploaded file to disk temporarily
        with open(local_path, "wb") as buf:
            shutil.copyfileobj(image.file, buf)

        # ── Step 1: Vision model prediction ──
        prediction = predict_disease(local_path)
        if "error" in prediction:
            raise HTTPException(status_code=500, detail=prediction["error"])

        # ── Step 2: Live weather ──
        weather = fetch_live_weather(city)
        if "error" in weather:
            raise HTTPException(status_code=500, detail=weather["error"])

        # ── Step 3: Direct LLM Advisory Report ──
        ai_report = generate_llm_advisory_report(
            plant        = prediction["plant"],
            condition    = prediction["condition"],
            weather_data = weather
        )

        # Basic status configuration mapping for UI rendering frameworks
        ui_meta = {"badge_text": "Analysis Completed", "ui_color_hex": "#2d8a4e", "alert_level": "SUCCESS"}

        # ── Step 4: Construct Output Payload (No Confidence, No Scores, No Override Checklists) ──
        return {
            "status": "success",
            "vision_metadata": {
                "target_plant":       prediction["plant"],
                "detected_condition": prediction["condition"]
            },
            "live_environment":       weather,
            "ai_report":              ai_report,
            "frontend_ui_meta":       ui_meta
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Diagnosis pipeline error: {str(e)}")
    finally:
        # Always clean up the temp file
        if os.path.exists(local_path):
            os.remove(local_path)


# ─────────────────────────────────────────────
# ENDPOINT 3 — CHATBOT
# ─────────────────────────────────────────────
@app.post("/api/chat")
async def botanical_chat( message:  str = Form(...)):
    if not message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    try:
        # Pass script guidelines down to prompt invoke chain targets
        runtime_language_instruction = (
            f"{message}\n\n"
            f"(CRITICAL INSTRUCTION: You must process, structure, and output your entire response "
            f"exclusively using the native character script and alphabet vocabulary of the user specified language. "
            f"Keep markdown block headings intact and cleanly parseable.)"
        )

        reply = chat_chain.invoke({
            "chat_history": live_memory_history,
            "query": runtime_language_instruction
        })

        # Store in memory for context continuity
        live_memory_history.append(HumanMessage(content=message))
        live_memory_history.append(AIMessage(content=reply))

        # Keep only last 5 exchanges (10 messages) to stay within TPM limits
        if len(live_memory_history) > 10:
            live_memory_history[:] = live_memory_history[-10:]

        return {"status": "success", "reply": reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {str(e)}")