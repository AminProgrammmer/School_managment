from database.dataschema import Students

from fastapi.exceptions import HTTPException
from fastapi import status


def students(db):
    return db.query(Students).all()

def add_student(data,db):
    try:
        new_student = Students(

        )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return "your student added"
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"error :   {e}")
    