from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from database.db import get_db
from database import db_classes
from schema import Class_Base

from authentication.authentication import RoleCheck
router = APIRouter(prefix="/class",tags=["class"])

@router.post("/create")
def add_class(data_class:Class_Base ,db:Session=Depends(get_db)):
    return db_classes.add_class(data=data_class,db=db)

# @router.get("/detail{id}")
# def detail_by_id(id:int,db:Session=Depends(get_db),role=Depends(RoleCheck(True))):
#     return db_admins.detail_admin(id=id,db=db)

# @router.delete("/delete{id}")
# def remove_admin(id:int,db:Session=Depends(get_db)):
#     return db_admins.delete_admin(id=id,db=db)