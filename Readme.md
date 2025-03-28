# AI-Powered Personalized Learning Platform

## Overview
The AI-Powered Personalized Learning Platform is a web application that offers customized learning experiences using advanced technologies like face recognition, mind map generation, and user progress tracking. The project is built with a FastAPI backend and a React frontend.

## Features
- Face Recognition: Enhances learning analysis by detecting user engagement and emotional state.
- Mind Map Generation: Visualizes learning paths and concepts for effective comprehension.
- User Progress Tracking: Tracks and displays user progress over time.
- Analytics Dashboard: Provides insights into learning patterns and areas of improvement.

## Architecture
The platform consists of two main components:
- **Backend** (FastAPI)
- **Frontend** (React with Tailwind CSS)

They communicate via REST API.

## Technologies Used
- Backend: FastAPI, Python, YOLO (for face recognition), NLP, SQLite (default), PostgreSQL (production)
- Frontend: React, Tailwind CSS
- Docker & Docker Compose for deployment

## Installation

### Clone the Repository
```sh
git clone <repository-url>
cd AI-Learning-Platform
```

### Backend Setup
```sh
cd backend
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup
```sh
cd frontend
npm install
npm start
```

### Docker Setup
```sh
docker-compose build
docker-compose up
```

## Usage
- Backend runs at `http://localhost:8000`
- Frontend runs at `http://localhost:3000`
- API documentation available at `http://localhost:8000/docs`

## Future Enhancements
- Enhanced analytics and reporting.
- Improved learning path generation using NLP.
- Face expression recognition for better engagement tracking.

## Author
Your Name

## License
MIT License

