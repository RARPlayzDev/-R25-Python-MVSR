y = int(input().strip())

if y < 1000 or y > 9000:
    print("Invalid")
else:
    while True:
        y += 1
        a = y // 1000
        b = (y // 100) % 10
        c = (y // 10) % 10
        d = y % 10

        if a != b and a != c and a != d and b != c and b != d and c != d:
            print(y)
            break
