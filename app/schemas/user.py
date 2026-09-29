from pydantic import BaseModel, Field, EmailStr

class CreateUser(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=3)
class LoginUser(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=3)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr