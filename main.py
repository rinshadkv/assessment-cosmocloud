from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query
from models import Student,StudentDTO
from crud import create_student, list_students, get_student, update_student, delete_student

app = FastAPI()

@app.post("/api/students", status_code=201)
async def create_student_route(student: Student):
    return {"id": create_student(student)}

@app.get("/api/students", response_model=list[StudentDTO])
async def list_students_route(country: Optional[str] = Query(None), age: Optional[int] = Query(None)):
    return list_students(country, age)

@app.get("/api/students/{student_id}", response_model=Student)
async def get_student_route(student_id: str):
    student = get_student(student_id)
    if student:
        return student
    else:
        raise HTTPException(status_code=404, detail="Student not found")

@app.patch("/api/students/{student_id}", status_code=204)
async def update_student_route(student_id: str, student: Student):
    if update_student(student_id, student) == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        return

@app.delete("/api/students/{student_id}", status_code=200)
async def delete_student_route(student_id: str):
    if delete_student(student_id) == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        return