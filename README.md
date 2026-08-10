# Multimodal AI Assistant

A complete multimodal AI assistant built with FastAPI and Streamlit. This project supports authenticated users, PDF and image uploads, retrieval-augmented chat, AI vision processing, and downloadable PDF report generation.

## Overview

This project includes:
- FastAPI backend with authentication, upload, chat, and report endpoints
- Streamlit frontend with login/signup, chat, document upload, image upload, and report generation
- Local SQLite storage for users, chats, and messages
- PDF text extraction, chunking, and FAISS vector store creation for document QA
- Image processing with AI vision prompts
- Reports generated as downloadable PDF files

## Features

- User signup and login with JWT authentication
- Upload PDF files for text extraction and knowledge retrieval
- Upload PNG/JPG/JPEG images for vision-based question answering
- Chat assistant that answers questions using uploaded PDF/document or image context
- Generate PDF conversation reports from chat sessions
- Health check endpoint and root welcome endpoint

## Project Structure

- `app/main.py` - FastAPI application entry point
- `app/api/auth.py` - Signup and login endpoints
- `app/api/upload.py` - PDF/image upload and vector store creation
- `app/api/ask.py` - Chat endpoint for PDF and image QA
- `app/api/report.py` - PDF report generation endpoint
- `app/services/` - Core AI, PDF, image, vector store, and auth services
- `app/database/` - Database models, connection, and session utilities
- `frontend/app.py` - Streamlit frontend interface
- `uploads/` - Saved uploaded files
- `reports/` - Generated PDF reports
- `data/faiss_index/` - FAISS vector database index files
- `requirements.txt` - Python dependencies

## Tech Stack

- Python
- FastAPI
- Streamlit
- SQLAlchemy + SQLite
- FAISS
- Google Gemini via `langchain_google_genai`
- ReportLab
- Requests
- python-multipart

## Requirements

- Python 3.11+ recommended
- `.env` file with at least:
  - `GEMINI_API_KEY`
  - `SECRET_KEY`
  - `API_URL` (optional, defaults to `http://127.0.0.1:8000`)

## Setup

1. Clone the repository
2. Create and activate a virtual environment (optional but recommended)
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the required secrets:

```env
GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_jwt_secret
API_URL=http://127.0.0.1:8000
```

## Running the Application

### Start the backend

```bash
uvicorn app.main:app --reload
```

The backend will be available at:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/health

### Start the frontend

```bash
streamlit run frontend/app.py
```

The Streamlit app will open in your browser at:
- http://localhost:8501

## Usage

1. Open the Streamlit app in your browser
2. Signup or login with your email and password
3. Upload a PDF or image
4. Use the chat interface to ask questions about the uploaded content
5. Generate a PDF report from the conversation
6. Download the generated report from the frontend

## API Endpoints

- `POST /signup` - register a new user
- `POST /login` - obtain a JWT access token
- `POST /upload` - upload PDF or image file
- `POST /ask` - ask questions about the uploaded document/image
- `POST /generate-report` - create a PDF chat report
- `GET /health` - health check endpoint

## Notes

- Uploaded files are saved in `uploads/`
- Generated conversation reports are saved in `reports/`
- The project currently uses local SQLite database storage (`chat.db`)
- The assistant uses retrieval-augmented generation for PDF content and AI vision processing for images
