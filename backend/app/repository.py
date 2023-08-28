import databases
from pydantic import BaseModel

database = databases.Database("sqlite:///./test.db")


class BookRepository:
    def __init__(self):
        self.books = "books"  # Table name

    async def get_all_books(self):
        query = f"SELECT * FROM {self.books}"
        return await database.fetch_all(query)

    async def create_book(self, title: str):
        query = f"INSERT INTO {self.books} (title, state) VALUES (:title, 'to-read')"
        return await database.execute(query=query, values={"title": title})

    async def update_book_state(self, book_id: int, state: str):
        query = f"UPDATE {self.books} SET state=:state WHERE id=:book_id"
        return await database.execute(query=query, values={"book_id": book_id, "state": state})

    async def delete_book(self, book_id: int):
        query = f"DELETE FROM {self.books} WHERE id=:book_id"
        return await database.execute(query=query, values={"book_id": book_id})
