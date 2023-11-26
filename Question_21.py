def add_dots(input_string):
    dotted_str = '.'.join(input_string)
    return dotted_str

def remove_dots(input_string):
    undotted_str = input_string.replace('.','')
    return undotted_str

str = "test"
dotted_result = add_dots(str)
undotted_result = remove_dots(dotted_result)

print(f"this is a origional string: {str}")
print(f"this is a dotted result: {dotted_result}")
print(f"this is a undotted_result: {undotted_result}")
