from pydantic import BaseModel
from typing import Optional

class Contacto(BaseModel):
    nombre:str
    telefono:str
    fecha_creacion:Optional[str] = None
