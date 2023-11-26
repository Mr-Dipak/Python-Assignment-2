"""
Middle letter:
Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter.
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".


"""

def mid(input_string):
    length = len(input_string)
    
    
    if length % 2 == 1:
        mid_index = length //2
        return input_string[mid_index]
    else:
        return ("")

string = "abc"
result1 = mid(string)

string2 = "aaaa"
result2 = mid(string2)

print("First Example of odd String result is: ", result1, " Secnong even String result is: ",result2)


    