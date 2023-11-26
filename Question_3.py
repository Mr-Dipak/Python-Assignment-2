"""
Q 3. Print square of all numbers between 1 to 10 except even numbers

"""

nums = [1,2,3,4,5,6,7,8,9,10]

squir_num = 0

for num in nums:
    if num %2 != 0:
        squir_num = num*num
        print(squir_num)
        
