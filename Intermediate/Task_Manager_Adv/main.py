from fastapi import  FastAPI
from database import Database
from task_routes import router

#  /  @  > < [] {}


api = FastAPI()
api.include_router(router)
