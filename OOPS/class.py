#class is blueprint or a template.
# EG : Form of an exam that contains name, place.

#object is an instance created from a class.
#EG : Form which contains the data of John Doe

class Employee:
    name : "HP"

    def get_salary(self):
        print(self)
        return 200000


e =  Employee()
print(e.get_salary())


c = Employee()
print(c.get_salary())