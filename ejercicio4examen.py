n= int(input("Introudce un número: "))
for i in range(0, n, 1):
    for j in range(i, 0, -1):
        print("*", end=" ")
    print("*")



