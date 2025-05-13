
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import mlflow.sklearn

app = FastAPI()
model = mlflow.sklearn.load_model("modelo_sorvete")

class Entrada(BaseModel):
    temperatura: float

@app.post("/prever")
def prever_venda(dado: Entrada):
    pred = model.predict([[dado.temperatura]])
    return {"vendas_previstas": float(pred[0])}
