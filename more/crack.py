import cs50
import sys
import crypt

def main():
    if len(sys.argv) != 2:
        print("Usage: python crack.py hash")
        exit(1)

    salt = "50"
    alphabet = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" #52個字符
    pw = "a" # initialize
    for c4 in alphabet:
        for c3 in alphabet:
            for c2 in alphabet:
                for c1 in alphabet:
                    if c1.isalpha() and c2.isalpha() == False and c3.isalpha() == False and c4.isalpha() == False:
                        pw = c1
                    elif c1.isalpha() and c2.isalpha() and c3.isalpha() == False and c4.isalpha() == False:
                        pw = c1 + c2
                    elif c1.isalpha() and c2.isalpha() and c3.isalpha() and c4.isalpha() == False:
                        pw = c1 + c2 + c3
                    elif c1.isalpha() and c2.isalpha() and c3.isalpha() and c4.isalpha():
                        pw = c1 + c2 + c3 + c4
                    if crypt.crypt(pw, salt) == sys.argv[1]:
                        print(pw)
                        exit(0)

if __name__ == "__main__":
    main()