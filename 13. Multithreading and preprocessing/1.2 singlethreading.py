## understanding multithreading

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)           # by this, im saying that for every execution, delay it by 1sec     (assume this as doing any i/o task or parallel task)
        print(f"Number {i}")

def print_alpha():
    for i in "abcde":
        print(f"alphabet {i}")
    

t = time.time()                        # getting current time
print_numbers()
print_alpha()
finished_t = time.time() - t           # getting time required to finish the task
print(finished_t)


# problem statement : 
#                     If print_numbers() is taking time to execute,in the meanwhile, i want atleast print_alpha() to do its work 