from sqlalchemy.orm import Session
import model
import schema

def get_student_by_student_id(db: Session, STUD_ID: int):
   return db.query(model.Student).filter(model.Student.STUD_ID == STUD_ID).first()


def get_student_by_id(db: Session, sl_id: int):
   return db.query(model.Student).filter(model.Student.STUD_ID == sl_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
   return db.query(model.Student).offset(skip).limit(limit).all()


def add_student_details_to_db(db: Session, Student: schema.StudentAdd):
    st_details = model.Student(
    	STUD_ID=STUDENT.STUD_ID,
    	STUD_NAME=STUDENT.STUD_NAME,
    	STUD_EMAIL=STUDENT.STUD_EMAIL,
    	STUD_DOB=STUDENT.STUD_DOB
        )
    db.add(st_details)
    db.commit()
    db.refresh(st_details)
    return model.Student(**STUDENT.dict())


def update_student_details(db: Session, sl_id: int, details: schema.UpdateStudent):
    db.query(model.Student).filter(model.Student.STUD_ID == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Student).filter(model.Student.STUD_ID == sl_id).first()
    
def delete_student_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Student).filter(model.Student.STUD_ID == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
    
###################################################################################################

def get_book_by_book_id(db: Session, BOOK_ID: int):
   return db.query(model.Book).filter(model.Book.BOOK_ID == BOOK_ID).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
   return db.query(model.Book).offset(skip).limit(limit).all()


def add_book_details_to_db(db: Session, Book: schema.BookAdd):
    bk_details = model.Book(
    	BOOK_ID=BOOK.BOOK_ID,
    	BOOK_TITLE=BOOK.BOOK_TITLE,
    	ISBN=BOOK.ISBN,
    	AUTHOR=BOOK.AUTHOR
        )
    db.add(bk_details)
    db.commit()
    db.refresh(bk_details)
    return model.Book(**BOOK.dict())


def update_book_details(db: Session, sl_id: int, details: schema.UpdateBook):
    db.query(model.Book).filter(model.Book.BOOK_ID == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Book).filter(model.Book.BOOK_ID == sl_id).first()


def delete_book_details_by_id(db: Session, sl_id: int):
    try:
        db.query(model.Book).filter(model.Book.BOOK_ID == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)
        
###################################################################################################















     

