This is an overview of the code in each Pydantic file.

Why is Pydantic so useful?
- Data Validation
- Settings management
- Used by FastAPI
- Uses Type Annotations


1. "Main.py"
- We will demonstrate how to use Pydantic classes and data validation to model JSON data from an external API.
- define specific Pydantic data classes
- utilize type-annotations
- optional vs. constrained fields
- custom validator functions
- export models to dict or JSON data

2. "enums.py"
- contains specific data class for DepartmentEnum.
- This is a specific data class defined for the variable "Department".


----------------------------------------
Additional Pydantic functionality
- Nested Pydantic models
- Using typing.Literal to constrain values
- Defining default values for fields
- Generating JSON schema from Pydantic models


3. "models.py"
- added custom basemodel class "Module" to validate nested JSON data
- BaseModel class "Student" then inherits "Module" as a Pydantic List to iterate through nested JSON and return list if matches data validation.
- Added @field_validator function to check for length of list returned from JSON.
***Important distinction with numbers in Pydantic***
- if defining a class value of int | float, all numbers will get converted to an integer regardless.
Example:
class Number(BaseModel):
    value: int | float

number = Number({'value': 2.2})
print(number) #float converted to int, number=2

4. "models_main.py"
- new version of models.py to work with models.py file.


5. "jsonschema.json"
- created JSON output file from pydantic code. 
- pip install datamodel-core-generator
- command line interface for generating pydantic json schema
- command line: datamodel-codegen --input jsonschema.json --output models2.py #outputs a new file "models2.py"


6. "models2.py"
- pydantic data model automatically generated from JSON schema.
