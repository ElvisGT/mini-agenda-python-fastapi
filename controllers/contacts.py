from fastapi import HTTPException,APIRouter,Query
from models.contact import Contacto
from datetime import datetime

contactos = []

def root():
    return {"Mensaje":"Api Ninja lista"}


def search(nombre:str):
    resultados = []
    for c in contactos:
        if nombre.lower() in c['nombre'].lower():
            resultados.append(c)
    if len(resultados) == 0:
        raise HTTPException(status_code=404,detail="No econtrados contactos")
    return {"Mensaje":f"{len(resultados)} resultados encontrados","Resultados":resultados}

def all_contactos():
    if len(contactos) == 0:
        raise HTTPException(status_code=404,detail="No hay contactos que mostrar")
    return contactos

def create(contacto:Contacto):
    contact_dict = contacto.dict()
    for c in contactos:
        if c['nombre'].lower() == contacto.nombre.lower():
            return {"Mensaje":"El usuario ya existe"}
    
    contact_dict["fecha_creacion"] = datetime.now().isoformat()
    contactos.append(contact_dict)
    return {"mensaje":"Contacto agregado","contacto":contact_dict}

def contact(nombre:str):
    for c in contactos:
        if c['nombre'].lower() == nombre.lower():
            return c
    raise HTTPException(status_code=404,detail='Usuario no encontrado')

def update(nombre:str,contacto:Contacto):
    contact_dict = contacto.dict()
    for i,c in enumerate(contactos):
        if c['nombre'].lower() == nombre.lower():
            c[i] = contact_dict
            contact_dict["fecha_creacion"] = c.get("fecha_creacion")
            return {"Mensaje":"Usuario creado correctamente","Contacto":contact_dict}
    
    raise HTTPException(status_code=404,detail="Usuario no encontrado")

def delete(nombre:str):
    for i,c in enumerate(contactos):
        if c['nombre'].lower() == nombre.lower():
            contactos.pop(i)
            return {"Mensaje":"Eliminado exitosamente"}
    raise HTTPException(status_code=404,detail="Usuario no encontrado")
