"""for i in range(2):
    for k in range(3):
        print(i)
        for j in range(5):
            if j==3:
                break
            else:
                continue
    else:
        print("Hello World")"""
"""
i=0,1
k=0,1,2
j=0,1,2,3,4

Output:-
0
0
0
Hello world
1
1
1
Hello World
"""

for i in range(5):
    for k in range(3):
        print(i)
        for j in range(5):
            if j==4:
                break
            else:
                continue
        if k == 2:
            print("$")
        else:
            pass
"""
i=0,1,2,3,4
k=0,1,2
Output:
0
0
0
$
1
1
1
$
2
2
2
$
3
3
3
$
4
4
4
$
"""