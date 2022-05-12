num = int(input("Introduce la base de la pirámide: "))


for i in range(1,num +1): 
    j = num - i
    k = j

    while k < num:
        k = k +  1
        print(k,end="")
    print("")


