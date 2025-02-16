from database.dataschema import Classes

from fastapi.exceptions import HTTPException
from fastapi import status

def add_class(data,db):
    try:
        new_class = Classes(
        name = data.name,
        admins_id = data.admins_id,
        major_id = data.major_id
        )
        db.add(new_class)
        db.commit()
        db.refresh(new_class)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"error :   {e}")