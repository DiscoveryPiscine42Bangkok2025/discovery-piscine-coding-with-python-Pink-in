n1a = 0
n2a = 0
n1= int(n1a)
n2= int(n2a)
while n1 <= 10:
    print(f"Table de {n1}: ",end="")
    while n2 <= 10:
        print(f"{n1*n2} ",end="")
        n2 += 1
    print()
    n1 += 1
    n2=0
