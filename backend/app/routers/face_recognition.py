from fastapi import APIRouter, UploadFile, File
import cv2
import numpy as np

router = APIRouter(
    prefix="/face_recognition",
    tags=["Face Recognition"]
)

@router.post("/detect/")
async def detect_faces(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Use a pre-trained YOLO model for face detection (simple placeholder)
    # Replace with your actual YOLO model for better results
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    detected_faces = faces.detectMultiScale(gray, 1.1, 4)
    
    response = [{"x": x, "y": y, "w": w, "h": h} for (x, y, w, h) in detected_faces]
    return {"faces": response}
