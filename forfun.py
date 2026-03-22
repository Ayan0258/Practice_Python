<<<<<<< HEAD
# n = int(input("Enter your number: "))

# for i in range(1, n+1):

#     if i == 1 or i == 2 or i == n:
#         print("*"*i)

#     else:
#         print("*", end="")
#         print(" "*(i-2), end="")
#         print("*")

"""

*****
*   *
*   *
*   *
*

"""

n=int(input("Enter the number: "))

for i in range(1, n+1):

    if(i==1):
        print("*"*n)
    elif(i==n):
        print("*")

    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")
=======
# n = int(input("Enter your number: "))

# for i in range(1, n+1):

#     if i == 1 or i == 2 or i == n:
#         print("*"*i)

#     else:
#         print("*", end="")
#         print(" "*(i-2), end="")
#         print("*")

"""

*****
*   *
*   *
*   *
*

"""

n=int(input("Enter the number: "))

for i in range(1, n+1):

    if(i==1):
        print("*"*n)
    elif(i==n):
        print("*")

    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*")
>>>>>>> db292639cc0b7b623393d4eb4882fd2855be1a03
    print("")