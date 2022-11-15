from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

list=[]

class Envio(BaseModel):
     codidoUsuario:int
     codigoDelProduto:int
     nombre:str
     apellido:str
     pais:str
     direccion:str
     departamento:str
     cuidad:str
     estado:str
     codigoPostal:int
     telefono:int

@app.get("/envio")
def ver ():
     return list

@app.post ("/insert")
def guardardato(dato:Envio):
     list.append(dato)
     return {"mensaje":"guardados"}
