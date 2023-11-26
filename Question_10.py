"""
RockyDon Problem
Problem Statement
Given a positive integer number n. You need to write a Python script that iterates through 1 to n. Prints Rocky if the number is divisible by 3, print Don if the number is divisible by 5, Print “RockyDon” if the number is divisible by both 3 and 5, else it simply print the number.
Example
n = 10 1 2 Rocky 4 Don Rocky 7 8 Rocky Don


"""

def checkrockydon(i):
    if i % 3 ==0 and i% 5 ==0:
        return "rockydon"
    elif i % 3 == 0:
        return "rocky"
    elif i % 5 ==0:
        return "don"
    else:
        return str(i)
    
end = int(input("Enter the nTh number: "))
def rockydon():
    for i in range(1,end+1):
        result = checkrockydon(i)
        print(result,end=" ")

rockydon()