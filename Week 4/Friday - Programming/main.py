#==ACTIVITY 1==
def maths():
    a = 10
    b = 20
    print("a <= b:", a <= b) # 10 is less than or equal to 20
    print("b // a:", b // a) # 20 divided by 10 is 2
    print("b % a:", b % a) # 20 modulo 10 is 0
    print("a == b:", a == b) # 10 is not equal to 20
    print("b != a:", b != a) # 20 is not equal to 10
    a -= 15
    b *= 3
    print("a after -= 15:", a) # 10 - 15 = -5
    print("b after *= 3:", b) # 20 * 3 = 60
'''
STATE   STATE   AND OUTPUT
ON      ON      ON
ON      OFF     OFF
OFF     ON      OFF
OFF     OFF     OFF

STATE   STATE   OR OUTPUT
0       0       0
1       0       1
0       1       1
1       1       1

STATE  STATE   AND OUTPUT   OR OUTPUT
HIGH   HIGH    HIGH         HIGH
HIGH   LOW     LOW          HIGH
LOW    HIGH    LOW          HIGH
LOW    LOW     LOW          LOW

STATE   STATE   OR OUTPUT   NOT OUTPUT
+       +       +           -
+       -       +           -
-       +       +           +
-       -       -           +
'''

#==ACTIVITY 2==
def testing_is():
    data1=[10,20,30,40,50]
    data2=[17,22,43,40,1]
    data3=[10,20,30,40,50]

    print(data1 is data2)  # false
    print(data2 is data3)  # false

def testing_bitwise():
    k = 5  # In binary: 0101
    m = 2  # In binary: 0010
    print(f"k({k}) & m({m}): {k & m}")  # Bitwise AND
    print(f"k({k}) | m({m}): {k | m}")  # Bitwise OR
    print(f"k({k}) ^ m({m}): {k ^ m}")  # Bitwise XOR
    print(f"~k({k}): {~k}")        # Bitwise NOT
    print(f"k({k}) << 1: {k << 1}")  # Bitwise left shift
    print(f"k({k}) >> 1: {k >> 1}")  # Bitwise right shift

def testing_membership():
    Y = 10; z= 20
    mylist = [10, 2, 3, 4, 5 ]
    if Y in mylist:
        print("Y is in mylist")
    else:
        print("Y is not in mylist")
    if z in mylist:
        print("z is in mylist")
    else:
        print("z is not in mylist")

def main():
    maths()
    testing_is()
    testing_bitwise()
    testing_membership()

if __name__ == "__main__":
    main()