from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from database.dataschema import Admins

from password_hashing import Hash

def add_admin(db: Session, data):
    try:
        new_admin = Admins(
            name=data.name,
            last_name=data.last_name,
            natural_code=data.natural_code,
            number=data.number,
            email = data.email,
            password = Hash.bcrypt(data.password)
        )
        if not new_admin:
            raise HTTPException(detail="Admin details not found", status_code=status.HTTP_404_NOT_FOUND)
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
        return new_admin
    
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(detail="please call with support to site .An error occurred while adding the admin , maybe you enter an unique natural code or email or phone number.", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def detail_admin(id,db):
    return db.query(Admins).where(Admins.id == id).first()

def delete_admin(id,db):
    user = db.query(Admins).where(Admins.id == id).first()
    db.delete(user)
    db.commit()
    return "ok"