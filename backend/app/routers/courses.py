from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Course
from schemas import CourseCreate, CourseRead
from typing import List

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/", response_model=CourseRead)
def add_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/", response_model=List[CourseRead])
def list_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

