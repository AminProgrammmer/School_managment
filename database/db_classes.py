from database.dataschema import Classes
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status
from schema import Class_Base

def add_class(data:Class_Base,db:Session) -> str|dict:
    try:
        new_class = Classes(
        name = data.name,
        major_id = data.major_id
        )
        db.add(new_class)
        db.commit()
        db.refresh(new_class)
        return "your class added"
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"error :   {e}")
    
def delete_class(id:int,db:Session) ->str|dict:
        class_item = db.query(Classes).where(
            Classes.id == id).first()
        if not class_item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND
                                ,
                            detail="your enter class id not found")

        db.delete(class_item)
        db.commit()
        return "your enter class is deleted"
        

def edit_class(id:int,data:Class_Base,db:Session) -> str|dict:
    class_item = db.query(Classes).where(
        Classes.id  == id).first().update(
        {
            "name" : data.name,
            "major_id" : data.major_id
        }
    )
    if not class_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="your enter class id not found")
    
    db.commit()
    return "your enter class is edited"
        
def get_all_class(db):
    return db.query(Classes).all()