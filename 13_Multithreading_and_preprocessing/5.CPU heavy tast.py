import multiprocessing
import time
import sys  #system
import math

# allowing limit so that system allows such a heavy calculation, (default limit = 4300 digits)
sys.set_int_max_str_digits(100000)  # set max number of digits an integer can have

def factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    t = time.time()
    lst = [1000,4000]
    # creating pool of processes
    with multiprocessing.Pool() as pool:  # since i've not explcitly mentioned 'processes' its set to max number of core available in my system
        results = pool.map(factorial,lst)

    for result in results:
        print(result)
    final_t = time.time() - t
    print(f"Total time = {final_t}")
