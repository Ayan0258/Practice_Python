"""
how to use super

"""



# class Employe:
#     def __init__(self):
#         print("Constractor of Employe")

#     a = 1



# class Programer(Employe):
#     def __init__(self):
#         print("Constractor of prgramer")

#     b = 2

# class Manager(Programer):
#     def __init__(self):
#         super().__init__()
#         print("Constractor of Manager")

#     c = 3

# o = Manager()
# print(o.a, o.b, o.c)

"""
how to use class method
"""

# class Employe:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class atribute of a is {cls.a}")

# e = Employe()

# e.a = 45
# e.show()


"""
property decorater
"""
# class Employe:
#     a = 1

#     @classmethod
#     def show(cls):
#         print(f"The class atribute of a is {cls.a}")

#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"

#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]#this is work is if you space "" this will spilt a list like "Ayan DAs" into a [ayan,das]
#         self.lname = value.split(" ")[1]



# e = Employe()
# e.a = 45
# e.name = "Ayan Das"
# print(e.name)
# e.show()

"""

oparator overloading
"""

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n
    
n = Number(1)
m = Number(2)

print(n + m)