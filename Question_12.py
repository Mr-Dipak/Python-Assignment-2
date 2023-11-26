"""
Q 12. Write a Python program that accepts a list of 10 float numbers from the user.
Problem Statement
You need to write a Python program that accepts 10 float numbers from the user and adds them to a list.
Example: If user enters 10 20 30 40 50 60 70 80 90 100
Output: [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.00


"""
float_list = []
for i in range(10):
    number = float(input(f"Enter number {i+1}: "))
    float_list.append(number)
print(float_list)

    


