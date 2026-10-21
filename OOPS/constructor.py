


class Person:
    company = "IBM"

    def __init__(self,salary,name,bond,company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def getSalary(self):
        return self.salary

    def getInfo(self):
        print (f"the person name is {self.name}, and his term is {self.bond} years")


e = Person(2000,"John",5,"Deloitte")
print(e.getSalary())
e.getInfo()
print(e.company)
print(Person.company)

print(dir(e))