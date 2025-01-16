## understanding multithreading

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)           
        print(f"Number {i}")

def print_alpha():
    for i in "abcde":
        print(f"alphabet {i}")
    

## Creating threads 
thread1 = threading.Thread(target = print_numbers)   # inside 'target' we assign our function
thread2 = threading.Thread(target = print_alpha)


t = time.time()                        

## start the threads
thread1.start()
thread2.start()

## join the threads with main thread (synchronization)
thread1.join()
thread2.join()
## why .join() ? 
#  when executing a process, one thread becomes the main thread (here 'time'), and with the help of join() we wait for threads to complete their execution and get in sync with main thread 

## see that, without this join(), if we execute the program, finished_t = 0.00s 



finished_t = time.time() - t          
print(finished_t)
