n = int(input())
zero=0
eagle=0
reshka=0
for a in range(n):
    b = int(input("0 or 1: "))
    if(b ==0):
        eagle+=1
    else:
        reshka+=1
if(reshka>eagle):
    print(eagle)
else:
    print(reshka)