class Employe:
    def __init__(self):
        print("Constractor of Employe")

    a = 1



class Programer(Employe):
    def __init__(self):
        print("Constractor of prgramer")

    b = 2

class Manager(Programer):
    def __init__(self):
        super().__init__()
        print("Constractor of Manager")

    c = 3

o = Manager()
print(o.a, o.b, o.c)