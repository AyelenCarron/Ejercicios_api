from typing_extensions import Annotated
from fastapi import FastAPI, Path, Query


LibroId= Annotated[int, Path(gt=0)]
Isbn= Annotated[str, Query(min_length=13, max_length=13)]

app= FastAPI()

@app.get("/libros/{libro_id}")
async def biblioteca(libro_id:LibroId, isbn:Isbn):
    return{
        "libro":libro_id,
        "isbn": isbn
    }