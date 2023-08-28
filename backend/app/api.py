from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.repository import BookRepository

router = APIRouter()

class BookCreate(BaseModel):
    title: str

class BookUpdate(BaseModel):
    state: str

class BookResponse(BookCreate):
    id: int
    state: str

repository = BookRepository()  # Assuming you have a BookRepository class

@router.get("/books", response_model=List[BookResponse])
async def get_books():
    return await repository.get_all_books()

@router.post("/books", response_model=BookResponse)
async def create_book(book: BookCreate):
    return await repository.create_book(book.title)

@router.put("/books/{book_id}", response_model=BookResponse)
async def update_book_state(book_id: int, book_update: BookUpdate):
    return await repository.update_book_state(book_id, book_update.state)

@router.delete("/books/{book_id}")
async def delete_book(book_id: int):
    await repository.delete_book(book_id)
    return {"message": "Book deleted"}
