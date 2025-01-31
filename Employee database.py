from fastapi import FastAPI
from fastapi import Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

employees = {
    1:  {"name": "John", "age": 27, "email": "john@company.com", "password": "John#12"},
    2:  {"name": "Alice", "age": 30, "email": "alice@company.com", "password": "Alice#34"},
    3:  {"name": "Bob", "age": 25, "email": "bob@company.com", "password": "Bob#56"},
    4:  {"name": "Charlie", "age": 29, "email": "charlie@company.com", "password": "Charlie#78"},
    5:  {"name": "David", "age": 35, "email": "david@company.com", "password": "David#90"},
    6:  {"name": "Eve", "age": 28, "email": "eve@company.com", "password": "Eve#11"},
    7:  {"name": "Frank", "age": 33, "email": "frank@company.com", "password": "Frank#22"},
    8:  {"name": "Grace", "age": 26, "email": "grace@company.com", "password": "Grace#33"},
    9:  {"name": "Hank", "age": 31, "email": "hank@company.com", "password": "Hank#44"},
    10: {"name": "Ivy", "age": 24, "email": "ivy@company.com", "password": "Ivy#55"},
    11: {"name": "Jack", "age": 29, "email": "jack@company.com", "password": "Jack#66"},
    12: {"name": "Karen", "age": 32, "email": "karen@company.com", "password": "Karen#77"},
    13: {"name": "Leo", "age": 27, "email": "leo@company.com", "password": "Leo#88"},
    14: {"name": "Mona", "age": 30, "email": "mona@company.com", "password": "Mona#99"},
    15: {"name": "Nathan", "age": 34, "email": "nathan@company.com", "password": "Nathan#12"},
    16: {"name": "Olivia", "age": 26, "email": "olivia@company.com", "password": "Olivia#23"},
    17: {"name": "Paul", "age": 28, "email": "paul@company.com", "password": "Paul#34"},
    18: {"name": "Quinn", "age": 31, "email": "quinn@company.com", "password": "Quinn#45"},
    19: {"name": "Rachel", "age": 29, "email": "rachel@company.com", "password": "Rachel#56"},
    20: {"name": "Sam", "age": 25, "email": "sam@company.com", "password": "Sam#67"},
    21: {"name": "Tom", "age": 35, "email": "tom@company.com", "password": "Tom#78"},
    22: {"name": "Uma", "age": 27, "email": "uma@company.com", "password": "Uma#89"},
    23: {"name": "Victor", "age": 33, "email": "victor@company.com", "password": "Victor#90"},
    24: {"name": "Wendy", "age": 28, "email": "wendy@company.com", "password": "Wendy#11"},
    25: {"name": "Xander", "age": 30, "email": "xander@company.com", "password": "Xander#22"},
    26: {"name": "Yara", "age": 29, "email": "yara@company.com", "password": "Yara#33"},
    27: {"name": "Zane", "age": 31, "email": "zane@company.com", "password": "Zane#44"},
    28: {"name": "Abby", "age": 32, "email": "abby@company.com", "password": "Abby#55"},
    29: {"name": "Ben", "age": 26, "email": "ben@company.com", "password": "Ben#66"},
    30: {"name": "Clara", "age": 27, "email": "clara@company.com", "password": "Clara#77"},
}

class Employee(BaseModel):
    name: str
    age: int
    email: str
    password: str

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None


@app.post("/create-employee/{employee_id}")
def create_employee(employee_id: int, employee: Employee):
    if employee_id in employees:
        return {"Error": "Employee Exists"}
    
    employees[employee_id]= employee.model_dump()
    return employees[employee_id]


@app.get("/get-employee/{employee_id}")
def get_employee(employee_id: int= Path(..., Description= "Input the id of the employee you want to view")):
    if employee_id not in employees:
        return {"Error": "Employee Doesn't Exists"}

    employee_data = employees[employee_id].copy()
    employee_data.pop("password")  
    return employee_data

@app.put("/update-employee/{employee_id}")
def update_employee(employee_id: int, updated_employee: EmployeeUpdate):
    if employee_id not in employees:
        return {"Error": "Employee Doesn't Exists"}
    
    if updated_employee.name is not None:
        employees[employee_id]["name"] = updated_employee.name 
    
    if updated_employee.age is not None:
        employees[employee_id]["age"] = updated_employee.age
    
    if updated_employee.email is not None:
        employees[employee_id]["email"] = updated_employee.email

    if updated_employee.password is not None:
        employees[employee_id]["password"] = updated_employee.password

 

    return update_employee

@app.delete("/delete-employee/{employee_id}")
def delete_employee(employee_id: int):
    if employee_id not in employees:
        return {"Error": "Employee Doesn't Exists"}

    del employees[employee_id]
    return employee_id
    
