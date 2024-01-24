import libraries
import requests
import uuid
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, field_validator
from typing import Union
#import enums
from enums import DepartmentEnum
#import student class
from models import Student, Module

call to JSON data from github
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'


request data from github
response = requests.get(url)
data = response.json()

get last record
del data [-1]['date_of_birth']

append new record to JSON data to test error using confloat
data.append( {
        "id": "d15782d9-3d8f-4624-a88b-c8e836569df8",
        "name": "Eric Travis",
        "date_of_birth": "1995-05-25",
        "GPA": "5.0", #change to 5.0 to test error using confloat
        "course": "Computer Science",
        "department": "Science and Engineering",
        "fees_paid": False
    },)

append another record to test error using validator
data.append(
    {
        "id": "48dda775-785d-41e3-b0dd-26a4a2f7722f",
        "name": "Justin Holden",
        "date_of_birth": "1994-08-22",
        "GPA": "3.23",
        "course": "Philosophy",
        "department": "Arts and Humanities",
        "fees_paid": True
    })



#Pydantic class for data modeling
class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4) #confloat is a constrained float
    course: str | None #Union of data types[str, None] Can also use Optional
    department: DepartmentEnum #Use DepartmentEnum instead of str
    fees_paid: bool


#define validator function for date of birth
    @field_validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)
        sixteen_years_ago = sixteen_years_ago.date() #convert from datetime to date

        if value > sixteen_years_ago:
            raise ValueError("Student must be 16 years or older, sorry!")
        return value


create list of key, values from JSON data
for student in data:
    model = Student(**student)
    export to dictionary
    print(model.dict())

    export to JSON
    print(model.date_of_birth)


