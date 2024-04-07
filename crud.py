from bson import ObjectId
from typing import List, Optional
from models import Student, StudentDTO
from database import collection


def create_student(student: Student):
    student_data = student.model_dump()
    result = collection.insert_one(student_data)
    return str(result.inserted_id)


def list_students(country: Optional[str] = None, age: Optional[int] = None) -> List[StudentDTO]:
    query = {}
    if country:
        query['address.country'] = country
    if age:
        query['age'] = {'$gte': age}
    students = collection.find(query)
    return [StudentDTO(name=student['name'], age=student['age']) for student in students]


def get_student(student_id: str):
    if student_id is None:
        raise ValueError("Student ID cannot be None")
    student = collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return Student(**student)
    else:
        return None


def update_student(student_id: str, student: Student):
    if student_id is None:
        raise ValueError("Student ID cannot be None")
    student_data = student.model_dump()
    result = collection.update_one(
        {"_id": ObjectId(student_id)}, {"$set": student_data})
    return result.modified_count


def delete_student(student_id: str):
    if student_id is None:
        raise ValueError("Student ID cannot be None")
    result = collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count
