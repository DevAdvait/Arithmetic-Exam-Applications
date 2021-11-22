a, b, c = input().split()
a = int(a)
c = int(c)

if b == "+":
    add = a + c
    print(add)
elif b == "-":
    subtract = a - c
    print(subtract)
elif b == "*":
    mul = a * c
    print(mul)