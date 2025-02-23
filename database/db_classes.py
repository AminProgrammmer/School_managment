from database.dataschema import Classes

from fastapi.exceptions import HTTPException
from fastapi import status

def add_class(data,db):
    try:
        new_class = Classes(
        name = data.name,
        major_id = data.major_id
        )
        db.add(new_class)
        db.commit()
        db.refresh(new_class)
        return "your class added"
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"error :   {e}")
    
def delete_class(id,db):
        class_item = db.query(Classes).where(Classes.id == id).first()
        if class_item:
            db.delete(class_item)
            db.commit()
            return "your enter class is deleted"
        else :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter class id not found")
        

def edit_class(id,data,db):
    class_item = db.query(Classes).where(Classes.id  == id).first().update(
        {
            "name" : data.name,
            "major_id" : data.major_id
        }
    )
    if class_item:
        db.commit()
        return "your enter class is edited"
    else :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="your enter class id not found")
        
def classes(db):
    return db.query(Classes).all()