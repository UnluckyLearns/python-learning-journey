#  /  @  > < [] {} |
from fastapi import APIRouter
from task_models import Task,TaskUpdate
from task_manager import TaskManager
from fastapi import HTTPException

router = APIRouter()
task_mana  = TaskManager()

@router.get('/tasks')
def main_page(search: str | None=None ,completed :bool | None=None):
    task_mana.fetch(search,completed)
    return task_mana.task_list

@router.post('/newtask')
def create_task(task : Task):
   dict_one = task_mana.insert(task)
   return dict_one

@router.get('/tasks/{task_id}')
def second_page(task_id : int):
    dict_one = task_mana.fetch_one(task_id)
    return dict_one


@router.put('/tasks/{task_id}')
def update_task(task_id : int,taskup: TaskUpdate):
    dict_one = task_mana.update(taskup,task_id)
    return dict_one

@router.delete('/tasks/{task_id}')
def delete_task(task_id : int):
    deleted = task_mana.delete(task_id)
    if not deleted : 
        raise HTTPException(status_code = 404, detail = "Task Not Found")
    return {"message": "Task deleted"}
