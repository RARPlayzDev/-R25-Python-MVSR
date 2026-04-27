# ============ ZIP FUNCTION WITH TUPLES ============

t1 = (1, 2, 3, 4)
t2 = (10, 20, 30, 40)
t3 = ("a", "b", "c")

z = zip(t1, t2, t3)

print("Zip object:", z)
print("Zipped tuple:", tuple(z))

# Unequal length
t4 = (100, 200)
print("Unequal zip:", tuple(zip(t1, t4)))

# Looping through zip
for x, y in zip(t1, t2):
    print(x, y)

# Converting zip result
print("List:", list(zip(t1, t2)))
print("Set:", set(zip(t1, t2)))
print("Dict:", dict(zip(t1, t2)))

# Unzipping
zip
