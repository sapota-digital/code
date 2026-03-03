from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])


class UserCreate(BaseModel):
    name: str
    email: str


@router.get("/")
def list_users():
    return []


@router.post("/", status_code=201)
def create_user(user: UserCreate):
    return {"id": 1, **user.model_dump()}


@router.get("/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}


@router.put("/{user_id}")
def update_user(user_id: int, user: UserCreate):
    return {"id": user_id, **user.model_dump()}


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    return None
