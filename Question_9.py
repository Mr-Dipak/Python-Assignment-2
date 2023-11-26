"""

Q 9.Write a Python program to print all the prime numbers between two intervals
Problem Statement You need to write a Python script that asks the user to enter an interval of positive numbers and print all the prime numbers
of that interval.


"""

def is_prime(num):

    if num < 2:
        return False
    
    for i in range(2,int(num**0.5)+1):
       if num % i ==0:
           return False
    return True

start = int(input("Enter Starting number: "))
end = int(input("Enter Ending number: "))


def primenum(start, end):
    for number in range(start, end +1):
        if is_prime(number):
            print(number)

primenum(start,end)



