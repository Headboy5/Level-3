count = 1

while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    print(number)
    if number % 2 == 0:
        continue
    print(number, "squared is", number * number)
    count += 1