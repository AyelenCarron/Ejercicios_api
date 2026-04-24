from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, Path, Query

app=FastAPI()

UserName=Annotated[str, Path(description="Nombre de usuario")]
Rol=Annotated[str, Query(description="Rol de estudiante")]

@app.get("/usuario/{username}")
async def datos_usuario(username:UserName, rol:Rol):
    if rol not in ["estudiante","profesor"]:
        return{
        "user":username,
        "perfil": rol,
        "acceso": "acceso denegado"
        }
    return{
    "user":username,
    "perfil": rol,
    "acceso": "acceso permitido"
    }