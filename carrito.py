from typing_extensions import Annotated
from pydantic import BaseModel, Field
from fastapi import FastAPI, HTTPException

app= FastAPI()


Carrito=[]

class Producto(BaseModel):
    nombre:str
    precio:int=Field(gt=0)

@app.post ("/llenar_carrito")
async def lista_compra(producto: Producto):
    Carrito.append(producto)
    return {"mensaje": "Producto agregado", "producto": producto}

@app.get ("/total")
async def suma_carrito():
    total= sum(producto.precio for producto in Carrito)
    return {
        "cantidad_productos": len(Carrito),
        "total_a_pagar": total
    }

    







