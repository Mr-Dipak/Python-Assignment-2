"""
Python program to print the first non-repeated character from a string.
Problem Statement: You have given a string and you need to find the first non-repeated characters.
Example
given_string = welcome to techgeekbuzz.com website Output l


"""
def first_non_repeated_char(input_string):
    char_count = {}

    for char in input_string:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char] = 1

        
    for char in input_string:
        if char_count[char] == 1:
            return char
            
    return None
            

given_string= "welcome to techgeekbuzz.com website"

result = first_non_repeated_char(given_string)

print(result)