"""
Remove first n Characters from a string

Problem Statement:
You have given a non-empty string, and a positive integer number n (less than the length of the string). You need to write a Python 
function that returns by removing the first n characters from the string.
Example
string = "Hi There! Welcome to UDMS" n = 10 Remove the first 10 characters from the string. Output: Welcome to UDMS


"""
n = int(input("Enter the number: "))
def removeString(input_string,n):
    if n < len(input_string):
        result = input_string[n:]
        return result
    
input_string = "Hi There! Welcome to UDMS"
print(input_string)
print(removeString(input_string,n))