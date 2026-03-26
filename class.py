class Employe:
    role = "Ai Engineer"
    salary = 200000

Ayan = Employe()
Ayan.name = "AyanDas"
print(Ayan.name,Ayan.role,Ayan.salary)

Ram = Employe()
Ram.name = "Ram lal"
print(Ram.name,Ram.role,Ram.salary)

/////staticmethod//

class Employe:
    role = "Ai Engineer"
    salary = 200000


    def getinfo(self):
        print(f"The role is: {self.role},The salary ammount is: {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Ayan = Employe()
Ayan.greet()
Ayan.getinfo() 

///constractor.//


class Employe:
    role = "Ai Engineer"
    salary = 200000

    def __init__(self):
        print("I am creating an object") #///dunder method which is automacticly called

    def getinfo(self):
        print(f"The role is: {self.role},The salary ammount is: {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


Ayan = Employe()
print(Ayan.role,Ayan.salary)