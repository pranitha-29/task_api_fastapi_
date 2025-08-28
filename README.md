Task Management REST API (FastAPI + SQLite)

This repository contains a Task Management REST API built with FastAPI, developed as part of my internship assignment.
It includes CRUD operations, validation, error handling, database integration, auto Swagger/OpenAPI docs, and optional JWT authentication.
A Dockerfile and Postman collection are included for easy deployment and testing.

Features

FastAPI with auto docs at /docs and OpenAPI JSON at /openapi.json

SQLite via SQLAlchemy (easily switch to PostgreSQL/MySQL)

CRUD for tasks: create, list, get-by-id, update, delete

Filtering & search: GET /tasks?completed=true&q=term

Input validation with Pydantic

Graceful error handling (404 for missing items, 422 for bad input)

Optional JWT auth: register & login; protect write endpoints if enabled

Dockerfile for containerized deployment

Postman collection included

Quickstart (Local)
1) Create venv & install dependencies
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

pip install -r requirements.txt

2) Run the API
uvicorn app.main:app --reload


Open: http://127.0.0.1:8000/docs

Environment Variables (Optional)

Create a .env file (or set env vars) to customize:

DATABASE_URL=sqlite:///./app.db
JWT_SECRET=change-this-secret
JWT_ALG=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
ENABLE_AUTH=true


If ENABLE_AUTH=true, write endpoints require Authorization: Bearer <token> header.

If false or unset, endpoints are open.

A default .env.example is provided.

Endpoints (Core)

POST /tasks – create task

GET /tasks – list tasks (filters: completed, q)

GET /tasks/{task_id} – get one

PUT /tasks/{task_id} – update

DELETE /tasks/{task_id} – delete

Auth (Optional)

POST /auth/register – create user

POST /auth/login – get JWT access token

Switching to PostgreSQL/MySQL

Set DATABASE_URL like:

Postgres: DATABASE_URL=postgresql+psycopg2://user:pass@host:5432/dbname

MySQL: DATABASE_URL=mysql+pymysql://user:pass@host:3306/dbname

Install the appropriate driver (see requirements.txt hints).

Docker
docker build -t task-api .
docker run -p 8000:8000 --env-file .env task-api

Project Structure
app/
  core/         # config, security (JWT), app settings
  db/           # database base, session, init
  models/       # SQLAlchemy models (Task, User)
  routers/      # route handlers (tasks, auth)
  schemas/      # Pydantic schemas (request/response)
  utils/        # helper functions, common utilities
  main.py       # application entry point
requirements.txt
Dockerfile
postman_collection.json
.env.example
README.md
