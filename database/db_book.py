from database.dataschema import Book
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from schema import book_Base

def get_all_book(db:Session) -> list:
    return db.query(Book).all()


def add_book(data:book_Base,db:Session) -> str|dict:
    try:
        new_book = Book(
        name = data.name,
        major_id = data.major_id
        )
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return "your book added"
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"error :   {e}")
    
def delete_book(id:int,db:Session) -> str | dict:
        book_item = db.query(Book).where(Book.id == id).first()
        if not book_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter book id not found")
        db.delete(book_item)
        db.commit()
        return "your enter book is deleted"

def edit_book(id:int,data:book_Base,db:Session) -> str|dict:
    book_item = db.query(Book).where(Book.id  == id).first().update(
        {
            "name" : data.name,
            "major_id" : data.major_id
        }
    )
    if not book_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter book id not found")
    db.commit()
    return "your enter book is edited"


