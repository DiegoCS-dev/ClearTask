from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from app.schemas.task import UpdateTask, Task, TaskResponse
from app.services.task import create_task, view_all_task, view_task_id, updateTask, delete_task,concluir_task
from app.utils.dependencies import get_current_user

task_routes = APIRouter(tags=["taks"])

@task_routes.post("/task")
async def create_task_route(body: Task, user_id: int = Depends(get_current_user)):
    create_task(body, user_id)
    return JSONResponse(status_code=201, content="Task criada com sucesso!")
@task_routes.get("/task", response_model=list[TaskResponse])
async def view_task_route(user_id: int = Depends(get_current_user)):
    return view_all_task(user_id)
@task_routes.get("/task/{id}", response_model=TaskResponse)
async def view_task_id_route(id, user_id: int = Depends(get_current_user)):
    dados = view_task_id(user_id, id)
    if dados is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return dados
@task_routes.put("/task/{id}")
async def update_task_route(id: int, body: UpdateTask, user_id: int =  Depends(get_current_user)):
    if updateTask(id, body, user_id) == 0:
        return JSONResponse(status_code=404, content="Tarefa não encontrada!")
    return {"message": "Tarefa atualizada com sucesso!"}
@task_routes.delete("/task/{id}")
async def delete_task_route(id: int, user_id: int = Depends(get_current_user)):
    if delete_task(id, user_id) == 0:
        return JSONResponse(status_code=404, content="Tarefa não encontrada!")
    return {"message": "Tarefa deletada com sucesso!"}
@task_routes.patch("/task/{id}/status")
async def concluir_task_route(id: int, user_id: int = Depends(get_current_user)):
    if concluir_task(id, user_id) == 0:
        return JSONResponse(status_code=404, content="Tarefa não encontrada!")
    return {"message": "Tarefa concluida com sucesso!"}