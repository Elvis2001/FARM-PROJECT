#Schema helps to serialize and also convert mongdb json to UI needed json

def studentEntity(mongodb_student_item) -> dict:
    return {
        "id": str(mongodb_student_item["_id"]),
        "name": mongodb_student_item["student_name"],
        "email": mongodb_student_item["student_email"],
        "phone": mongodb_student_item["student_phone"]
    }

def ListOfStudentsEntity(mongodb_student_items_list) -> list:
    list_of_students = []
    for student in mongodb_student_items_list:
        list_of_students.append(studentEntity(student))
    return list_of_students