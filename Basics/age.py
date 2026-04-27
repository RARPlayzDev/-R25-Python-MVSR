def calculate_age(cd, cm, cy, bd, bm, by):
    age = cy - by
    if (cm < bm) or (cm == bm and cd < bd):#birthday passed or not logic
        age = age - 1
    return age

current = input("Enter current date (dd/mm/yy): ")
cd, cm, cy = map(int, current.split('/'))


dob = input("Enter your date of birth (dd/mm/yy): ")
bd, bm, by = map(int, dob.split('/'))

age = calculate_age(cd, cm, cy, bd, bm, by)
print("Your age is:", age, "years")
