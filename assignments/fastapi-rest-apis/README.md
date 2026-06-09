# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using the FastAPI framework to practice routing, request validation, and JSON responses.

## 📝 Tasks

### 🛠️ Create a Basic REST API

#### Description
Create a FastAPI application that manages simple "items" in memory. The API should provide endpoints to create, read, update, and delete items, and demonstrate use of Pydantic models for validation.

#### Requirements
Completed program should:

- Expose the following endpoints:
  - `GET /` — health/info endpoint
  - `GET /items/` — list all items
  - `GET /items/{id}` — retrieve an item by id
  - `POST /items/` — create a new item
  - `PUT /items/{id}` — update an existing item
  - `DELETE /items/{id}` — delete an item
- Use Pydantic models for request and response validation.
- Return appropriate HTTP status codes (e.g., `201` for created, `404` for not found).
- Validate input and handle errors gracefully with meaningful messages.
- Store items in-memory (a Python list/dict) — persistent storage is not required for this exercise.
- Include example requests demonstrating how to call the endpoints.

Example request/response (simplified):

```text
POST /items/
Request body: {"name": "Notebook", "price": 4.99}
Response: 201 Created
{ "id": 1, "name": "Notebook", "price": 4.99 }
```

Starter code: see `starter-code.py` in this folder.

How to run (local):

1. Install dependencies:

```bash
pip install fastapi uvicorn
```

2. Run the starter app:

```bash
python starter-code.py
```

3. Open the API docs at `http://127.0.0.1:8000/docs` to explore and test endpoints.
