from fastapi import FastAPI

from routers import products, users

app = FastAPI()
app.include_router(users.router)
app.include_router(products.router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
