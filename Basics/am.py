""" num = int(input("Enter a number: "))

# Find the number of digits
n = len(str(num))

# Calculate the sum of each digit raised to the power n
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

# Check if it's an Armstrong number
if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
 """
""" num = int(input("Enter a number: "))

rev=0
# Calculate the sum of each digit raised to the power n
temp = num

while temp > 0:
    digit = temp % 10
    rev=rev*10+digit
    temp //= 10

print(rev)
 """
# Count number of vowels in a string

string = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in string:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
