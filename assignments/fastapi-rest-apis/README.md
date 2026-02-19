# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Students will build a small RESTful API using the FastAPI framework. The API will expose endpoints to list, retrieve, and create simple "items" and include validation and auto-generated documentation.

## 📝 Tasks

### 🛠️ Basic API Endpoints

#### Description
Create a FastAPI application with the following endpoints:

- `GET /items` — return a list of items
- `GET /items/{item_id}` — return a single item by id
- `POST /items` — create a new item (accept JSON body)

#### Requirements
Completed program should:

- Use FastAPI to implement the endpoints
- Validate input using Pydantic models
- Store items in an in-memory list (no external DB required)
- Return appropriate HTTP status codes for success and errors


### 🛠️ Documentation and Testing

#### Description
Ensure the API is documented and testable via the OpenAPI docs provided by FastAPI. Add at least two example requests and show expected responses.

#### Requirements

- The API must expose interactive docs at `/docs` (FastAPI default)
- Provide example `curl` commands in this README for testing the endpoints


## 📎 Starter Code

This assignment includes starter code to get you started. Files included:

- `main.py` — minimal FastAPI app with in-memory storage
- `requirements.txt` — Python dependencies


## 📅 Due Date

Due: 2026-02-26


## 💡 Hints

- Use a Pydantic `BaseModel` for the item schema
- Keep persistence simple: a global list of dicts with incremental ids
- Run with `uvicorn main:app --reload` for local development


## ✅ Submission

Place your final `main.py` (or a ZIP) in the assignment folder and push to the repository. Ensure your README shows example requests and any notes.
