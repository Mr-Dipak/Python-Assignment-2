"""
10: Python program to count the occurrence of each item from a list.
Problem Statement
You have given a list with repeated items and you need to write a script that counts the occurrence of every list item.
Example
given_list = [10, 20, 30, 10, 30, 20, 20, 20, 40, 50] Output = {10 : 2, 20 : 4, 30: 2, 40: 1, 50: 1 }

"""

def count_occurrence(input_list):
    item_count = {}

    for item in input_list:
        if item in item_count:
            item_count[item] +1
        else:
            item_count[item] = 1
    return item_count

given_list = [10, 20, 30, 10, 30, 20, 20, 20, 40, 50]

result = count_occurrence(given_list)

print(result)