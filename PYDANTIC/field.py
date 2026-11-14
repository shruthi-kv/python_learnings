from pydantic import BaseModel, Field, ValidationError

class FieldUser(BaseModel):
    name : str = Field(description = "The user's full name", default = "john")

user1 = FieldUser(name="vaibhav")
print(user1)

user2 = FieldUser()
print(user2)

class FlawedUser(BaseModel):
    age : int = Field(description="Name of the user", default ="twenty")

flaw1 = FlawedUser()
print(flaw1)


class PoperUser(BaseModel):
    age : int = Field(description="age of the user", default="twelve", validate_default= True)

# try:
#     proper = PoperUser()
# except ValidationError as e:
#     print(e)



class Package(BaseModel):
    weight : float = Field(alias="pkg_weight_kg")
    destination : str = Field(alias = "pkg_destination_place")
    is_fragile : bool = Field(alias="pkg_is_fragile")

data = {
    "pkg_weight_kg" : 3.5,
    "pkg_destination_place" : "Chennai",
    "pkg_is_fragile" : False,
}


pack = Package(pkg_weight_kg=3.5, pkg_destination_place="Bangalore", pkg_is_fragile=False )
print(pack)

pack2 = Package(**data)
print(pack2)



class Student(BaseModel):
    email : str = Field(validation_alias ="student_email", serialization_alias ="studentEmail")

student1 = Student(student_email = "hello@gmail.com")

print(student1.model_dump(by_alias=True))