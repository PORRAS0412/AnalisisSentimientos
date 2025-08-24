from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Crear la app
app = FastAPI()

# Cargar tu modelo (ejemplo: sentiment-analysis)
model = pipeline("sentiment-analysis")

# Definir formato de entrada
class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API de mi modelo funcionando 🚀"}

@app.post("/predict")
def predict(data: InputText):
    result = model(data.text)
    return {"result": result}