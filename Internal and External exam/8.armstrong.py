num = int(input("Enter a number: "))
temp = num
powr = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** powr
    temp = temp//10
if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")

'''
153%10=3
153//10=15
15%10=5
15//10=1
1%10




'''
