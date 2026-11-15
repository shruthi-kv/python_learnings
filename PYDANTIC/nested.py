from pydantic import BaseModel
from typing import List, Optional
# class Address(BaseModel):
#     country : str
#     state : str
#     city : str

# class Person(BaseModel):
#     name : str
#     age : int
#     address: Address


# Person1data ={
#     "name" :"Shruthi",
#     "age" : 24,
#     "address": {
#         "country" :"India",
#         "state" :"Karnatka",
#         "city" :"Bangalore"
#     }
# }

# person1 = Person(**Person1data)
# print(person1.model_dump())


class Address(BaseModel):
    country : str
    state : str
    city : str

class Person(BaseModel):
    name : str
    age : int
    address: List[Address]


Person1data ={
    "name" :"Shruthi",
    "age" : 24,
    "address": [
        {
        "country" :"India",
        "state" :"Karnatka",
        "city" :"Bangalore"
        },
                {
        "country" :"India",
        "state" :"Karnatka",
        "city" :"Bangalore"
        },
                {
        "country" :"India",
        "state" :"Karnatka",
        "city" :"Bangalore"
        }
    
    
    ]
}

person1 = Person(**Person1data)
print(person1.model_dump())



class FamilyTree(BaseModel):
    name: str
    children : Optional[List["FamilyTree"]] = None

FamilyTree.model_rebuild()

data = {
    "name":"root",
    "children":[
        {
            "name":"child_1",
            "children":[
                {"name":"grand_1"},
                {"name":"grand_2"}
            ]
        },
         {
                    "name":"child_2",
                    "children":[
                        {"name":"grand_3"},
                        {"name":"grand_4"}
                    ]
                }
    ]
}

fam = FamilyTree(**data)
print(fam.model_dump())