for i in range(2):
    for k in range(3):
        print(i)
        for j in range(5):
            if j==3:
                break
            else:
                continue
else:
    print("Hello World")