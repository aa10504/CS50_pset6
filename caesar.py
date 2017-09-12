import sys
import cs50

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar.py k")
        exit(1)
    else:
        key = int(sys.argv[1])
        print("plaintext: ",end="")
        p_text = cs50.get_string()

        c_text = cipher(key, p_text)

        print("ciphertext: {}".format(c_text))

def cipher(a, word):
    b = a % 26
    tmp = None

    for i in range(len(word)):
        if i == 0:
            if word[i] >= 'A' and word[i] <= 'Z' and chr(ord(word[i]) + b) > 'Z':
                tmp = chr(ord('A') + ord(word[i]) + b - ord('Z') - 1)
            elif word[i] >= 'a' and word[i] <= 'z' and chr(ord(word[i]) + b) > 'z':
                tmp = chr(ord('a') + ord(word[i]) + b - ord('z') - 1)
            elif word[i] >= 'A' and word[i] <= 'Z':
                tmp = chr(ord(word[i]) + b)
            elif word[i] >= 'a' and word[i] <='z':
                tmp = chr(ord(word[i]) + b)
            else:
                tmp = word[i]
        else:
            if word[i] >= 'A' and word[i] <= 'Z' and chr(ord(word[i]) + b) > 'Z':
                tmp = tmp + chr(ord('A') + ord(word[i]) + b - ord('Z') - 1)
            elif word[i] >= 'a' and word[i] <= 'z' and chr(ord(word[i]) + b) > 'z':
                tmp = tmp + chr(ord('a') + ord(word[i]) + b - ord('z') - 1)
            elif word[i] >= 'A' and word[i] <= 'Z':
                tmp = tmp + chr(ord(word[i]) + b)
            elif word[i] >= 'a' and word[i] <='z':
                tmp = tmp + chr(ord(word[i]) + b)
            else:
                tmp = tmp + word[i]
    return tmp

if __name__ == "__main__":
    main()