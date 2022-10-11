from fastapi import FastAPI, File, UploadFile
from .image_predictor import ImagePredictor
from PIL import Image
import io
import numpy as np

app = FastAPI()

predictor = ImagePredictor()

@app.get("/")
def welcome():
    return {"welcome": "ocr-fast-api"}

@app.post("/ocr/")
async def create_upload_file(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    results = predictor.predict_from_file(np.asarray(img))
    print(results)
    return {i: {'bndbox': [int(v[0][0][0]), int(v[0][0][1]), int(v[0][1][0]), int(v[0][1][1])], 'text': v[1], 'score': v[2]} for i, v in enumerate(results)}
    
