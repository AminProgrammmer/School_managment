from database.dataschema import Majors
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from schema import major_Base
def get_all_major(db:Session) -> list:
    return db.query(Majors).all()

def add_major(data:major_Base,db:Session) -> str|dict:
    new_major = Majors(
        name = data.name
    )
    try:
        db.add(new_major)
        db.commit()
        db.refresh(new_major)
        return "new major added"
    except Exception as e:
        raise HTTPException(
    detail=f"you got the error call with mangers of the site : {e}",
    status_code=status.HTTP_400_BAD_REQUEST)        
    

def delete_major(id:int,db:Session) -> str|dict:
    major_item = db.query(Majors).where(Majors.id == id).first()
    if not major_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter major id not found")
    
    db.delete(major_item)
    db.commit()
    return "your enter class is deleted"


def edit_major(id:int,data:major_Base,db:Session) -> str|dict:
    major_item = db.query(Majors).where(
        Majors.id  == id).first().update(
        {
            "name" : data.name,
        }
    )
    if not major_item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter class id not found")
    db.commit()
    return "your enter class is edited"

        