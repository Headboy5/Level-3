import time
from functools import wraps

def decoratorTimer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

    return wrapper

@decoratorTimer
def test():
    from main import Human
    john = Human("John", 30, "5'9\"", "70 kg")
    print(john.eat("apple", 0.5))
    print(john.sleep(8))
    print(john.exercise("running", 1))
    print(f"Name: {john.name}, Age: {john.age}, Height: {john.height}, Weight: {john.weight} kg")
    from main import main
    main()

test()