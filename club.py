from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

lista_socios= []


class Socio(BaseModel):
    dni: int
    nombre:Annotated[str, Field(min_legth=2)]
    esta_al_dia:bool

app= FastAPI()
@app.get("/socios/")
async def consultar_socios():
         return  lista_socios


@app.post("/registrar/")
async def registrar(nuevo_socio:Socio):
    for socio in lista_socios:
        if socio.dni == nuevo_socio.dni:
            raise HTTPException(status_code=400, detail="El socio ya existe")
    lista_socios.append(nuevo_socio)
    return {"mensaje": f"Socio {nuevo_socio.nombre} registrado con éxito"}

@app.delete("/borrar_socio")
async def borrar(socio_dni:int):
    global lista_socios

    socio_encontrado=None
    for socio in lista_socios:
        if socio.dni == socio_dni :
            socio_encontrado= socio
            break
          
    if socio_encontrado is None:
        raise HTTPException(status_code=400, detail="El socio no existe")
          
    lista_socios.remove(socio_encontrado)
    return {"mensaje": f"Socio con DNI {socio_dni} eliminado correctamente"}

    



