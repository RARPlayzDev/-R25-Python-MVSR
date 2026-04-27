t = (10, 20, 30, 20, 40)
t2 = (50, 60)
print("Tuple t:", t)
print("Tuple t2:", t2)

#=== TUPLE METHODS ===

# 1. count()
print("Count of 20:", t.count(20))

# 2. index()
print("Index of 30:", t.index(30))

#=== BUILT-IN FUNCTIONS WITH TUPLE ===

print("Length:", len(t))
print("Maximum:", max(t))
print("Minimum:", min(t))
print("Sum:", sum(t))

# sorted() returns a list
print("Sorted:", sorted(t))

# tuple() conversion
l = [1, 2, 3]
print("List to Tuple:", tuple(l))
#=== TUPLE OPERATIONS ===

# Concatenation
concat = t + t2
print("Concatenation:", concat)

# Repetition
repeat = t * 2
print("Repetition:", repeat)

# Membership
print("Is 20 in tuple?", 20 in t)
print("Is 99 not in tuple?", 99 not in t)

# Slicing
print("Slice [1:4]:", t[1:4])
print("Slice [:3]:", t[:3])
print("Slice [::2]:", t[::2])

#=== ITERATION ===
for item in t:
    print(item, end=" ")
print()


#=== TUPLE COMPARISON ===
print((1, 2, 3) == (1, 2, 3))
print((1, 2, 3) < (1, 2, 4))


#=== IMMUTABILITY DEMO ===
try:
    t[0] = 100
except TypeError as e:
    print("Error:", e)


#=== DELETE TUPLE ===
temp = (1, 2, 3)
print("Before delete:", temp)
del temp
print("Tuple deleted successfully")

