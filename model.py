from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db_handler import Base
#import datetime

class Student(Base):
    
    __tablename__ = "STUDENT"
    STUD_ID = Column(Integer, primary_key=True, index=True, nullable=False)
    STUD_NAME = Column(String(30), unique=True, index=True, nullable=False)
    STUD_EMAIL = Column(String(30), index=True, nullable=False)
    STUD_DOB = Column(DateTime, index=True, nullable=False)
       
    student = relationship("Record", back_populates="record")
     
class Book(Base): 

    __tablename__ = "BOOK"
    BOOK_ID = Column(Integer, primary_key=True, index=True, nullable=False)
    BOOK_TITLE = Column(String(30), unique=True, index=True, nullable=False)
    ISBN = Column(String(30), index=True, nullable=False)
    AUTHOR = Column(String(30), index=True, nullable=False)
    
    book = relationship("Record", back_populates="owner")
    
class Record(Base):

    __tablename__ = "STUD_RECORD"
    REC_NO = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    STUD_ID = Column(Integer, ForeignKey("STUDENT.STUD_ID"))
    BOOK_ID = Column(Integer, ForeignKey("BOOK.BOOK_ID"))
    DATE_ISSUED = Column(DateTime, index=True, nullable=False)
    DATE_RECEIVED = Column(DateTime, index=True, nullable=False)
    
    record = relationship("Student", back_populates="student")
    owner = relationship("Book", back_populates="book")
    
