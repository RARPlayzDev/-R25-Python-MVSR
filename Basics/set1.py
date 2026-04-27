s = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print("Set s:", s)
print("Set s2:", s2)

#=== SET METHODS ===
s.add(70)
print("add:", s)

s.update([80, 90])
print("update:", s)

s.remove(20)
print("remove:", s)

s.discard(100)
print("discard:", s)

print("pop:", s.pop())
print("after pop:", s)

s_copy = s.copy()
print("copy:", s_copy)

s.clear()
print("clear:", s)

#=== BUILT-IN FUNCTIONS ===
nums = {1, 2, 3, 4, 5}
print("len:", len(nums))
print("max:", max(nums))
print("min:", min(nums))
print("sum:", sum(nums))
print("sorted:", sorted(nums))
print("set from list:", set([1, 2, 2, 3]))

#=== SET OPERATIONS ===
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("union:", a | b)
print("intersection:", a & b)
print("difference:", a - b)
print("symmetric diff:", a ^ b)

#=== SET RELATIONS ===
print("issubset:", {1, 2}.issubset(a))
print("issuperset:", a.issuperset({1, 2}))
print("isdisjoint:", a.isdisjoint({9, 10}))

#=== MEMBERSHIP & LOOP ===
print(3 in a)
for i in a:
    print(i, end=" ")
print()

#=== FROZENSET ===
fs = frozenset([1, 2, 3])
print("frozenset:", fs)

#=== DELETE SET ===
temp = {9, 8, 7}
print("before delete:", temp)
del temp
print("set deleted")
