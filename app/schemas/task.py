from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskResponse(TaskCreate):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
