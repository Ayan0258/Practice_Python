"""
1. Create a Class “Programmer” for storing information of few programmers working at Microsoft.

2. Write a class “Calculator” capable of finding square, cube and square root of a number.

3. Create a class with a class attribute 'a'; create an object from it and set 'a' directly using object. Does this change the class attribute?

4. Add a static method in problem 2, to greet the user with hello.

5. Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.

6. Can you change the self-parameter inside a class to something else (say “harry”)? Try changing self to “slf” or “harry” and see the effects.

"""

# //1//

# class programmers:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin,company):
#         self.name = name
#         self.salary = salary
#         self.pin =pin
#         self.company = company

# p =programmers("Ayan",120000,70009,"nvdia")
# print(p.name,p.salary,p.pin,p.company)
# m =programmers("mita",120000,70009,"microsoft")
# print(m.name,m.salary,m.pin,m.company)


# ///2///


# class Calculator:
#     def __init__(self, n):
#         self.n = n

#     def square(self):
#         print(f"The square value is:{self.n**2}")

#     def cube(self):
#         print(f"The cube value is: {self.n**3}")

#     def squareroot(self):
#         print(f"the squareroot value is: {self.n**1/2}")


# a = Calculator(5)
# a.square()
# a.cube()
# a.squareroot()

# ///3///


# class demo:
#     a = 4

# o = demo()
# print(o.a) #print class atribute . because instance atribute not presnt
# o.a = 0 #instance atribute is set
# print(o.a)#print instant atribute because its present here
# print(demo.a)
