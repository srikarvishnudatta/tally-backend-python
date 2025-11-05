from fastapi import APIRouter, Response, Depends
from sqlalchemy.orm import Session
from src.database.database import get_db
from src.service.auth_service import AuthService
from src.dto.user_dto import LoginUser

auth_router = APIRouter(prefix="/auth")

def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(
        db
    )

@auth_router.post("/login")
async def login(response: Response, data:LoginUser, auth_service: AuthService = Depends(get_auth_service)):
    token = await auth_service.login_user(data=data)
    response.set_cookie("access_token", 
                        value=token,  
                        httponly=True,
                        expires="")
    return