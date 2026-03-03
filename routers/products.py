from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["products"])


class ProductCreate(BaseModel):
    name: str
    price: float


@router.get("/")
def list_products():
    return []


@router.post("/", status_code=201)
def create_product(product: ProductCreate):
    return {"id": 1, **product.model_dump()}


@router.get("/{product_id}")
def get_product(product_id: int):
    return {"id": product_id}


@router.put("/{product_id}")
def update_product(product_id: int, product: ProductCreate):
    return {"id": product_id, **product.model_dump()}


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int):
    return None
