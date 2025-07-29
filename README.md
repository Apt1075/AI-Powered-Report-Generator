# 🚀 Backend: AI-Powered Shipment Report Generator

This is the **backend** for the AI-Powered Shipment Report Generator — a FastAPI application that processes **natural language queries**, converts them into **MongoDB filters** using a **FLAN-T5 model**, and returns shipment reports from the database.

---

## ✅ Features

- 🧠 Natural Language Query → MongoDB Filter using **FLAN-T5 (Hugging Face)**
- 📦 Retrieves filtered shipment data from **MongoDB**
- ⚡ Built with **FastAPI** for speed and simplicity
- 📤 Returns JSON response for frontend AG Grid
- 📂 Supports date range, district, and trip status filtering
- 🔌 Modular structure for easy scaling and maintenance

---

## 📁 Folder Structure

│ ├── main.py # Entry point for FastAPI app
│ ├── db.py # MongoDB connection logic
│ ├── query_builder.py # Converts NLP output to MongoDB query
│ ├── nlp_model.py # Loads and uses FLAN-T5 model
│ ├── schema.py # Pydantic models for request/response
│ └── sample_data.json # Sample shipment data for testing
│
├── .env # Environment variables (Mongo URI, etc.)
├── requirements.txt # Python dependencies
└── README.md # This file
