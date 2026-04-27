a=10
b=50
def calculate_sum():
    global a
    a=20
    result=a+b
    print(f"{result}")
    return result
def multiply_numbers():
    result=a*b
    print(f"{result}")
    return result
print(a)
calculate_sum()
a=15
print(a)
multiply_numbers()
print(a)
"""
Output:
10
70
15
750
15

"""