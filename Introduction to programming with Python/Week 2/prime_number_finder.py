Number_list=range(2,101)
for i in Number_list:
    for j in range(2,i):
        if (i%j==0):
            print(i, "is not a prime number")
            break
        else:
            print(i, "is a prime number")
            break