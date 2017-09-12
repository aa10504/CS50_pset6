alphabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c2 in alphabet:
    for c1 in alphabet:
        if c1.isalpha() and c2.isalpha() == False:
            pw = c1
            print(pw)
        elif c1.isalpha() and c2.isalpha():
            pw = c1 + c2
            print(pw)