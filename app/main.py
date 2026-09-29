from fastapi import FastAPI
import uvicorn

from app.routers.auth import user_routes
from app.routers.tasks import task_routes
from app.routes_html.routes_html import routes
from fastapi.staticfiles import StaticFiles
# Executa a criação das tabelas
from app.models import user
from app.models import task

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
# API
app.include_router(user_routes)
app.include_router(task_routes)

# Páginas HTML
app.include_router(routes)

if __name__ == "__main__":
    uvicorn.run("app.main:app", reload=True)