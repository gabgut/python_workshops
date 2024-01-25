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
    a = True
    b = False
    print(f"a and b: {a and b}")
    print(f"a or b: {a or b}")
    print(f"~a: {not a}")

    # Bitwise operators
    bin1 = 0b0110
    bin2 = 0b1100
    print(f"0110 & 1100: {bin(bin1 & bin2)} ({bin1 & bin2})")
    print(f"0110 | 1100: {bin(bin1 | bin2)} ({bin1 | bin2})")
    print(f"~0110: {bin(~bin1)} ({~bin1})")
    print(f"0110 ^ 1100: {bin(bin1 ^ bin2)} ({bin1 ^ bin2})")
    print(f">>")

    # Assigment operators


    # Identity operators


    # Memership operators

if __name__ == "__main__":
    main()