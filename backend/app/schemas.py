from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    name: str
    credits: int
    department: str

class CourseCreate(CourseBase): pass
class CourseRead(CourseBase):
    id: int
    class Config:
        orm_mode = True

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int

class EnrollmentCreate(EnrollmentBase): pass
class EnrollmentRead(EnrollmentBase):
    id: int
    status: str
    class Config:
        orm_mode = True

class GradeBase(BaseModel):
    student_id: int
    course_id: int
    instructor_id: int
    grade: str

class GradeCreate(GradeBase): pass
class GradeRead(GradeBase):
    id: int
    class Config:
        orm_mode = True

class ScheduleBase(BaseModel):
    course_id: int
    instructor_id: int
    room: str
    time: str

class ScheduleCreate(ScheduleBase): pass
class ScheduleRead(ScheduleBase):
    id: int
    class Config:
        orm_mode = True

class InstructorAssignmentBase(BaseModel):
    course_id: int
    instructor_id: int

class InstructorAssignmentCreate(InstructorAssignmentBase): pass
class InstructorAssignmentRead(InstructorAssignmentBase):
    id: int
    class Config:
        orm_mode = True

