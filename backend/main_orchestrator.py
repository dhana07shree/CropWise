# backend/main_orchestrator.py
import os
import json
from dotenv import load_dotenv
from utils.predictor import predict_disease
from utils.weather_tool import fetch_live_weather
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def generate_llm_advisory_report(plant: str, condition: str, weather_data: dict):
    """
    Constructs a modern LangChain LCEL Chain utilizing StrOutputParser
    and Groq's native JSON mode for raw, high-speed structured text processing.
    """
    # Initialize Groq with strict JSON-mode response formatting enabled
    llm = ChatGroq(
        temperature=0.2,
        model_name="llama-3.1-8b-instant",
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_kwargs={"response_format": {"type": "json_object"}} 
    )

    # Structural template prompt
    template = """
    You are an elite expert agricultural scientist and plant pathologist specialized in precision crop management.
    Analyze the crop diagnostic metrics and microclimate constraints below to compile an actionable agronomic recovery strategy.

    --- BOTANICAL DIAGNOSTIC CONSTRAINTS ---
    Target Plant Taxonomy Category: {plant}
    Pathological Condition Identified: {condition}

    --- REGIONAL REAL-TIME MICRO-CLIMATE METRICS ---
    Target Geographic Location: {location_city}
    Ambient Temperature Thermal Index: {temp_c}°C
    Relative Air Moisture Volatility Index: {humidity}%
    Prevailing Wind Dynamic Velocity: {wind_speed} km/h
    Visual Macro Atmosphere Sky Conditions: {weather_txt}

    --- MANDATORY CODEC EXCLUSION PRINCIPLES ---
    You must output your analysis EXACTLY inside a structured JSON object framework matching this schema key topology layout. Do not invent key paths:
    {{
      "severity_estimation": {{
        "score_percentage": <int, evaluation mapping from 0-100 indicating crop tissue damage extent. If condition is healthy, set to 0.>,
        "tier": "<string: None, Low, Medium, High, or Critical>",
        "justification": "<string: concise summary linking the condition type to active micro-climate trends>"
      }},
      "disease_information": {{
        "description": "<string: concise profile overview of the pathogen biology or healthy tissue analysis context>",
        "primary_causes": ["<string list: list environmental or treatment factors relative to this plant state>"]
      }},
      "micro_climate_advisory": {{
        "risk_assessment": "<string: analyze how current local temperature/humidity levels might impact this plant state layout>",
        "actionable_warning": "<string: provide a generic seasonal advisory warning note based on local weather conditions>"
      }},
      "cost_estimation": {{
        "organic_treatment": {{
            "price_range_inr": "<string: localized price range estimate in Indian Rupees (₹). Use ₹0 if healthy.>",
            "methods": ["<string list: list organic steps, soil enrichment, or relevant bio-pesticide routines if matching an infection>"]
        }},
        "chemical_treatment": {{
            "price_range_inr": "<string: localized price range estimate in Indian Rupees (₹). Use ₹0 if healthy.>",
            "methods": ["<string list: list targets or write None if healthy>"]
        }}
      }},
      "recovery_timeline": {{
        "expected_recovery_days": "<string: realistic estimate description window or Stable text representation>",
        "interactive_checklist": [
          {{"day": 1, "task": "<string: immediate crop maintenance or therapeutic intervention activity step>"}},
          {{"day": 3, "task": "<string: standard moisture control or field monitoring action step>"}},
          {{"day": 5, "task": "<string: any additional and important step needed"}},
          {{"day": 7, "task": "<string: routine tracking observation step>"}}
        ]
      }},
      "preventive_measures": ["<string list: provide practical agricultural methods to keep your fields thriving and strong>"],
      "recommendation_ranking": [
        {{"rank": 1, "treatment_name": "<string: primary field action plan path>", "effectiveness": "<string>", "cost_tier": "<string: Free, Cheap, or Moderate>"}},
        {{"rank": 2, "treatment_name": "<string: secondary observation plan path>", "effectiveness": "<string>", "cost_tier": "<string>"}}
      ]
    }}
    Ensure output is stringently clean, complete, unescaped, and valid JSON. Keep keys lowercase exactly as defined. Do not append any conversational filler text.
    """

    prompt = PromptTemplate(
        input_variables=["plant", "condition", "location_city", "temp_c", "humidity", "wind_speed", "weather_txt"],
        template=template
    )

    chain = prompt | llm | StrOutputParser()

    response_text = chain.invoke({
        "plant": plant,
        "condition": condition,
        "location_city": weather_data.get("city", " "),
        "temp_c": weather_data.get("temperature_celsius", 27.0),
        "humidity": weather_data.get("humidity_percentage", 65),
        "wind_speed": weather_data.get("wind_speed_kmh", 12.0),
        "weather_txt": weather_data.get("weather_condition", "Clear")
    })

    try:
        return json.loads(response_text)
    except Exception:
        # Fallback processing in case formatting limits are hit
        return {
            "parsing_fallback": True,
            "raw_text": response_text
        }

