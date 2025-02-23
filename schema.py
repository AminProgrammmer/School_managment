from pydantic import BaseModel,field_validator,EmailStr
import re

class major_Base(BaseModel):
    name:str

class Admin_Base(BaseModel):
    name : str
    last_name : str
    natural_code : str
    number : str
    email : EmailStr
    password : str
    major_id : int
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if value[-9:-4:] in ["gmail","yahoo"] and value[-4::] in [".net",".com"]:
            return value
        else:
            raise ValueError('email invalid')
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search("[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search("[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search("[0-9]", v):
            raise ValueError("Password must contain at least one digit")
        if not re.search("[@#$%^&+=]", v):
            raise ValueError("Password must contain at least one special character (@#$%^&+=)")
        return v
    
class Admin_Detail(BaseModel):
    id:int
    name : str
    last_name : str
    natural_code : str
    number : str
    email : str
    is_manager:bool
    major_id : int


class Class_Base(BaseModel):
    name :str
    major_id :int

