from fastapi import APIRouter,Query
from controllers.contacts import contact,create,update,search,delete,all_contactos,root
from models.contact import Contacto

router = APIRouter()

@router.get("/")
def read_root():
    return root()

# Buscador y paginacion
@router.get("/contactos/buscar")
def search_contacts(nombre:str = Query(...,min_length=1)):
    return search(nombre)

@router.get("/contactos")
def get_contactos():
    return all_contactos()

@router.post("/contacto")
def create_contacto(contacto:Contacto):
    return create(contacto)

@router.get("/contactos/{nombre}")
def get_contact(nombre:str,contacto:Contacto):
    return contact(nombre,contacto)

@router.put("/contactos/{nombre}")
def update_contact(nombre:str,contacto:Contacto):
    return update(nombre,contacto)

@router.delete("/contactos/{nombre}")
def delete_contact(nombre:str,contacto:Contacto):
    return delete(nombre,contacto)
