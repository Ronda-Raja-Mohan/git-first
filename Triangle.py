
a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")

    if a == b == c:
        print("It is an Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle")
    elif (a*a + b*b == c*c) or (b*b + c*c == a*a) or (a*a + c*c == b*b):
        print("It is a Right Angled Triangle")
    else:
        print("It is a Scalene Triangle")
else:
    print("Not a Valid Triangle")