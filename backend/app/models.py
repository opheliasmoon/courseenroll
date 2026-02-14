from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String)  # admin, student, instructor
    student = relationship("Student", back_populates="user", uselist=False)
    instructor = relationship("Instructor", back_populates="user", uselist=False)

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    email = Column(String)
    user = relationship("User", back_populates="student")
    enrollments = relationship("Enrollment", back_populates="student")
    grades = relationship("Grade", back_populates="student")

class Instructor(Base):
    __tablename__ = "instructors"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String)
    email = Column(String)
    user = relationship("User", back_populates="instructor")
    grades = relationship("Grade", back_populates="instructor")
    schedules = relationship("Schedule", back_populates="instructor")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    credits = Column(Integer)
    department = Column(String)
    schedules = relationship("Schedule", back_populates="course")
    grades = relationship("Grade", back_populates="course")
    enrollments = relationship("Enrollment", back_populates="course")
    instructor_assignments = relationship("InstructorAssignment", back_populates="course")

class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    enrollment_date = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String, default="enrolled")
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")

class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    grade = Column(String)
    student = relationship("Student", back_populates="grades")
    course = relationship("Course", back_populates="grades")
    instructor = relationship("Instructor", back_populates="grades")

class Schedule(Base):
    __tablename__ = "schedules"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    room = Column(String)
    time = Column(String)
    course = relationship("Course", back_populates="schedules")
    instructor = relationship("Instructor", back_populates="schedules")

class InstructorAssignment(Base):
    __tablename__ = "instructor_assignments"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    instructor_id = Column(Integer, ForeignKey("instructors.id"))
    course = relationship("Course", back_populates="instructor_assignments")
    instructor = relationship("Instructor")

