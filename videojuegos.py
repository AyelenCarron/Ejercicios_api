from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI

AnioLanzamiento= Annotated[int, Field(gt=1950)]

class Juego(BaseModel):
    titulo: Annotated[str,Field(min_length=2)]
    genero: str
    lanzamiento:AnioLanzamiento
    
app= FastAPI()

@app.post("/juegos/")
async def enviar_juego(juego:Juego):
    return {
        "msg":"Juego enviado",
        "datos":juego
    }
