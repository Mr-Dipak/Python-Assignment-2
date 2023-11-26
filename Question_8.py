"""
Q 8. Write a Python program to print the sum of first n numbers.
Problem Statement:
You need to write a Python program that accepts an N positive integer from the user and print the sum upto that N number For example,
if the user input 4 the program should print 10 N = 4 1 + 2 + 3 + 4 = 10 .


"""

def sumof_N_num(a):
    if a >= 0:
        sum = a*(a+1)/2
        return sum
    else:
        print("you are not etered positive integer.")

n = int(input("Enter the number: "))
result = sumof_N_num(n)
print(result)