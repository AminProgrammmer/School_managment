from database.dataschema import Grade,Students,Book
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi.exceptions import HTTPException
from fastapi import status
from schema import Grade_base

def add_gpa_student(data:Grade_base,db:Session) -> str|dict:
    book_id = db.query(Book).where(Book.id == data.book_id).first()
    Student_id = db.query(Students).where(Students.id==data.student_id).first()
    if not book_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter book id not found")
    elif not Student_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter student id not found")
    else:
        grade_item = Grade(
            gpa = data.gpa,
            book_id = data.book_id,
            student_id = data.student_id)
        db.add(grade_item)
        db.commit()
        db.refresh(grade_item)
        return "you entered a gpa"

        
def edit_grade(id:int,data:Grade_base,db:Session) -> str|dict:
    book_id = db.query(Book).where(Book.id == data.book_id).first()
    Student_id = db.query(Students).where(Students.id==data.student_id).first()
    if not book_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter book id not found")
    elif not Student_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="your enter student id not found")
    else:
        major_item = db.query(Grade).where(
        Grade.id  == id).update(
        {
            "gpa" : data.gpa,
            "book_id" : data.book_id,
            "student_id":data.student_id
        }
        )
        if not major_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="your enter class id not found")
        db.commit()
        return "your enter grade is edited"

        
def delete_grade(id:int,db:Session) -> str|dict:
    grade_item = db.query(Grade).where(Grade.id == id).first()
    if not grade_item:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="your enter grade id not found")
    
    db.delete(grade_item)
    db.commit()
    return "your enter class is deleted"

def gpa_student(id:int,db:Session) -> dict:
    item_grade = db.query(func.sum(Grade.gpa) /func.count(Grade.gpa)).where(Grade.student_id==id).scalar()
    if not item_grade:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="not found grade for entered student id")
    grade = db.query(Grade).where(Grade.student_id == id).all()
    return {"gpa":item_grade,"books":grade}