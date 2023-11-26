"""
Exercise 8: Python program to print n number of the Fibonacci sequence using recursion.

Problem Statement:

A Fibonacci sequence is a series of integers that start from 0 and 1, and every next number is decided by the sum of the previous two numbers.
You need to write a Python code that asks the user to enter the value n, representing the length of the sequence.
And a recursive function to print a Fibonacci sequence of n length.
Example
n = 10 Output: 0 0 1 2 3 5 8 13 21 34


"""
n = int(input("Enter the "))

def fabonacci(n):
    if n<=0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:

        feb_seq = fabonacci(n-1)
        feb_seq.append(feb_seq[-1]+feb_seq[-2])
        return feb_seq

result=fabonacci(n)
print(result)

    