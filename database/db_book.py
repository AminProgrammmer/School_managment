from database.dataschema import Book

from fastapi.exceptions import HTTPException
from fastapi import status

def books(db):
    return db.query(Book).all()


def add_book(data,db):
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
    
def delete_book(id,db):
        book_item = db.query(Book).where(Book.id == id).first()
        if book_item:
            db.delete(book_item)
            db.commit()
            return "your enter book is deleted"
        else :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter book id not found")
        

def edit_book(id,data,db):
    book_item = db.query(Book).where(Book.id  == id).first().update(
        {
            "name" : data.name,
            "major_id" : data.major_id
        }
    )
    if book_item:
        db.commit()
        return "your enter book is edited"
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter book id not found")