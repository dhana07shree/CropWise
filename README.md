🌿 CropWise -- AI-Powered Crop Disease Diagnosis & Advisory Platform



An end-to-end AI platform that combines Computer Vision, DeepLearning, Real-Time Weather Intelligence, and Generative AI todiagnose crop diseases and generate personalized treatmentrecommendations.

🚀 Live Demo

Replace the links below after deployment.

<!-- 🌐 Frontend:https://your-vercel-link.vercel.app

⚙ Backend API:https://your-render-link.onrender.com

📄 Swagger API Docs:https://your-render-link.onrender.com/docs -->
https://crop-wise-fawn.vercel.app/

📸 Project Screenshots

Create a folder named screenshots/ and add the images below.

🏠 Home Page

screenshots/home.png

🔍 Disease Diagnosis

screenshots/diagnosis.png

📊 AI Advisory Report

screenshots/report.png

🤖 AI Chatbot

screenshots/chatbot.png

After adding images, replace the placeholders with:

![Home](screenshots/home.png)
![Diagnosis](screenshots/diagnosis.png)
![Report](screenshots/report.png)
![Chatbot](screenshots/chatbot.png)

📖 Overview

CropWise is an AI-powered agricultural decision-support platform thathelps farmers identify crop diseases from leaf images and providesintelligent treatment recommendations using live weather information andLarge Language Models.

The application integrates:

CNN-based disease detection

Live weather intelligence

AI-generated advisory reports

Agricultural chatbot

Modern responsive web interface

✨ Key Features

✅ CNN-based crop disease detection

✅ Supports 38 disease/healthy classes

✅ Supports 14 crop species

✅ Live weather integration

✅ Disease severity estimation

✅ Organic & chemical treatment suggestions

✅ Cost estimation

✅ Recovery timeline

✅ Preventive measures

✅ AI-powered agricultural chatbot

✅ Multilingual responses

✅ Responsive UI

✅ Production deployment

🌱 Supported Crops

Apple

Blueberry

Cherry

Corn (Maize)

Grape

Orange

Peach

Bell Pepper

Potato

Raspberry

Soybean

Squash

Strawberry

Tomato

🛠 Tech Stack

Category          Technologies

Frontend          HTML5, CSS3, JavaScriptBackend           Python, FastAPIDeep Learning     TensorFlow, Keras, MobileNetV2AI                LangChain, Groq LlamaWeather           WeatherAPIDeployment        Vercel, RenderVersion Control   Git, GitHub

🧠 AI Model Information

Property     Value

Model        MobileNetV2-based CNNFramework    TensorFlow / KerasDataset      PlantVillageInput Size   224 × 224 × 3Classes      38Crops        14Output       Disease + Confidence

🏗 Detailed System Architecture

                    USER
                      │
      Upload Leaf Image + Enter City
                      │
                      ▼
       HTML/CSS/JavaScript Frontend (Vercel)
                      │
             POST /api/diagnose
                      │
                      ▼
          FastAPI Backend (Render)
                      │
      ┌───────────────┼────────────────┐
      │               │                │
      ▼               ▼                ▼
 Image Validation  Weather API   Temporary Storage
      │               │
      ▼               ▼
 TensorFlow CNN   Live Weather Data
      │
      ▼
 Disease Prediction
(Plant + Disease + Confidence)
      │
      ▼
 LangChain Orchestrator
      │
      ▼
 Groq Llama LLM
      │
      ▼
 Structured JSON Advisory
      │
      ▼
 Dynamic Frontend Dashboard

🔄 Complete Request Flow

User Uploads Leaf Image
        │
        ▼
Frontend creates FormData
(Image + City)
        │
        ▼
POST /api/diagnose
        │
        ▼
FastAPI receives request
        │
        ▼
Image saved temporarily
        │
        ▼
CNN predicts disease
        │
        ▼
Weather API fetches live weather
        │
        ▼
Prediction + Weather
        │
        ▼
LangChain Prompt
        │
        ▼
Groq LLM
        │
        ▼
Structured JSON
        │
        ▼
Frontend updates dashboard

🤖 Chatbot Architecture

User
 │
 ▼
Frontend
 │
 ▼
POST /api/chat
 │
 ▼
FastAPI
 │
 ▼
Conversation Memory
 │
 ▼
PromptTemplate
 │
 ▼
Groq LLM
 │
 ▼
Response
 │
 ▼
Chat UI

☁ Deployment Architecture

            GitHub Repository
                 │
      ┌──────────┴──────────┐
      ▼                     ▼
   Vercel                Render
 Frontend               Backend
      │                     │
      └──────────┬──────────┘
                 ▼
             HTTPS Users

📂 Folder Structure

CropWise/
├── backend/
│   ├── app.py
│   ├── main_orchestrator.py
│   ├── models/
│   │   └── best_plant_model.keras
│   ├── utils/
│   │   ├── predictor.py
│   │   └── weather_tool.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── diagnose.html
│   ├── chatbot.html
│   ├── style.css
│   └── script.js
├── screenshots/
├── README.md
├── LICENSE
└── .gitignore

🔌 API Endpoints

Method   Endpoint          Description

GET      /               Health CheckPOST     /api/diagnose   Disease DiagnosisPOST     /api/chat       Agricultural Chatbot

⚙ Installation

git clone https://github.com/yourusername/CropWise.git
cd CropWise

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate

pip install -r backend/requirements.txt

🔐 Environment Variables

Create a .env file inside backend/

GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key

▶ Running the Project

cd backend
uvicorn app:app --reload

Backend

http://127.0.0.1:8000

Swagger

http://127.0.0.1:8000/docs

🚀 Future Scope

Retrieval-Augmented Generation (RAG)

ChromaDB Integration

Agricultural Knowledge Base

Grad-CAM Explainability

Fertilizer Recommendation Engine

Crop Yield Prediction

Historical Crop Health Tracking

Authentication & User Accounts

Mobile Application

Regional Language Support

⚠ Disclaimer

CropWise is an educational and decision-support tool. Farmers shouldconsult agricultural experts before applying treatments on a largescale.

👩‍💻 Author

Dhanashree Chandekar

B.Tech -- Artificial IntelligenceNational Institute of Technology (NIT) Rourkela

Email: dchandekar2006@gmail.com
