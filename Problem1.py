
# a = 1 #its a integer
# b = 3.5 #its a floationg point number
# c = "Harry" #its a string
# d = False #its a bolean 
# e = None # e is a none type variable
# d = 5 != 5
# print (d) 

# a = "33.2"
# b = float(a)
# t = type(b)
# print(t)

# a = int(input("Enter the Number 1 "))
# b = int(input("Enter the Number 2 "))

# print("Number a is greater than b: ", a>b)


# name = "Papina"
# nameshort= name [0:4]
# print(nameshort)
# Character1 = name [1]
# print(Character1)

# name = "tumkipuki"
# # print(name[-5:-1])
# # print(name[4:8])
# print(len(name))
# print(name.endswith("ki"))


# name=input("Enter your Name")
 
# print(f"GOOd afternoon {name}")


# letter = """
# hey bro |Name|
# can you give me my money back
# you have to give my money in this |date|
# """
# print(letter.replace("|Name|","Bikram").replace("|date|","1st january 2005"))


# Marks =[]

# p1 = input ("Enter your Markss name:")
# Marks.append(p1)
# p2 = input ("Enter your Markss name:")
# Marks.append(p2)
# p3 = input ("Enter your Markss name:")
# Marks.append(p3)
# p4 = input ("Enter your Markss name:")
# Marks.append(p4)
# p5 = input ("Enter your Markss name:")
# Marks.append(p5)
# p6 = input ("Enter your Markss name:")
# Marks.append(p6)
# p7 = input ("Enter your Markss name:")
# Marks.append(p7)
# p8 = input ("Enter your Markss name:")
# Marks.append(p8)
# Marks.sort()
# print(Marks)\\
# a = (2,3,4,5,2,3,1,0,0,0,0,4,3,4,0,)
# n = a.count(0)
# print(n)
# s1 = {1,2,93,48,5}
# s2 = {3,1,44,47,48,5}
# print(s1.union(s2))
# print(s1.intersection(s2))
# words = {
#     "shukor": "pig",
#     "jol" : "Water",
#     "gach" : "Tree"
# }

# word =input("Enter the bengali word :")
# print(words[word])
# s = set()
# n=input("enter the number: ")
# s.add(int(n))
# n=input("enter the number: ")
# s.add(int(n))
# n=input("enter the number: ")
# s.add(int(n))
# n=input("enter the number: ")
# s.add(int(n))
# n=input("enter the number: ")
# s.add(int(n))
# n=input("enter the number: ")
# s.add(int(n))
# n=input("enter the number: ")
# s.add(int(n))
# print(s)


# d = {}

# name = input("Enter your name: ")
# lang = input("Enter your language: ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your language: ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your language: ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your language: ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your language: ")
# d.update({name: lang})
# name = input("Enter your name: ")
# lang = input("Enter your language: ")
# d.update({name: lang})

# print(d)


# a = int(input("Enter your age; "))

# if(a>18):
#     print("You are above 18 +")
#     print("good for you")

# elif(a<0):
#     print("Are you out of your mind")
# else:
#     print("You are underaged")


# p1=int(input("Enter the no of p1: "))
# p2=int(input("Enter the no of p2: "))
# p3=int(input("Enter the no of p3: "))
# p4=int(input("Enter the no of p4: "))

# if(p1>p2 and p1>p3 and p1>p4):
#     print("Greater number is p1:", p1)

# elif(p2>p1 and p2>p3 and p2>p4):
#     print("Greater number is p2:", p2)

# elif(p3>p1 and p3>p2 and p3>p4):
#     print("Greater number is p3:", p3)

# elif(p4>p1 and p4>p2 and p4>p3):
#     print("Greater number is P4:", p4)



# marks1 = int(input("Enter your marks number: "))
# marks2 = int(input("Enter your marks number: "))
# marks3 = int(input("Enter your marks number: "))

# total_percentage=(100*(marks1+marks2+marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print("You are passed this year \n conrats",total_percentage)

# else:
#     print("you are failed this year \n now go home and cry",total_percentage)

# a1="i am not a bot"
# a2="click this"
# a3="yes"

# message=(input("Enter your message"))
# if(a1 in message) or (a2 in message) or (a3 in message):
#     print("this is spam message")

# else:
#     print("This is not a spam")

# marks = int(input("Enter your marke"))

