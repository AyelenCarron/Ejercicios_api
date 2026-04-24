from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Path, Query

app=FastAPI()

biblioteca=[]

class Libro(BaseModel):
    titulo: str = Field(min_length=3)
    autor : str = Field(min_length=2)
    paginas : int = Field(ge=0)

@app.post("/libro")
async def nuevo_libro(nuevo_libro:Libro):
    biblioteca.append(nuevo_libro.model_dump())
    return {
        "Mensaje":"Nuevo libro añadido",
        "Dato": nuevo_libro
    }


