from fastapi import FastAPI, File, UploadFile
from image_predictor import ImagePredictor
from PIL import Image
import io

app = FastAPI()

predictor = ImagePredictor()

@app.post("/scorefile/")
async def create_upload_file(file: UploadFile = File(...)):
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    print(img.mode)
    if img.mode in ['p', 'RGBA']:
        img = img.convert('RGB')
        print(img.mode)
    results = predictor.predict_from_file(img)
    return {i: {'bndbox': [int(v[0][0][0]), int(v[0][0][1]), int(v[0][1][0]), int(v[0][1][1])], 'text': v[1], 'score': v[2]} for i, v in enumerate(results)}
    