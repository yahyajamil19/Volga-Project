from fastapi import FastAPI, UploadFile, File
import shutil
import os

from azure_speech import transcribe_audio

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/transcribe")
async def upload_audio(file: UploadFile = File(...)):

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = transcribe_audio(filepath)

    return result
