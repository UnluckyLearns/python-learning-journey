from pydantic import BaseModel, ValidationError,Field


class Task(BaseModel):
    title: str = Field(min_length = 1,max_length = 25)
    description : str | None = Field(None,max_length = 100)
    completed : bool = False

class TaskUpdate(BaseModel):
    title : str | None = Field(None,min_length = 1,max_length = 22)
    description : str | None = Field(None,max_length = 100)
    completed : bool | None = None
    