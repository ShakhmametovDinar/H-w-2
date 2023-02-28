n = int(input())
b=0
for a in range(n):
    if(b<n/2):
        b = 2 ** a
        print(b)
