"""
7: Python program to write data of one file to another except for lines 3, 6, and 9.
Problem statement
You have given a file data.txt, you need to write a Python program that reads the content from data.txt and writes its all content to new_data.txt except the lines 3, 6, and 9.
data.txt	new_data.txt
Line 1 data Line 2 data Line 3 data Line 4 data Line 5 data Line 6 data Line 7 data Line 8 data Line 9 data Line 10 data	Line 1 data Line 2 data Line 4 data Line 5 data Line 7 data Line 8 data Line 10 data


"""

with open('data.txt','r')as input_list:
    lines = input_list.readlines()

with open('new_data.txt','w') as output_list:
    for i, line in enumerate(lines, start=1):
        if i not in (3,6,9):
            output_list.write(line)

