import pydantic 
from pydantic import BaseModel

print(pydantic.__version__) #2.14.2

class User(BaseModel):
    name:str   #type hints are required
    age : int
    is_active : bool


user1 = User(name="Bob",age=34,is_active=True)
print(user1)
print(user1.model_dump())

#we can set default values
#when you instanciate an object in this class, you might not necessarily pass a parameter, this could because of several reason,
#eg : if you building an api, that api might not have a parameter passed in, to do that you cna cretae default parameters.

class Student(BaseModel):
    name : str
    age : int = 18
    place : str

student1 = Student(name ="shruthi", age =32, place = "banglore")
student2 = Student(name="ball", place="chennai")

print(student1)
print(student1.model_dump())
print(student2)



# type validation - pydantic has in-built conversion
student3 = Student(name="Vivan",age="34", place="bombay")
print(student3)



#FIELDS
#In pydantic, Fields() lets us add metadata, validation rules, and custom behaviour to a model field.
