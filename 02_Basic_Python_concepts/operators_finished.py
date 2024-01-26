"""

Exmple file of operators

"""

def main():
    # Arithmetic operators
    add = 3 + 2
    print(add)
    
    sub = 4 - 2
    print(sub)

    mul = 2 * 2
    print(mul)

    div0 = 3 / 2
    print(div0)

    div1 = 3 // 2
    print(div1)

    mod = 10 % 5
    print(mod)

    pow = 3 ** 2
    print(pow)

    # Comparison operators
    print(f"5 > 3: {5 > 3}")
    print(f"5 < 3: {5 < 3}")
    print(f"5 >= 3: {5 >= 3}")
    print(f"5 <= 5: {5 <= 5}")
    print(f"5 == 5: {5 == 5}")
    print(f"5 != 3: {5 != 3}")

    # Logical operators
    a, b = True, False
    print(f"a and b: {a and b}")
    print(f"a or b: {a or b}")
    print(f"~a: {not a}")

    # Bitwise operators
    bin1, bin2 = 0b0110, 0b1100
    print(f"0110 & 1100: {bin(bin1 & bin2)} ({bin1 & bin2})")
    print(f"0110 | 1100: {bin(bin1 | bin2)} ({bin1 | bin2})")
    print(f"~0110: {bin(~bin1)} ({~bin1})")
    print(f"0110 ^ 1100: {bin(bin1 ^ bin2)} ({bin1 ^ bin2})")
    print(f"0110 >> 1: {bin(bin1 >> 1)} ({bin1 >> 1})")
    print(f"1100 << 1: {bin(bin2 << 1)} ({bin2 << 1})")

    # Assigment operators
    num = 20
    print(f"num = 20: {num}")
    num += 10
    print(f"num += 10: {num}")
    num -= 5
    print(f"num -= 5: {num}")
    num *= 4
    print(f"num *= 4: {num}")
    num /= 2
    print(f"num /= 2: {num}")
    num //= 2
    print(f"num //= 2: {num}")
    num %= 3
    print(f"num %= 2: {num}")
    num = int(num)
    num <<= 3
    print(f"num >>= 3: {num}")
    num >>= 1
    print(f"num >>= 1: {num}")
    num **= 2
    print(f"num **= 2: {num}")
    num &= 16
    print(f"num &= 16: {num}")
    num |= 12
    print(f"num |= 12: {num}")
    num ^= 10
    print(f"num ^= 10: {num}")

    # Identity operators
    a, b = 10, 20
    print(a is b)
    print(a is not b)

    # Memership operators
    list = [i for i in range(10)]
    print(list)

    if (10 not in list):
        print("10 is NOT present in given list")
    else:
        print("10 is present in the given list")

    if (5 in list):
        print("5 is present in given list")
    else:
        print("5 is NOT present in given list")

if __name__ == "__main__":
    main()