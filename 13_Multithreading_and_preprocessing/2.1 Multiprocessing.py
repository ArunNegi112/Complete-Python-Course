## understanding multiprocessing

import multiprocessing
import multiprocessing.process
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)           
        print(f"Number {i}")

def print_alpha():
    for i in "abcde":
        time.sleep(2)
        print(f"alphabet {i}")
    

if __name__ == "__main__" :     
# This block tells the system to start executing the file from here
    ## Creating processes 
    p1 = multiprocessing.Process(target = print_numbers)   # inside 'target' we assign our function
    p2 = multiprocessing.Process(target = print_alpha)


    t = time.time()                        

    ## start the process
    p1.start()
    p2.start()

    ## join the processes with main process (synchronization)
    p1.join()
    p2.join()
    ## why .join() ? 
    #  Even though processes run in parallel (unlike threads that share the same memory), the main process still needs to coordinate their completion.
    #  Without join(), you may encounter unpredictable behavior if the main process exits before child processes complete.

    ## see that, without this join(), if we execute the program, finished_t = 0.00s

    finished_t = time.time() - t          
    print(finished_t)


# Even though this looks same as multithreading, the execution and memory allocation by computer is different