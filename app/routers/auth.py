from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.schemas.user import CreateUser, LoginUser, UserResponse
from app.services import auth
from app.utils.dependencies import get_current_user


user_routes = APIRouter(tags=["usuarios"])

@user_routes.post("/create_user")
async def create_user(body: CreateUser):
    print(body)
    if auth.create_User(body):
        return JSONResponse(status_code=201,
        content="Usuario criado com sucesso!")
    return JSONResponse(status_code=409, content="Email ja cadastrado!")

@user_routes.post("/login")
async def login(body:LoginUser):
    access_token = auth.login(body)
    if access_token:
        return JSONResponse(status_code=200, content={
                            "message": "Logado com sucesso!",
                            "access_token": access_token,
                            "token_type": "bearer"
                            })
    return JSONResponse(status_code=401, content="Senha incorreta ou email incorreto!")
@user_routes.get("/me", response_model=UserResponse)
async def me(user_id: int = Depends(get_current_user)):
    return auth.me(user_id)