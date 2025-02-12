from fastapi import APIRouter,Depends

from sqlalchemy.orm.session import Session

from database.db import get_db
from database import db_admins
from schema import Admin_Base,Admin_Detail

router = APIRouter(prefix="/admin",tags=["admin"])

@router.post("/create")
def add_admin(data_user:Admin_Base ,db:Session=Depends(get_db)):
    return db_admins.add_admin(data=data_user,db=db)

@router.get("/detail{id}")
def detail_by_id(id:int,db:Session=Depends(get_db)):
    return db_admins.detail_admin(id=id,db=db)

@router.delete("/delete{id}")
def remove_admin(id:int,db:Session=Depends(get_db)):
    return db_admins.delete_admin(id=id,db=db)