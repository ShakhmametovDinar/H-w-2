x=int(input("Введите число: "))
y=int(input("Введите число: "))
for a in range(x):
    for b in range(y):
        if x == a+b and y==a*b:
            print(a,b)