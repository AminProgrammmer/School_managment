from pydantic import BaseModel,field_validator,EmailStr

class Admin_Base(BaseModel):
    name : str
    last_name : str
    natural_code : str
    number : str
    email : EmailStr
    password : str
    
    @field_validator("email")
    @classmethod
    def validate_email(cls, value):
        if value[-9:-4:] in ["gmail","yahoo"] and value[-4::] in [".net",".com"]:
            return value
        else:
            raise ValueError('email invalid')
    
    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value)<8:
            raise ValueError("password must be grater than 8")
        else:
            return value

class Admin_Detail(BaseModel):
    id:int
    name : str
    last_name : str
    natural_code : str
    number : str
    email : str
    is_manager:bool
