from sqlalchemy import Column,Integer,String,ForeignKey,Boolean
from sqlalchemy.orm.relationships import Relationship
from .db import base


class Majors(base):
    __tablename__ = "Majors"
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    Student = Relationship("Students",back_populates="major")
    clas = Relationship("Classes",back_populates="major")
    
class Admins(base):
    __tablename__ = "Admins"
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    last_name = Column(String(20))
    natural_code = Column(String(10),unique=True)
    is_manager = Column(Boolean,default=False)
    number = Column(String(11),unique=True)
    email = Column(String,unique=True)
    password = Column(String)
    clas = Relationship("Classes",back_populates="admin")

class Classes(base):
    __tablename__ = "Classes"
    
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    admins_id = Column(Integer,ForeignKey("Admins.id"))
    major_id = Column(Integer,ForeignKey("Majors.id"))
    major = Relationship("Majors",back_populates="clas")
    admin = Relationship("Admins",back_populates="clas")
    Student = Relationship("Students",back_populates="clas")

class Students(base):
    __tablename__ = "Students"
    id = Column(Integer,primary_key=True,unique=True)
    name = Column(String(20))
    last_name = Column(String(20))
    natural_code = Column(String(10),unique=True)
    number = Column(String(11),unique=True)
    class_id = Column(Integer,ForeignKey("Classes.id"))
    major_id = Column(Integer,ForeignKey("Majors.id"))
    
    clas = Relationship("Classes",back_populates="Student")
    
    major = Relationship("Majors",back_populates="Student")
