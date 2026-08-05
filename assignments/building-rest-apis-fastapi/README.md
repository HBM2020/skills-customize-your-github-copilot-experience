# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to practice route creation, request and response models, validation, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoint

#### Descrição
Set up a FastAPI application and implement a simple health-check route to confirm your API is running.

#### Requisitos
O programa concluído deve:

- Create a FastAPI app instance in `starter-code.py`.
- Implement a `GET /health` endpoint.
- Return a JSON response with the key `status` and value `"ok"`.
- Run locally using `uvicorn` and respond correctly in the browser or with `curl`.

### 🛠️ Implement CRUD for a Resource

#### Descrição
Create endpoints to manage a simple `books` resource using an in-memory list.

#### Requisitos
O programa concluído deve:

- Define a `BookCreate` model with `title`, `author`, and `year`.
- Define a `Book` model that includes an `id` field.
- Implement `POST /books` to add a new book.
- Implement `GET /books` to list all books.
- Implement `GET /books/{book_id}` to return a single book by ID.

### 🛠️ Add Update, Delete, and Error Handling

#### Descrição
Complete the API with update and delete operations and return proper HTTP errors when a book does not exist.

#### Requisitos
O programa concluído deve:

- Implement `PUT /books/{book_id}` to update an existing book.
- Implement `DELETE /books/{book_id}` to remove a book.
- Return HTTP 404 when a requested ID is not found.
- Validate that `year` is a positive integer.
- Test all endpoints using the automatic Swagger UI at `/docs`.
