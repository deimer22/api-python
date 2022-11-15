from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

list=[]

class paquete(BaseModel):
    codigoUsuario:int
    codigoProducto:int
    peso:int
    pais:str
    direccion:str
    departamento:str
    cuidad:str
    estado:str
    codigoPostal:int

@app.get("/entrega")
def ver ():
     return list

@app.post ("/insert")
def guardardato(dato:paquete):
     list.append(dato)
     return {"mensaje":"guardados"}
