from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, ListOfStudentsEntity
from bson import ObjectId


student_router = APIRouter()


@student_router.get("/students")
async def find_all_students():
    return ListOfStudentsEntity(connection.local.students.find())



@student_router.get("/hello")
async def hello_world():
    return {"message": "Hello, World!"}


@student_router.post("/students")
async def create_student(student: Student):
   student_dict = student.dict()
   result = connection.local.students.insert_one(student_dict)
   return studentEntity(connection.local.students.find_one({"_id": result.inserted_id}))


'''@student_router.post("/students")
async def create_student(student: Student):
 connection.local.students.insert_one(dict(student))
   return ListOfStudentsEntity(connection.local.students.find())'''  


@student_router.put("/students/{student_id}")
async def update_student(student_id, student:Student):
    connection.local.students.find_one_and_update(
        {"_id" : ObjectId(student_id)},
        {"$set" : dict(student)}
    )
    return studentEntity(connection.local.students.find_one({"_id": ObjectId(student_id)}))


@student_router.delete("/students/{student_id}")
async def delete_student(student_id):
    return studentEntity(connection.local.students.find_one_and_delete({"_id": ObjectId(student_id)}))




@student_router.get("/students/{student_id}")
async def find_student_by_id(student_id):
    return studentEntity(connection.local.students.find_one({"_id": ObjectId(student_id)}))
