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

class Employe:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class atribute of a is {cls.a}")

e = Employe()

e.a = 45
e.show()