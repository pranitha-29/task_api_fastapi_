from fastapi import FastAPI
from app.db import database
from app.routers import users, tasks

# Create DB tables
database.Base.metadata.create_all(bind=database.engine)

# FastAPI app
app = FastAPI(title="Task Management API", version="1.0.0")

# Include routers
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Management API with Authentication 🚀"}
