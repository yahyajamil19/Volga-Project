from fastapi import FastAPI, UploadFile, File
from transcriber import transcribe_audio
import shutil
import os

app = FastAPI(title="Speech Transcription Pipeline")

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = transcribe_audio(filepath)

    return result
