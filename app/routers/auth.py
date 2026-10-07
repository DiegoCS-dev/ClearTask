from fastapi import APIRouter, Depends, Form, Request, responses, UploadFile, File
from fastapi.responses import RedirectResponse  
from fastapi.templating import Jinja2Templates
from app.schemas.user import CreateUser, LoginUser, UserResponse
from app.services import auth
from app.utils.dependencies import get_current_user

templates = Jinja2Templates(directory="app/templates")

user_routes = APIRouter(tags=["usuarios"])


@user_routes.post("/create_user")
async def create_user( request: Request,
                    name: str = Form(...),
                      email: str = Form(...),
                      password: str = Form(...),
                      confirm_password: str = Form(...)):
    if password != confirm_password:
            return templates.TemplateResponse(
            request=request,
            name="register.html",
            context={
                "request": request,
                "error": "As senhas não coincidem!",
                "name": name,
                "email": email
            },
            status_code=400
        )
    body = CreateUser(name=name, email=email, password=password)

    if auth.create_User(body):
        return RedirectResponse(url="/login", status_code=303)
    return templates.TemplateResponse(request=Request, name="register.html", context={"request": request, 
                                                                                      "error": "Erro ao criar usuário. Email indisponivel."}, status_code=409)

@user_routes.post("/login")
async def login(email: str = Form(...), 
            password: str = Form(...)
):
    body = LoginUser(email=email, 
                     password=password)
    access_token = auth.login(body)

    if not access_token:
        return RedirectResponse(url="/login?error=1", status_code=303)
    response = RedirectResponse(url="/dashboard", status_code=303)
    response.set_cookie(key="access_token", 
                        value=access_token, 
                        httponly=True, 
                        samesite="lax", 
                        secure=False,
                        path="/")
    print("token:", access_token)
    print("SET-COOKIE:", response.headers.get("set-cookie"))
    return response

@user_routes.get("/me", response_model=UserResponse)
async def me(user_id: int = Depends(get_current_user)):
    return auth.me(user_id)