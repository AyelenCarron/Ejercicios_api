from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI


class Notificacion(BaseModel):
    mensaje:Annotated[str, Field(gt=2, lt=140)]
    prioridad:Annotated[int, Field(gt=0, lt=6)]

app= FastAPI()

@app.post("/notificar/")
async def recibir_notificacion(notificar:Notificacion):
    return{
        "msg":"Llegó una notificación",
         "info": notificar
    }