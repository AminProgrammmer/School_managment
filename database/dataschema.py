from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .db import base


class Students(base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(20))
    last_name = Column(String(20))
    national_code = Column(String(10), unique=True)
    number = Column(String(11), unique=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    major_id = Column(Integer, ForeignKey("majors.id"))
    clas = relationship("Classes", back_populates="students")
    major = relationship("Majors", back_populates="students")
    grade = relationship("Grade", back_populates="student")


class Majors(base):
    __tablename__ = "majors"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    students = relationship("Students", back_populates="major")
    classes = relationship("Classes", back_populates="major")
    books = relationship("Book", back_populates="major")
    admins = relationship("Admins", back_populates="major")


class Book(base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    major_id = Column(Integer, ForeignKey("majors.id"))
    major = relationship("Majors", back_populates="books")
    grades = relationship("Grade", back_populates="book")

class Grade(base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    gpa = Column(Integer)
    book_id = Column(Integer, ForeignKey("books.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    book = relationship("Book", back_populates="grades")
    student = relationship("Students", back_populates="grade")
 
class Admins(base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    last_name = Column(String(20))
    national_code = Column(String(10), unique=True)
    is_manager = Column(Boolean, default=False)
    number = Column(String(11), unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    major_id = Column(Integer, ForeignKey("majors.id"))
    major = relationship("Majors", back_populates="admins")

class Classes(base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    major_id = Column(Integer, ForeignKey("majors.id"))
    major = relationship("Majors", back_populates="classes")
    students = relationship("Students", back_populates="clas")