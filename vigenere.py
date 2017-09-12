import sys
import cs50

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar.py k")
        exit(1)

    for c in sys.argv[1]:
        if c.isalpha() == False:
            print("Usage: python caesar.py k")
            exit(1)

    print("plaintext: ",end="")
    p_text = cs50.get_string()
    c_text = vigenere(sys.argv[1], p_text)
    print(c_text)

def vigenere(key, word):
    translated = [] # 存加密過的字符的list

    key2 = [] # 將密碼長度改成和plain text一樣,且通通換成integer(A=0,a=0,B=2....)
    counter = 0
    for c in word:
        if c.isalpha():
            if key[counter].isupper():
                key2.append(ord(key[counter]) - 65)
            else:
                key2.append(ord(key[counter]) - 97)

            if counter < (len(key) - 1):
                counter += 1
            else:
                counter = 0

    counter2 = 0
    for c in word:
        if c.isalpha(): #如果明文的字符是字母的話
            if c.isupper():
                tmp = chr((ord(c) - 65 + key2[counter2]) % 26 + 65)
                translated.append(tmp)
            else:
                tmp = chr((ord(c) - 97 + key2[counter2]) % 26 + 97)
                translated.append(tmp)
            counter2 += 1
        else: #如果字符不是字母的話
            translated.append(c)
    return "".join(translated)

if __name__ == "__main__":
    main()