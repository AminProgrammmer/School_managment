from authentication.authentication import RoleCheck

from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from database.db import get_db
from database import db_student
from schema import Student_Base
from authentication.authentication import RoleCheck
router = APIRouter(prefix="/Students",tags=["student"])


@router.get("/{id}")
def student_detail(id:int,db:Session=Depends(get_db)):
    return db_student.detail_student(id,db)

@router.get("")
def students(db:Session=Depends(get_db)):
    return db_student.get_student_all(db=db)

@router.post("/create")
def add_student(data_student:Student_Base ,db:Session=Depends(get_db),role = Depends(RoleCheck(True))):
    return db_student.add_student(data=data_student,db=db)


@router.delete("/delete{id}")
def remove_student(id:int,db:Session=Depends(get_db)
                   ,role = Depends(RoleCheck(True))):
    return db_student.delete_student(id=id,db=db)


@router.put("/edit{id}")
def edit_student(id:int,data:Student_Base,db:Session=Depends(get_db),role = Depends(RoleCheck(True))):
    return db_student.edit_student(id,data,db)