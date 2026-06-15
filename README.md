# 🌿 CropWise – AI-Powered Crop Disease Diagnosis & Advisory Platform

## Overview

CropWise is an intelligent agricultural assistance platform that combines **Computer Vision**, **Deep Learning**, **Real-Time Weather Intelligence**, and **Generative AI** to help farmers and agricultural enthusiasts identify crop diseases and receive actionable treatment recommendations.

The platform enables users to upload a leaf image and specify their location. A trained deep learning model analyzes the image to detect plant diseases, while live weather data is incorporated to generate personalized disease management recommendations. Additionally, CropWise includes a dedicated AI-powered agricultural chatbot capable of answering plant, farming, soil, and crop-related queries.

---

## Key Features

### 🌱 AI-Based Crop Disease Detection

* Upload a leaf image for instant disease analysis.
* Supports **38 plant disease classes** across multiple crop types.
* Powered by a CNN-based image classification model.
* Detects both healthy and diseased plant conditions.

### 🌦️ Real-Time Weather Intelligence

* Fetches live weather conditions based on the user's city.
* Integrates temperature, humidity, wind speed, and weather conditions into recommendations.
* Generates weather-aware disease management strategies.

### 🤖 AI Advisory Report Generation

Generates detailed crop reports including:

* Disease severity assessment
* Disease description and causes
* Weather-based risk analysis
* Organic treatment recommendations
* Chemical treatment recommendations
* Estimated treatment costs
* Recovery timeline
* Preventive measures
* Ranked treatment plans

### 💬 CropWise Botanical Assistant

An AI-powered agricultural chatbot that:

* Answers questions related to crops, diseases, farming, soil health, irrigation, fertilizers, and pest management.
* Provides India-focused recommendations.
* Supports multilingual interactions.
* Maintains conversational context for follow-up questions.

### 🎨 Modern User Interface

* Interactive image upload interface
* Real-time result visualization
* Weather dashboard
* Treatment recommendation panels
* Agricultural chatbot interface

---

## Supported Crops

CropWise currently supports disease detection for:

* Apple
* Blueberry
* Cherry
* Corn (Maize)
* Grape
* Orange
* Peach
* Bell Pepper
* Potato
* Raspberry
* Soybean
* Squash
* Strawberry
* Tomato

---

## Technology Stack

### Backend

* Python
* FastAPI
* LangChain
* Groq LLM API
* WeatherAPI

### Deep Learning

* TensorFlow
* Keras
* MobileNetV2-based CNN Architecture
* NumPy

### AI Components

* Large Language Models (LLMs)
* Prompt Engineering
* Structured JSON Output Generation
* Conversational Memory Management

### Frontend

* HTML5
* CSS3
* JavaScript

---

## Project Architecture

```text
User Uploads Leaf Image + City
             │
             ▼
      Disease Prediction Model
             │
             ▼
       Disease Classification
             │
             ▼
        Weather Data Fetch
             │
             ▼
      AI Advisory Generation
             │
             ▼
      Structured Crop Report
             │
             ▼
         Frontend Dashboard
```

---

## Folder Structure

```text
CropWise/
│
├── backend/
│   ├── app.py
│   ├── main_orchestrator.py
│   ├── utils/
│   │   ├── predictor.py
│   │   └── weather_tool.py
│   ├── models/
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── diagnose.html
│   ├── chatbot.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/CropWise.git
cd CropWise
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the backend directory:

```env
GROQ_API_KEY=your_groq_api_key
WEATHER_API_KEY=your_weather_api_key
```

---

## Model Setup

Place the trained model file at:

```text
backend/models/best_plant_model.keras
```

The model file is not included in this repository due to its large size.

---

## Running the Backend

Navigate to the backend directory and start the FastAPI server:

```bash
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Future Enhancements

* Retrieval-Augmented Generation (RAG) integration
* Agricultural knowledge base support
* Fertilizer recommendation engine
* Crop yield prediction
* Multi-leaf image analysis
* Mobile application deployment
* Regional language expansion
* Historical crop health tracking

---

## Disclaimer

CropWise is intended as a decision-support tool for educational and agricultural assistance purposes. Users should consult agricultural experts or local extension services before implementing large-scale crop treatment decisions.

---

## Author

**Dhanashree Chandekar**

B.Tech in Artificial Intelligence
National Institute of Technology (NIT) Rourkela

Email: [dchandekar2006@gmail.com](mailto:dchandekar2006@gmail.com)


