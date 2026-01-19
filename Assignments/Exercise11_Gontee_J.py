#Input
heightnum = int(input("Enter a heightnum: "))

#Process/Output
for row in range(heightnum):
    for col in range(heightnum - row -1):
        print(" ",end="")
    for col in range(row + 1):
        print("*", end=" ")
    print()