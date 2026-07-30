# 🌿 CropWise – AI-Powered Crop Disease Diagnosis & Advisory Platform

An end-to-end AI-powered agricultural platform that combines **Computer Vision, Deep Learning, Weather Intelligence, and Generative AI** to diagnose crop diseases and provide personalized treatment recommendations.

---

## 🚀 Live Demo
 https://crop-wise-fawn.vercel.app/

---

<!-- ## 📸 Project Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

---

### 🔍 Disease Diagnosis

![Diagnosis](screenshots/diagnosis.png)

---

### 📊 AI Advisory Report

![Report](screenshots/report.png)

---

### 🤖 AI Chatbot

![Chatbot](screenshots/chatbot.png)

--- -->

# 📖 Overview

CropWise is an AI-powered agricultural decision-support platform that enables farmers to identify crop diseases from leaf images and receive intelligent treatment recommendations.

The platform combines:

- 🌱 CNN-based crop disease classification
- 🌦️ Real-time weather intelligence
- 🤖 Large Language Models (Groq Llama)
- 🔗 LangChain orchestration
- 💬 AI-powered agricultural chatbot

---

# ✨ Key Features

- ✅ Classifies **38 disease & healthy crop classes**
- ✅ Supports **14 crop species**
- ✅ CNN-based deep learning disease detection
- ✅ Real-time weather integration
- ✅ AI-generated treatment recommendations
- ✅ Preventive measures and fertilizer suggestions
- ✅ Disease severity estimation
- ✅ Interactive AI chatbot
- ✅ Responsive web interface
- ✅ FastAPI backend with REST APIs
- ✅ Deployable on Render & Vercel

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript

## Backend

- FastAPI
- Python

## Machine Learning

- TensorFlow
- Keras (VGG16 Transfer Learning)

## AI & LLM

- LangChain
- Groq Llama 3

## APIs

- Weather API

## Deployment

- Render
- Vercel

---

# 🧠 Model Details

| Property | Value |
|----------|-------|
| Model | CNN (VGG16 Transfer Learning) |
| Dataset | PlantVillage |
| Crop Species | 14 |
| Disease Classes | 38 |
| Framework | TensorFlow/Keras |

---

# 🔄 System Architecture

```text
                    User
                      │
                      ▼
             Upload Leaf Image
                      │
                      ▼
            JavaScript Frontend
                      │
          Image + City Information
                      │
                      ▼
            FastAPI Backend API
                      │
     ┌────────────────┼────────────────┐
     │                │                │
     ▼                ▼                ▼
 CNN Disease     Weather API      LangChain
 Prediction      Integration      Orchestrator
     │                │                │
     └────────────────┼────────────────┘
                      ▼
              Groq Llama-3 LLM
                      │
                      ▼
        Structured AI Advisory Report
                      │
                      ▼
             Frontend Dashboard
```

---

# 🔄 Request Flow

```text
User Uploads Leaf Image
          │
          ▼
Frontend Creates FormData
(Image + City)
          │
          ▼
POST /api/diagnose
          │
          ▼
FastAPI Backend
          │
          ├── CNN Prediction
          ├── Weather API
          ├── LangChain Prompt
          └── Groq LLM
          │
          ▼
Structured JSON Response
          │
          ▼
Interactive Dashboard
```

---

# 🤖 Chatbot Workflow

```text
User Question
      │
      ▼
Frontend Chat Interface
      │
      ▼
POST /api/chat
      │
      ▼
FastAPI
      │
      ▼
LangChain Prompt
      │
      ▼
Groq Llama-3
      │
      ▼
AI Response
      │
      ▼
Chat Interface
```

---

# 📂 Folder Structure

```text
CropWise
│
├── backend
│   ├── app.py
│   ├── main_orchestrator.py
│   ├── predictor.py
│   ├── weather_tool.py
│   ├── requirements.txt
│   └── models
│       └── best_plant_model.keras
│
├── frontend
│   ├── index.html
│   ├── diagnose.html
│   ├── chatbot.html
│   ├── style.css
│   └── script.js
│
├── screenshots
│   ├── home.png
│   ├── diagnosis.png
│   ├── report.png
│   └── chatbot.png
│
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<YOUR_GITHUB_USERNAME>/CropWise.git
cd CropWise
```

---

## Backend Setup

```bash
cd backend

pip install -r requirements.txt

python app.py
```

---

## Frontend

Open

```
frontend/index.html
```

or deploy using Vercel.

---

# 🚀 Future Enhancements

- 📱 Android application
- 🌍 Multi-language support
- 📍 GPS-based weather detection
- 📷 Live camera disease detection
- ☁️ Cloud image storage
- 📈 Farmer analytics dashboard
- 🔔 Smart crop alerts
- 🌾 Yield prediction

---

# 👩‍💻 Author

**Dhanashree Chandekar**

- GitHub: https://github.com/<YOUR_GITHUB_USERNAME>
- LinkedIn: https://www.linkedin.com/in/<YOUR_LINKEDIN_USERNAME>/

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is licensed under the MIT License.