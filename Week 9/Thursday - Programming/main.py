import multiprocessing
import qrcode
import psutil
def square(x):
    return x * x

def print_cpu_info():
    print(f"My cpu times {psutil.cpu_times()}")
    print(f"My cpu counts {psutil.cpu_count()}")
    print(f"Idle cpu counts {psutil.cpu_count(logical=False)}") #Number of idle CPU 
    print(f"My cpu stats {psutil.cpu_stats()}") #CPU usage
    print(f"My cpu freq {psutil.cpu_freq()}")
    print(f"My cpu load {psutil.getloadavg()}") #avg system load over time

def print_memory_info():
    vm = psutil.virtual_memory()
    swap = psutil.swap_memory()
    print(f"RAM memory % used: {vm.percent}")
    print(f"Available virtual memory: {vm.available}")
    print(f"My total virtual memory: {vm.total}")
    print(f"My virtual memory in kilobyte: {vm.total / 1024:.2f}")
    print(f"My virtual memory in megabyte: {vm.total / (1024 ** 2):.2f}")
    print(f"My virtual memory in gigabyte: {vm.total / (1024 ** 3):.2f}")
    print(f"Swap memory: {swap}")

def make_numbers_list():
    #Define the list of numbers to square
    numbers = [1]
    for i in range(2, 11000000):
        numbers.append(i)
    return numbers

def multiprocessing_square(numbers):
    #Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        #Map the square function to each number in parallel
        results = pool.map(square, numbers)
    print("Squared Numbers:", results)

def main():
    print_cpu_info()
    print_memory_info()
    # numbers = make_numbers_list()
    # multiprocessing_square(numbers)


if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()