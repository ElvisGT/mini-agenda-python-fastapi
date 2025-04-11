from fastapi import FastAPI,HTTPException
from pydantic import BaseModel


app = FastAPI()

contactos = []

class Contacto(BaseModel):
    nombre:str
    telefono:str

@app.get("/")
def read_root():
    return {"Mensaje":"Api Ninja lista"}

@app.get("/contactos")
def get_contactos():
    return contactos

@app.post("/contacto")
def create_contacto(contacto:Contacto):
    for c in contactos:
        if c.nombre.lower() == contacto.nombre.lower():
            return {"Mensaje":"El usuario ya existe"}
    contactos.append(contacto.dict())
    return {"mensaje":"Contacto agregado","contacto":contacto}

@app.get("/contactos/{nombre}")
def get_contact(nombre:str):
    for c in contactos:
        if c.nombre.lower() == nombre.lower():
            return c
    raise HTTPException(status_code=404,detail='Usuario no encontrado')

@app.put("/contactos/{nombre}")
def update_contact(nombre:str,contacto:Contacto):
    for i,c in enumerate(contactos):
        if c['nombre'].lower() == nombre.lower():
            c[i] = contacto
            return {"Mensaje":"Usuario creado correctamente","Contacto":contacto}
    
    raise HTTPException(status_code=404,detail="Usuario no encontrado")