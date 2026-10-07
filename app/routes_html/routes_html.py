from fastapi import APIRouter, Request, Depends, Query
from pathlib import Path
from fastapi.templating import Jinja2Templates
from app.routers import auth
from app.services import task
from app.utils.dependencies import get_current_user

BASE_DIR = Path(__file__).resolve().parent.parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

routes = APIRouter()


@routes.get("/login")
async def login_page(request: Request,
                     error: int = Query(0)):
    error_message = None
    if error == 1:
        error_message = "Email ou senha incorretos."
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"error": error_message, "request": request}
    )

@routes.get("/dashboard")
async def dashboard_page(
    request: Request,
    user_id: int = Depends(get_current_user)
):                  
    user = await auth.me(user_id)
    tasks = await task.view_all_task(user_id)
    stats = {
        "total_tasks": len(tasks),
        "pending_tasks": len([task for task in tasks if task["status"] == "pending"]),
        "completed_tasks": len([task for task in tasks if task["status"] == "completed"]),
        "high_priority_tasks": len([task for task in tasks if task["priority"] == "high"])
    }

    return templates.TemplateResponse(request=request,
                                      name="dashboard.html",
                                      context={"request": request,
                                          "user": user,
                                          "tasks": tasks,
                                          "stats": stats})

@routes.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html",
        context={"request": request}
    )