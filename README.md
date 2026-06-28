# Arcanus Project

A 3-Layer Privacy-Preserving Enterprise Firewall and Frontend.

## Project Structure

- `frontend/`: Next.js application.
- `backend/`: FastAPI application.
- `Arcanus/`: Main configuration and shared resources.

## Prerequisites

- Node.js (v18+)
- Python (v3.11+)
- Git

## Getting Started

### 1. Clone the repository
```bash
git clone <repository-url>
cd Arcanus
```

### 2. Backend Setup
Navigate to the root `Arcanus` directory (the inner one containing the `backend` folder):

```bash
cd Arcanus
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt
```

> [!TIP]
> If you encounter `ModuleNotFoundError: No module named 'litellm.types'` on Windows, try re-installing a specific version of litellm:
> `pip install litellm==1.40.0` or `pip install litellm --upgrade`.

### 3. Frontend Setup
Navigate to the `frontend` directory:

```bash
cd Arcanus/frontend
npm install
```

### 4. Configuration
Ensure you have the `.env` files set up in both `frontend` and `backend` directories. Use the `.env.example` files as templates.

### 5. Running the Project

#### Run Backend
In the `Arcanus/backend` directory (with virtual environment activated):
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

#### Run Frontend
In the `Arcanus/frontend` directory:
```bash
npm run dev
```
The application will be available at `http://localhost:3000`.

## Features
- Agentic AI Firewall
- Privacy-preserving layers
- Modern dashboard UI
