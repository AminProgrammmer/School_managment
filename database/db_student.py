from database.dataschema import Students
from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm.session import Session
from schema import Student_Base

def get_student_all(db:Session) ->list:
    return db.query(Students).all()


def detail_student(id:int,db:Session):
    query = db.query(Students).where(
        Students.id==id
        ).first()
    if not query:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter id not found"
                            )
    return query

def add_student(data:Student_Base,db:Session) -> str:
    try:
        new_student = Students(
    name =data.name,
    last_name =data.last_name,
    national_code =data.national_code,
    number =data.number,
    class_id =data.class_id,
    major_id =data.major_id
        )
        if not new_student:
            raise HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail="not found data"
            )
        db.add(new_student)
        db.commit()
        db.refresh(new_student)
        return "your student added"
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"error :   {e}")


def delete_student(id:int,db:Session):
    student_item = db.query(Students).where(
        Students.id == id
        ).first()
    if student_item:
        db.delete(student_item)
        db.commit()
        return "your enter student is deleted"
    else :
        raise HTTPException(status_code=
                            status.HTTP_404_NOT_FOUND,detail=
                            "your enter student id not found")

def edit_student(id:int,data:Student_Base,db:Session):
    query = db.query(
        Students
        ).where(
            Students.id == id
            ).first().update(
        {
    "name":data.name,
    "last_name":data.last_name,
    "national_code":data.national_code,
    "number":data.number,
    "class_id":data.class_id,
    "major_id":data.major_id
    })
    if query:
        db.commit()
        return "your enter student edited"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter id wasnt found "
            )
    