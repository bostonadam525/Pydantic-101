#import libraries
import requests
from models import Student, Module

#call to JSON data from github
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

#response
response = requests.get(url)
data = response.json()

# #test additional record
# data[-1]['modules'].append(
#     {
#                 "id": 101,
#                 "name": "Japanese Cinema",
#                 "professor": "Prof. Travis Hudson",
#                 "credits": 20, #change to 24 to test error using Literal
#                 "registration_code": "abc"
#             }
# )


# # #iterate through data
#for student in data:
    #model = Student(**student)
    #print(model)
    #break #break after first iteration

# #change iteration
# for student in data:
#     model=Student(**student)
#     for module in model.modules:
#         print(module.id)


#print JSON schema
# annotate and declare JSON schema for Module class
#print(Module.schema_json(indent=2))

#annotate and declare JSON schema for Student class
print(Student.schema_json(indent=2))