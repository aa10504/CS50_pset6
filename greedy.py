import cs50

n = 0

while True:
    print("O hai! How much change is owed?")
    f = cs50.get_float()
    if f >= 0:
        break

rounded = f * 100

while rounded >= 25:
    rounded -= 25
    n += 1

while rounded >= 10:
    rounded -= 10
    n += 1

while rounded >= 5:
    rounded -= 5
    n += 1

while rounded >= 1:
    rounded -= 1
    n += 1

print("{}".format(n))