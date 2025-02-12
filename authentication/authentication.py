from fastapi import APIRouter,Depends,status
from sqlalchemy.orm.session import Session
from fastapi.exceptions import HTTPException
import password_hashing
# from db.db_user import User
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from auth import authenticate_user
from database.db import get_db

router = APIRouter(tags=['authentication'])

@router.post("/token")
def login_for_access_token(form_data : OAuth2PasswordRequestForm= Depends(),db:Session=Depends(get_db)):
    user = authenticate_user(db,form_data.username,form_data.password)