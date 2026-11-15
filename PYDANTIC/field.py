from pydantic import BaseModel, Field, ValidationError, model_validator, field_validator, EmailStr, HttpUrl,PositiveInt

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




class Book(BaseModel):
    title : str = Field(validation_alias ="book_title", serialization_alias="bookTitle")
    author : str = Field(validation_alias="book_author", serialization_alais="bookAuthor")


book1=Book(book_title="Tuesdays with morie", book_author="martin")

print(book1.model_dump(by_alias=True))

book2Data ={
    "book_title" :"ABC",
    "book_author" :"BNV"
}

book2=Book(**book2Data)
print(book2)


class Product(BaseModel):
    name : str = Field(min_length = 1, max_length = 50)
    price :  int = Field(gt = 0)
    description : str | None = Field(default = None, max_length =50)

product1data ={
    "name" : "macbook",
    "price" : 200000,
    "description" : "laptop for coding practice"
}

product1 = Product(**product1data)
print(product1)


class Bookish(BaseModel):
    title : str = Field(min_length =0, max_length=100)
    author : str
    isbn : str = Field(default = None)
    price : float = Field(le=1000, gt=0)
    in_stock : bool = Field(default=True)

bookishData ={
    "title" :"some title",
    "author" : "some author",
    # "isbn" : "something",
    "price" : 25.7,
    "in_stock" : True
}

Book3 = Bookish(**bookishData)
print(Book3.model_dump())





class Event(BaseModel):
    name: str
    start_hr : int
    end_hr : int

    @model_validator(mode="after")
    def check_time(self):
        if self.end_hr < self.start_hr:
            raise ValueError("end_hr is lesser than start_hr, Please fix this!")
        return self

event1 = Event(name="hackathon", start_hr =10, end_hr =90) #how can the start_hr be before the end_hr

print(event1.model_dump())





class Delivery(BaseModel):
    pickup : int
    drop : int

    @model_validator(mode="before")
    @classmethod
    def fix_inputs(cls, data):
        print("Before Validation sees raw data :", data)

        if int(data['drop']) < int(data['pickup']):
            data['drop'], data['pickup'] = data['pickup'], data['drop']
        return data

order1 = Delivery(pickup =12, drop =4)
print(order1.model_dump())



class Price(BaseModel):
    price : float
    @field_validator("price")
    def convertPositive(value):
        if value <= 0:
            raise ValueError("Price is not valid, please fix it!")
        return value

buy1= Price(price = 7.4)

print(buy1.model_dump())


class Contact(BaseModel):
    email : EmailStr
    website : HttpUrl
    followers : PositiveInt

good = Contact(
    email = "shruthi@gmail.com",
    website="https://www.mywebsite.com",
    followers = 100
)

print(good.model_dump())