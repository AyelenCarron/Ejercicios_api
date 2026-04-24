from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator # Corregido: validator
from typing_extensions import Annotated


app=FastAPI()

class Medicion(BaseModel):
    valor: float
    unidad: Annotated [str, Field(pattern = "^(C|F)$")]

    @field_validator("valor")
    @classmethod
    def validar_cero_absoluto(cls, v: float,info):
     if info.data.get("unidad") == "C" and v< -273.15:
        raise ValueError(" La temperatura no puede ser menor a cero")
     return v
