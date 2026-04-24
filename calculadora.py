from fastapi import FastAPI  

app = FastAPI()

@app.get("/sumar")
async def sumar(n1: int, n2: int):   
    return {       
        "total": n1 + n2
    }
