from django.shortcuts import render
from django.http import HttpResponse

fetched_students = [
    {"id": 1, "name": "Salma", "age": 23, "department": "Software Engineering"},
    {"id": 2, "name": "Shereen", "age": 23, "department": "Software Engineering"},
    {"id": 3, "name": "Sarah", "age": 21, "department": "Biomedical Engineering"},
    {"id": 4, "name": "Hamza", "age": 20, "department": "Aerospace Engineering"},
    {"id": 5, "name": "Youssef", "age": 22,"department": "Artificial Intelligence"}

]
context = {
    "Students_data": fetched_students
}

# Create your views here.


def get_all_students(req):
    return render(req, "Student/index.html", context)


def get_single_student(req, id):
    print(fetched_students[id - 1])
    context = {"Student_data": fetched_students[id - 1]}
    return render(req, "Student/Student.html", context)
