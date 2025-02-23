from database.dataschema import Majors

from fastapi.exceptions import HTTPException
from fastapi import status
def majors(db):
    return db.query(Majors).all()

def add_major(data,db):
    new_major = Majors(
        name = data.name
    )
    try:
        db.add(new_major)
        db.commit()
        db.refresh(new_major)
        return "new major added"
    except Exception as e:
        raise HTTPException(detail=f"you got the error call with mangers of the site : {e}",status_code=status.HTTP_400_BAD_REQUEST)        
    

def delete_major(id,db):
    major_item = db.query(Majors).where(Majors.id == id).first()
    if major_item:
        db.delete(major_item)
        db.commit()
        return "your enter class is deleted"
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter class id not found")


def edit_major(id,data,db):
    major_item = db.query(Majors).where(Majors.id  == id).first().update(
        {
            "name" : data.name,
        }
    )
    if major_item:
        db.commit()
        return "your enter class is edited"
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter class id not found")
        