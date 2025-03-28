from fastapi import FastAPI
from app.routers import users, face_recognition, mind_map
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(face_recognition.router)
app.include_router(mind_map.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered Personalized Learning Platform"}
