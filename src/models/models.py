from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Genre(str, Enum):
    male = "masculino"
    female = "femenino"


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4
    firstName: str
    lastName: str
    genre: Genre
    role: Role
