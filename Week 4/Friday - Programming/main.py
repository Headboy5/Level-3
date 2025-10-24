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

def main():
    maths()

if __name__ == "__main__":
    main()