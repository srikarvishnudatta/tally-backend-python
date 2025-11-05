from pydantic import BaseModel, Field


class LoginUser(BaseModel):
    email: str = Field("Email is required")
    password: str = Field("Password is required")


class CreateUser(BaseModel):
    email: str
    password: str
    firstName: str
    lastName: str
