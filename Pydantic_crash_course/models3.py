#import libraries
import uuid
from datetime import date, datetime, timedelta
from pydantic import BaseModel, confloat, field_validator, Field
from enums import DepartmentEnum
from typing import List, Literal #define literal type constraint

#class module to validate nested JSON data
class Module(BaseModel):
    id: int | uuid.UUID
    name: str
    professor: str
    credits: Literal[10, 20] #only 10 or 20 credits allowed
    registration_code: str

#basemodel
class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date = Field(default_factory=lambda: datetime.today().date()) #dynamic default value
    GPA: confloat(ge=0, le=4)
    course: str | None
    department: DepartmentEnum #enums.py custom data type
    fees_paid: bool
    modules: List[Module] = Field(default= [], max_items=10) #empty list if data is not present

#new validator function for modules list length
    @field_validator('modules')
    def validate_module_length(cls, value):
        if len(value) and len(value) != 3:
            raise ValueError('List of modules should have length of 3')
        return value


#define custom validator function for date of birth
    @field_validator('date_of_birth')
    def ensure_16_or_over(cls, value):
        sixteen_years_ago = datetime.now() - timedelta(days=365*16)
        sixteen_years_ago = sixteen_years_ago.date() #convert from datetime to date

        if value > sixteen_years_ago:
            raise ValueError('Student must be 16 or older')