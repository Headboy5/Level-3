def test_random():
    # Go to the python random library pick three method of your choice and write a python code of how to use them.
    import random

    # Using random.choice()
    fruits = ['apple', 'banana', 'cherry', 'date']
    selected_fruit = random.choice(fruits)
    print(f"Randomly selected fruit: {selected_fruit}")

    # Using random.sample()
    numbers = list(range(1, 11))
    sampled_numbers = random.sample(numbers, 3)
    print(f"Randomly sampled numbers: {sampled_numbers}")

    # Using random.randint()
    random_integer = random.randint(1, 100)
    print(f"Randomly selected integer: {random_integer}")

def test_regex():
    # Give example of \A and \Z from the regex library
    import re
    text = "Hello, and welcome to the world of Python programming. My name is Gustavo, but you can call me Gus."
    # Using \A to match the start of the string
    match_start = re.search(r'\AHello', text)
    if match_start:
        print("The string starts with 'Hello'")
    else:
        print("The string does not start with 'Hello'")
    # Using \Z to match the end of the string
    match_end = re.search(r'programming\.\Z', text)
    if match_end:
        print("The string ends with 'programming.'")
    else:
        print("The string does not end with 'programming.'")
    # Go to the RE library, pick these methods (sub, finditer, compile and fullmatch) and give example of how they are used in python development.
    # Using re.sub()
    new_text = re.sub(r'Python', 'Java', text)
    print(f"After substitution: {new_text}")
    # Using re.finditer()
    matches = re.finditer(r'\b\w{6}\b', text)
    # find all 6-letter words
    for match in matches:
        print(f"Found match: {match.group()} at position {match.start()}")
    # Using re.compile()
    five_char = re.compile(r'\b\w{5}\b')
    compiled_matches = five_char.finditer(text)
    for match in compiled_matches:
        print(f"Found compiled match: {match.group()} at position {match.start()}")
    # Using re.fullmatch()
    full_match = re.fullmatch(fr'Hello, and welcome to the world of Python programming. My name is Gustavo, but you can call me Gus.', text)
    if full_match:
        print("The entire string matches the pattern.")
    else:
        print("The entire string does not match the pattern.")

def test_datetime():
    from datetime import datetime

    now = datetime.now()
    print(now)

    # 2024-02-03 15:17:17.979151

    # Try and run this:
    print(f"Year: {now.year}")
    print(f"Month: {now.month}")
    print(f"Day: {now.day}")
    print(f"Hour: {now.hour}")
    print(f"Minute: {now.minute}")
    print(f"Second: {now.second}")
    # Create a date object for your birthday.
    birthday = datetime(2007, 3, 20)  # Replace with your actual birth date

    # What day of the week was your day of birth?
    print(f"You were born on a {birthday.strftime('%A')}.")

    # When will you be 1 year older? Hint(timedelta)
    from dateutil.relativedelta import relativedelta
    now = datetime.now()
    one_year_later = now + relativedelta(years=1)
    print(f"You will be 1 year older on {one_year_later}.")

def main():
    test_random()
    test_regex()
    test_datetime()

if __name__ == "__main__":
    main()