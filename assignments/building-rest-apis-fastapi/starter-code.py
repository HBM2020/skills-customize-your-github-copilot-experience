from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


class Book(BookCreate):
    id: int


books: list[Book] = []
next_id = 1


@app.get("/health")
def health_check():
    # Task 1: return a JSON response with status "ok"
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # Task 2: return all books
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # Task 2: return a single book by id or 404
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate):
    # Task 2: create and store a new book with an incremental id
    global next_id
    book = Book(id=next_id, **payload.model_dump())
    books.append(book)
    next_id += 1
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, payload: BookCreate):
    # Task 3: update a book by id or return 404
    for idx, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **payload.model_dump())
            books[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    # Task 3: remove a book by id or return 404
    for idx, book in enumerate(books):
        if book.id == book_id:
            del books[idx]
            return None
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
