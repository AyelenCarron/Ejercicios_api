from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI


class Alumno(BaseModel):
    nombre : str = Field(min_length=3 , max_length=50)
    materia : str = Field(min_length=2)
    nota : float = Field(ge=0, le=10)

app = FastAPI()

alumnos_db = []

@app.post("/alumnos")
async def crear_alumno(nuevo_alumno : Alumno):
    alumnos_db.append(nuevo_alumno.model_dump())
    return {
        "mensaje":"Alumno registrado exitosamente",
        "datos": nuevo_alumno
    }

@app.get("/alumnos")
async def get_alumnos():
    return {
        "mensaje": "Listado de alumnos",
        "datos": alumnos_db
    }

@app.get("/")
async def hola_mundo():
    return {
        "mensaje": "Hola Mundo"
    }

@app.get("/bienvenida")
async def bienvenida():
    return {
        "mensaje": "Bienvenidos a mi API REST hecha con fastapi"
    }

@app.get("/users/{user_id}")
async def ver_usuario(user_id : int):
    return{
        "mensaje": "Id del usuario",
        "ID": user_id
    }

@app.get("/buscar")
async def buscar(nombre : str, cantidad : int = 1):
    return{
        "Producto" : nombre,
        "Cantidad" : cantidad
    }

@app.get("/usuario/{username}")
async def get_acceso(username : str, rol : str):
    
    acceso = "permitido" if rol == "estudiante" else "denegado"

    return {
        "user": username,
        "perfil": rol,
        "acceso": acceso
    }