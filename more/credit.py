import cs50

def main():
    print("Number: ",end="")
    ccnumber = cs50.get_int()
    if ith_digit(ccnumber, 1) == 3:
        if ith_digit(ccnumber, 2) == 4 or ith_digit(ccnumber, 2) == 7:
            m = 0
            n = 0

            i = 2
            while i < 15:
                k = ith_digit(ccnumber, i)
                k2 = k * 2
                str_k2 = str(k2)
                x = 0
                y = 0
                if len(str_k2) == 1:
                    x = ith_digit(k2, 1)
                else:
                    x = ith_digit(k2, 1)
                    y = ith_digit(k2, 2)
                m = m + x + y
                i += 2

            j = 1
            while j < 16:
                k = ith_digit(ccnumber, j)
                n = n + k
                j += 2

            key = (m + n) % 10

            if key == 0:
                print("AMEX")
            else:
                print("INVALID")

    elif ith_digit(ccnumber, 1) == 5:
        if ith_digit(ccnumber, 2) == 1 or ith_digit(ccnumber, 2) == 2 or ith_digit(ccnumber, 2) == 3 or ith_digit(ccnumber, 2) == 4 or ith_digit(ccnumber, 2) == 5:
            print("MASTERCARD")
    elif ith_digit(ccnumber, 1) == 4:
        if len(str(ccnumber)) == 13 or len(str(ccnumber)) == 16:
            print("VISA")
    else:
        print("INVALID")

def ith_digit(number, i):
    s = str(number)
    n = int(s[i - 1])
    return n

if __name__ == "__main__":
    main()