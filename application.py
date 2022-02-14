from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from db_handler import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Library DBMS",
    description="Perform CRUD operation by using this API",
    version="1.0.0"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/retrieve_all_student_details', response_model=List[schema.Student])
def retrieve_all_student_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud.get_students(db=db, skip=skip, limit=limit)
    return students


@app.post('/add_new_student', response_model=schema.StudentAdd)
def add_new_student(STUDENT: schema.StudentAdd, db: Session = Depends(get_db)):
    stud_id = crud.get_student_by_student_id(db=db, STUD_ID=STUDENT.STUD_ID)
    if stud_id:
        raise HTTPException(status_code=400, detail=f"Student id {STUDENT.STUD_ID} already exist in database: {STUD_ID}")
    return crud.add_student_details_to_db(db=db, STUDENT=STUDENT)


@app.delete('/delete_student_by_student_id')
def delete_student_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_student_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_student_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_student_details', response_model=schema.Student)
def update_student_details(sl_id: int, update_param: schema.UpdateStudent, db: Session = Depends(get_db)):
    details = crud.get_student_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_student_details(db=db, details=update_param, sl_id=sl_id)
    
    
#########################################################################################################################################
    
@app.get('/retrieve_all_book_details', response_model=List[schema.Book])
def retrieve_all_book_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db=db, skip=skip, limit=limit)
    return books


@app.post('/add_new_book', response_model=schema.BookAdd)
def add_new_book(BOOK: schema.BookAdd, db: Session = Depends(get_db)):
    book_id = crud.get_book_by_book_id(db=db, BOOK_ID=BOOK.BOOK_ID)
    if book_id:
        raise HTTPException(status_code=400, detail=f"Book id {BOOK.BOOK_ID} already exist in database: {BOOK_ID}")
    return crud.add_book_details_to_db(db=db, BOOK=BOOK)


@app.delete('/delete_book_by_book_id')
def delete_book_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_book_by_book_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        crud.delete_book_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return {"delete status": "success"}


@app.put('/update_book_details', response_model=schema.Book)
def update_book_details(sl_id: int, update_param: schema.UpdateBook, db: Session = Depends(get_db)):
    details = crud.get_book_by_book_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to update")

    return crud.update_book_details(db=db, details=update_param, sl_id=sl_id)
    
    
########################################################################################################################################


    
    
    
    
    
    
    
