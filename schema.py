from typing import Optional
from pydantic import BaseModel
#import datetime

class StudentBase(BaseModel):
    STUD_ID: int
    STUD_NAME: str
    STUD_EMAIL: str
    #STUD_DOB: datetime


class StudentAdd(StudentBase):
    STUD_NAME: str
    STUD_EMAIL: str
    #STUD_DOB: datetime
   
    class Config:
        orm_mode = True


class Student(StudentAdd):
    STUD_ID: int

    class Config:
        orm_mode = True


class UpdateStudent(BaseModel):
   class Config:
        orm_mode = True
        
###########################################################################################

class BookBase(BaseModel):
    BOOK_ID: int
    BOOK_NAME: str
    ISBN: str
    AUTHOR: str


class BookAdd(BookBase):
    BOOK_ID: int
    BOOK_NAME: str
    ISBN: str
    AUTHOR: str
   
    class Config:
        orm_mode = True


class Book(BookAdd):
    BOOK_ID: int

    class Config:
        orm_mode = True


class UpdateBook(BaseModel):
   class Config:
        orm_mode = True
        

