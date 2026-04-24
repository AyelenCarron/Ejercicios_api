from fastapi import FastAPI

app=FastAPI()

videoteca=[
    {"Jack Dawson": "Titanic"},
    {"Sheldon": "The bigbang theory"},
    {"Miranda Prestly": "El diablo viste a la moda"}, 
    {"Minnie Jackson": "Historias cruzadas"},
    {"Rose Maxson": "Fences"}
    ]

@app.get("/personaje/{id}")
async def diccionario_peronajes(id:int):
    if 0<= id <len(videoteca):
        return {
           "El personaje es": videoteca[id]
        }
    else:
        return{
            "Personaje no encontrado"
        }