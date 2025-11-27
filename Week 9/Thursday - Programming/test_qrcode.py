import qrcode
from pathlib import Path
from faker import Faker
import pyshorteners
import pyshorteners.shorteners
import pyshorteners.shorteners.tinyurl
import psutil

from termcolor import colored, cprint
def test_qrcode():
    data = "Welcome to Leeds Trinity University"
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(data)
    qr.make(fit = True)
    img = qr.make_image(fill_color = 'red', back_color = 'black')
    save_dir = Path(__file__).parent
    img.save(save_dir / "qrcode.png")

def test_faker():
    fake =Faker("en_GB")
    name = fake.name()
    address = fake.address()
    email = fake.email()
    print(f"Name: {name}\nAddress: {address}\nEmail: {email}")

def test_url_shortener():
    url = "https://www.leedstrinity.ac.uk/"
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(url)
    print(f"Original URL: {url}\nShortened URL: {short_url}")

def test_colored_print():
    cprint("This is a red text on yellow background", 'red', 'on_yellow')
    cprint("This is a green text", 'green')
    cprint("This is a blue text with underline", 'blue', attrs=['underline'])

def add_two_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return None
    return a + b

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

def main():
    test_qrcode()
    test_faker()
    test_url_shortener()
    test_colored_print()
    print(f"The sum of the two numbers is: {add_two_numbers()}")
    print_cpu_info()
    print_memory_info()

if __name__ == "__main__":
    main()
    input("Press Enter to exit...")