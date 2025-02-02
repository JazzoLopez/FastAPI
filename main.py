from fastapi import FastAPI, HTTPException
from uuid import uuid4, UUID
from typing import List
from src.models.models import Genre, Role, User

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        firstName="Marco",
        lastName="Luna",
        genre=Genre.male,
        role=Role.admin,
    ),
    User(
        id=uuid4(),
        firstName="Brayto",
        lastName="Luna",
        genre=Genre.male,
        role=Role.admin,
    ),
    User(
        id=uuid4(),
        firstName="aziel",
        lastName="Luna",
        genre=Genre.male,
        role=Role.admin,
    ),
    User(
        id=uuid4(),
        firstName="Irving",
        lastName="Luna",
        genre=Genre.male,
        role=Role.admin,
    ),
]


@app.get("/")
async def root():
    return {"message": "Hola, bienvenidos!"}


@app.get("/api/users")
async def get_users():
    return db


@app.post("/api/users")
async def create_users(user: User):
    db.append(user)
    return {"message": "User created successfully", "id": user.id}


@app.delete("/api/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": f"User with id {id} deleted successfully"}
    raise HTTPException(
        status_code=404, detail=f"Error al eliminar, el id {id} no fue encontrado"
    )


@app.put("/api/users/{id}")
async def update_user(id: UUID, user: User):
    for idx, existing_user in enumerate(db):
        if existing_user.id == id:
            # Actualizar los campos del usuario existente con los nuevos datos
            db[idx].firstName = user.firstName
            db[idx].lastName = user.lastName
            db[idx].genre = user.genre
            db[idx].role = user.role
            return {"message": f"User with id {id} updated successfully"}
    raise HTTPException(status_code=404, detail=f"User with id {id} not found")
