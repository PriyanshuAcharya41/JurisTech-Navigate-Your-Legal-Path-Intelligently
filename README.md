# JurisTech: Navigate Your Legal Path

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
![React](https://img.shields.io/badge/React-18-61DAFB?style=for-the-badge&logo=react)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-FF4B4B?style=for-the-badge&logo=streamlit)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100-009688?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**JurisTech** is an advanced AI-powered legal assistant designed to demystify Indian law. It offers two distinct user interfaces: a full-featured **React application** and a simple, rapid-prototype **Streamlit application**. By leveraging a multi-agent system, it provides users with comprehensive legal analysis, identifies relevant IPC sections, researches precedents, and drafts formal legal documents from a simple, natural language description.

!(error.png)

---

## 📋 Key Features

* **🤖 Multi-Agent System:** Utilizes a specialized crew of AI agents (Case Intake, IPC Section, Legal Precedent, and Document Drafter) for a structured and thorough analysis.
* **⚖️ IPC Section Analysis:** Employs Retrieval-Augmented Generation (RAG) with a ChromaDB vector store to accurately identify and explain relevant sections of the Indian Penal Code.
* **📚 Precedent Research:** Integrates with the Tavily search API to find and summarize relevant case law and legal precedents from trusted Indian legal sources.
* **✍️ Automated Document Drafting:** Generates a complete legal document (either as a formatted string or a structured JSON object) based on the comprehensive analysis.
* **✌️ Dual Frontend Options:**
    * A rich, dynamic **React** application for a polished user experience.
    * A fast and simple **Streamlit** application for quick analysis.
* **📜 Response History:** The FastAPI backend automatically saves every successful analysis to a history log.

---

## 🏛️ Architecture

JurisTech supports two distinct operational flows depending on the chosen frontend.

**React Flow (Full-Stack):**
```
+------------------+      +---------------------+      +---------------------+
|  React Frontend  |----->|  FastAPI Backend    |----->|  CrewAI Engine      |
| (localhost:1234) |      | (JSON Output API)   |      | (JSON Task)         |
+------------------+      +---------------------+      +---------------------+
```

**Streamlit Flow (Simple):**
```
+---------------------+      +---------------------+
| Streamlit Frontend  |----->|  CrewAI Engine      |
| (streamlit_app.py)  |      | (Simple Text Task)  |
+---------------------+      +---------------------+
```

---

## 💻 Tech Stack

| Category     | Technology                                                                                                                                                                                                                         |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Frontend** | ![React](https://img.shields.io/badge/-React-61DAFB?style=flat-square&logo=react) ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit) |
| **Backend** | ![FastAPI](https://img.shields.io/badge/-FastAPI-009688?style=flat-square&logo=fastapi) ![Uvicorn](https://img.shields.io/badge/-Uvicorn-ff4081?style=flat-square)                                                                   |
| **AI Core** | ![CrewAI](https://img.shields.io/badge/-CrewAI-orange?style=flat-square) ![LangChain](https://img.shields.io/badge/-LangChain-8A2BE2?style=flat-square) ![OpenAI](https://img.shields.io/badge/-OpenAI-412991?style=flat-square&logo=openai) |
| **Databases**| ![ChromaDB](https://img.shields.io/badge/-ChromaDB-6E44FF?style=flat-square) (Vector Store)                                                                                                                                          |
| **Tools** | ![Tavily](https://img.shields.io/badge/-Tavily_API-blue?style=flat-square) (Precedent Search)                                                                                                                                         |
| **Deployment**| ![Docker](https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker) (Containerization for React/FastAPI)                                                                                                          |

---

## ⚙️ Getting Started

Follow these instructions to set up and run the project locally.

### 1. Initial Setup (Common for Both Frontends)

```bash
# Clone the repository
git clone [https://github.com/PriyanshuAcharya41/JurisTech-Navigate-Your-Legal-Path-Intelligently.git](https://github.com/PriyanshuAcharya41/JurisTech-Navigate-Your-Legal-Path-Intelligently.git)
cd JurisTech-Navigate-Your-Legal-Path-Intelligently

# Create and activate a Python virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Set up your environment variables
# Create a .env file and add your API keys (use .env.example as a template)
cp .env.example .env

# Build the local vector database (one-time setup)
python ipc_vectordb_builder.py
```

### 2. Running the Application

Choose one of the two options below to run the application.

#### **Option A: Run with React Frontend (Full-Featured)**

This requires two terminals.

**In Terminal 1 - Start the Backend:**
```bash
# Your backend API server
uvicorn api:app --reload
```
The backend will be running on `http://localhost:8000`.

**In Terminal 2 - Start the Frontend:**
```bash
# Navigate to the frontend directory
cd frontend

# Install npm dependencies (if you haven't already)
npm install

# Run the React development server
npm start # Or 'npm run dev' depending on your setup (Parcel uses 'start')
```
Your frontend will be running on **`http://localhost:1234`**. Open this URL in your browser.

#### **Option B: Run with Streamlit Frontend (Simple)**

This is a simpler, single-command option. It does not require the Uvicorn server.

```bash
# Make sure you are in the project's root directory
streamlit run streamlit_app.py
```
This will open the Streamlit application directly in your browser.

### 3. Docker Setup (For React/FastAPI Version)

To run the full-stack React and FastAPI application in containers:

```bash
# Make sure Docker Desktop is running
docker-compose up --build
```
The application will be available at `http://localhost:3000`.

---

## 🔗 API Endpoints (For React Version)

The FastAPI backend exposes the following endpoints:

* `POST /analyze`: The main endpoint that accepts a user's legal issue and returns the full JSON analysis.
* `GET /history`: Retrieves a list of all previously saved analyses.

---

## 🙏 Acknowledgments

This project's foundation was inspired by the original `ai-legal-assistant-crewai` repository. It has since been significantly expanded with a full-stack architecture, dual frontend options, structured JSON outputs, and a persistent history feature.
