import cs50

alphabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c4 in alphabet:
    for c3 in alphabet:
        for c2 in alphabet:
            for c1 in alphabet:
                if c1.isalpha() and c2.isalpha() == False and c3.isalpha() == False and c4.isalpha() == False:
                    pw = c1
                    print(pw)
                elif c1.isalpha() and c2.isalpha() and c3.isalpha() == False and c4.isalpha() == False:
                    pw = c1 + c2
                    print(pw)
                elif c1.isalpha() and c2.isalpha() and c3.isalpha() and c4.isalpha() == False:
                    pw = c1 + c2 + c3
                    print(pw)
                elif c1.isalpha() and c2.isalpha() and c3.isalpha() and c4.isalpha():
                    pw = c1 + c2 + c3 + c4
                    print(pw)

