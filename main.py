from fastapi import FastAPI

app=FastAPI()

@app.get("/usuario/{username}")
async def get_usuario(username, rol):
    acceso="permitido" if rol == "estudiante" else "denegado"
    return{
        "user":username,
        "perfil": rol,
        "acceso":acceso
    }

@app.get("/holamundo/")
async def holamundo():
    return {
        "mensaje":"Hola mundo"
    }

@app.get("/convertir/{pesos}")
async def get_converir(pesos: int):    
    return{        
        "dolares":round(pesos/1400, 2)
    }

@app.get("/sumar")
async def sumar(n1:int, n2:int):   
    return{       
        "total": n1 + n2
    }
@app.get("/personaje/{indice_actor}")
async def diccionario(indice_actor:str):
    nombre_limpio=indice_actor.strip().title()

    diccionario={
      "Di Caprio":"Titanic",
      "Homero Simpson":"Los Simpson",
      "Sheldon":"The bigbang Theory",
      "Margot Robbie": "Barbie",
      "Merly Streap": "El diablo viste a la moda"
    }
    if nombre_limpio in diccionario:
        return{
           "personaje": nombre_limpio,
           "obra": diccionario[nombre_limpio]
        }
    for  artista in diccionario:
        if nombre_limpio in artista:
            return{
                "nota":"Busqueda parcial encontrada",
                "personaje": artista,
                "obra": diccionario[artista]
            
            }

    return { f"{nombre_limpio} no se encuentra en nuestra lista"}
    