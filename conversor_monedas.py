from fastapi import FastAPI

app=FastAPI()

@app.get("/convertir/{pesos}")
async def get_converir(pesos: int):    
    return{        
        "dolares":round(pesos/1400, 2)
    }
