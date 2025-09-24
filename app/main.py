from fastapi import FastAPI, UploadFile, File
from app.model import predict

app = FastAPI()

@app.get("/")
def health():
    return {"status" : "ok"}

@app.post("/predict")
async def get_prediction(file: UploadFile = File(...)):
    image_bytes = await file.read()
    preds = predict(image_bytes)
    return {"predictions": preds}
