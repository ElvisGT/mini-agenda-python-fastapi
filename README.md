# 🥷 Ninja Contactos API – FastAPI

API REST para gestionar contactos. CRUD completo en memoria usando FastAPI.

## 🚀 Tecnologías
- Python 3.13.3
- FastAPI + Uvicorn
- Pydantic

## 🧠 Funciones
- `GET /contactos` – Listar
- `POST /contactos` – Agregar (con validación)
- `GET /contactos/{nombre}` – Buscar
- `PUT /contactos/{nombre}` – Editar

## ⚙️ Uso rápido

```bash
pip install fastapi uvicorn
uvicorn main:app --reload
```
