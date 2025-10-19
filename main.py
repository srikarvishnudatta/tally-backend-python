from fastapi import FastAPI, APIRouter
from src.routers.auth_router import auth_router
from src.routers.expense_router import expense_router
from src.routers.group_router import group_router

app = FastAPI()

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(expense_router)
api_router.include_router(group_router)

app.include_router(api_router)


@app.get("/")
def hello() -> str:
    return "Hello world"


@app.get("/status")
def check_status():
    return {"status": "healthy"}
