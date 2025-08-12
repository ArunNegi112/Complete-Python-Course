from concurrent.futures import ProcessPoolExecutor
import time

def squre(n):
    time.sleep(2)
    return f"square of {n} is {n*n}"


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
if __name__=="__main__" : #this gives starting point to the computer for execution
    t = time.time()

    with ProcessPoolExecutor(max_workers=4) as executor:    # max_worker = 4 -> using 4 cores of CPU
        results = executor.map(squre, numbers)

    for result in results:
        print(result)
    final_t = time.time() - t
    print(final_t)
    