# if(marks<=100 and marks>=90):
#     grade = "E"
# elif(marks<=90 and marks>=80):
#     grade = "O"
# elif(marks<=80 and marks>=70):
#     grade = "A"
# elif(marks<=70 and marks>=60):
#     grade = "B"
# elif(marks<=60 and marks>=50):
#     grade = "C"
# elif(marks<=50 and marks>=40):
#     grade = "D"
# elif(marks<=40):
#     grade="F"


# print("youyr grade is",grade)

# i = 0

# while(i<8):
#     print("harry")
#     i =i + 1

# for i in range(1, 6):
#     print(i)
# y=[1,3,4,5,6]

# for item in y:
#     print(item)

# else:
#     print("done")


# for i in range(100):
#     if(i == 78):
#         continue
#     print(i)

# n = int(input("Enter your number"))

# for i in range(1, 11):
#     print(f"{n} x {i} = {n * i}")

# a =["Ayan", "Eater", "Ramash", "Eshita"]

# for name in a:
#     if (name.startswith("E")):
#         print(f"hello{name}")

# n =int(input("Enter your number:"))

# for i in range(2,n):
#     if(n%i)==0:
#         print("the number is prime")
#         break
# else:
#     print("Your number is prime")

# n =int(input("Enter your number: "))
# i = 1
# sum = 0 
# while(i<=n):
#     sum += i
#     i+=1

# print(sum)

# n = int(input("Enter your number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i

# print(f"the factorial of {n}is {product}")

# '''
# n = 5
#      *
#     ***
#    *****
#   *******
#  *********
# '''

# n = int(input("Enter the number : "))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")

# """

# ***
# * *
# ***

# """
# n =int(input("enter your number: "))
# for i in range (1,n+1):
#     if (i==1 or i==n):
#         print("*"* n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")


# """
# *
# * *
# *   *
# *     *
# *********


# *
# **
# * *
# *  *
# *****

# """
# n =int(input("enter your number: "))
# for i in range(1,n+1):
#     if(i==1 or i==2 or i==n):
#         print("*"*i)
#     else:
#         print("*",end="")
#         print(" "*(n-2),end="")
#         print("*",end="")
#     print("")

# n =int(input("Enter your number: "))

# for i in range(1,11):
#     print(f"{n} x {11-i}={n*(11-i)}")

# def goodday(name, ending="Go now"):
#     print(f"goodday {name}")
#     print(ending)

# goodday("Ayan", "Thanks for comming")
# goodday("Harry")
# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     return n * factorial(n-1)

# n = int(input("Enter your number"))
# print(f"value of the factorial number",{factorial(n)})

# """"

# from here i connect my git hub 

# """


# print("github test")

# lets see if this ubdate or not


# def greatest(a, b, c):
#     if (a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a = 1
# b = 6
# c = 3

# print(greatest(a, b, c))

# def f_to_c(f):
#     return 5*(f-32)/9

# f =int(input("Enter the teamparature in F: "))
# e = f_to_c(f)
# print(f"{round(e,3)}c")



# def star(n):
#     if (n==0):
#         return
#     print("*" * n)
#     star(n-1)

# star(6)

# def rem(l,word):
#     n=[]
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))  
#     return n    
# l = ["Harry", "Ayan", "Anu", "Anushka", "an"]
# print(rem(l,"an"))




# """
# lets make a game

# Rock, Paper, Scissor

#     "1. Rock",
#     "2. Paper",
#     "3. Scissor"


# """
# import random
# computer = random.choice([1,2,3])
# youfist =int(input("Enter your first movee(1 = Rock, 2 = Paper, 3 = Scissor) : "))

# print("Computer chose",computer)

# if (computer==youfist):
#     print("you can't win with same move")

# else:
#     if(computer==1 and youfist==2):
#         print("You win")

#     elif(computer==2 and youfist==1):
#         print("You Lose")

#     elif(computer==1 and youfist==3):
#         print("You Lose")

#     elif(computer==3 and youfist==1):
#         print("You win")

#     elif(computer==2 and youfist==3):
#         print("You win")

#     elif(computer==3 and youfist==2):
#         print("You Lose")

#     else:
#         print("somthing went worng")



"""
making files
"""

pt = "Hey this is my first way to make txtfile making"

f = open("myfile.txt", "w")
f.write(pt)
f.close()