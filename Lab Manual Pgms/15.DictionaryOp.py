# 15. Dictionary operations
print("=== Program 15: Dictionary Operations ===")
my_dict = {}
n = int(input("How many elements to add? "))
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value
print(f"Dictionary: {my_dict}")
remove_key = input("Enter key to remove: ")
if remove_key in my_dict:
    del my_dict[remove_key]
    print(f"After removal: {my_dict}")
else:
    print("Key not found!")
