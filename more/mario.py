import cs50

while True:
    print("Height: ",end="")
    x = cs50.get_int()
    if x >= 1 and x <= 22:
        break

for i in range(x):
    for j in range(i + 1, x):
        print(" ",end="")
    for k in range(i + 1):
        print("#",end="")
    print("  ",end="")
    for n in range(i + 1):
        print("#",end="")
    print("")