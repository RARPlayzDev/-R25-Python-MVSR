# Variables
a = 9
b = 3
c="Kaarthik"
print("c=",c)
# Operators

# Arithmetic Operators
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a ** b =", a ** b)
print("a // b =", a // b)
print("a % b =", a % b)

# Assignment Operators
z = 12
print("z =", z)

z += 1
print("z = z + 1 :", z)

z -= 2
print("z = z - 2 :", z)

z *= 2
print("z = z * 2 :", z)

z //= 12
print("z = z // 12 :", z)

# Comparison Operators
print("z == 12 :", z == 12)
print("z != 11 :", z != 11)
print("z > 10  :", z > 10)
print("z < 13  :", z < 13)
print("a >= b  :", a >= b)
print("b <= a  :", b <= a)

# Logical Operators
print(a > b and a >= 9)
print(not a)

# Bitwise Operators
x = 5
y = 3
print("x & y (AND) :", x & y)
print("x | y (OR) :", x | y)
print("x ^ y (XOR) :", x ^ y)
print("~x (NOT) :", ~x)
print("x << 1 (LEFT SHIFT) :", x << 1)
print("x >> 1 (RIGHT SHIFT) :", x >> 1)

# Membership Operators
text = "python"
print("p in text :", "p" in text)
print("m not in text :", "m" not in text)

# Identity Operators
a1 = [1, 2, 3]
b1 = [1, 2, 3]
c1 = a1

print("a1 is b1 :", a1 is b1)
print("a1 is c1 :", a1 is c1)
print("a1 is not b1 :", a1 is not b1)
