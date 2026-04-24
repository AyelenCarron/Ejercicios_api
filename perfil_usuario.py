from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI

class Perfil(BaseModel):
    nombre_completo:str
    biografia: str = Field(default="Sin descripción", max_length=200)

app= FastAPI()

@app.post("/perfil/")
async def usuario_perfil(usuario:Perfil):
    return{
        "mensaje": "Perfil recibido",
        "nombre de usuario":usuario
    }
        
        