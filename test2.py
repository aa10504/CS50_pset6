import cs50

def main():
    p = cs50.get_string()
    c = cipher(p)
    print("before: {}, after: {}".format(p, c))

def cipher(word):
    tmp = None
    for i in range(len(word)):
        if i == 0:
            tmp = chr(ord(word[i]) + 1) # ord(character)轉換成ASCii數字
        else:
            tmp = tmp + chr(ord(word[i]) + 1)
    return tmp
if __name__ == "__main__":
    main()