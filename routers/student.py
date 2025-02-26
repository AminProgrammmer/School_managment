from authentication.authentication import RoleCheck

from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from database.db import get_db
from database import db_student
from schema import Student_Base
from authentication.authentication import RoleCheck
router = APIRouter(prefix="/Students",tags=["student"])


@router.get("")
def students(db:Session=Depends(get_db)):
    return db_student.students(db=db)

@router.post("/create")
def add_student(data_student:Student_Base ,db:Session=Depends(get_db),role = Depends(RoleCheck(True))):
    return db_student.add_student(data=data_student,db=db)

@router.delete("/delete{id}")
def remove_major(id:int,db:Session=Depends(get_db),role = Depends(RoleCheck(True))):
    return db_student.delete_major(id=id,db=db)

@router.put("/edit{id}")
def edit_major(id:int,data:Student_Base,db:Session=Depends(get_db),role = Depends(RoleCheck(True))):
    return db_student.edit_major(id,data,db)