import multiprocessing
import qrcode
def square(x):
    return x * x

#Define the list of numbers to square
numbers = [1]
for i in range(2, 11000000):
    numbers.append(i)

def main():
    #Create a pool of worker processes
    with multiprocessing.Pool() as pool:
        #Map the square function to each number in parallel
        results = pool.map(square, numbers)
    print("Squared Numbers:", results)

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()