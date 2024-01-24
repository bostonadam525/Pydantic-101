#import basemodel
from pydantic import BaseModel, ValidationError, Field
from typing import List
from enum import Enum
import json

# class Gender
class Gender(str, Enum):
    MALE="Male"
    FEMALE="Female"
    NON_BINARY="Non binary"

# define a class that inherits from BaseModel
# define pydantic data types within class
class Person(BaseModel):
    username: str=Field(default=None, max_length=8, min_length=2) #field used to add specific validation
    email: str=Field(default=None, max_length=8, min_length=2)
    age: int=Field(lt=60,gt=18) #less than, greater than
    friends: List[str]=[]
    gender: Gender #inherits from Gender class


#create a data dictionary
data = {
    "username": "john",    #"usernameistombrady", #validates error
    "email": "testuser@gmail.com",
    "age": 19,
    "friends": ["john"],
    "gender": Gender.MALE
}

# create an instance of the class
# validate error
try:

    new_person = Person(**data) # unpack dictionary


    schema = new_person.schema()

    print(json.dumps(schema, indent=4))


    #print(new_person.json()) #returns json data
    #print(new_person.dict()) #returns dictionary data
    print(new_person.schema()) #returns schema data

except ValidationError as e:
    print(e.json()) #returns json error message