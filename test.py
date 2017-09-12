import cs50

s = cs50.get_string()

for c in s:
    if c.isalpha() == False:
        print("N")
        exit(1)