from fastapi import FastAPI
from database import engine, Base
from routers import courses, enrollments, grades, schedules, instructors

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CourseEnroll API", version="1.0")

app.include_router(courses.router)
app.include_router(enrollments.router)
app.include_router(grades.router)
app.include_router(schedules.router)
app.include_router(instructors.router)

