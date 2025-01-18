from concurrent.futures import ThreadPoolExecutor
import time

def print_number(n):
    time.sleep(2)
    return f"Number ={n}"

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
t = time.time()

with ThreadPoolExecutor(max_workers=3) as executors:    # By using ThreadPoolExecutor we are giving max_worker = 3 i.e creating 3 threads to execute code in this block, 
    results = executors.map(print_number,numbers)       # 3 threads with working on 3 numbers, i.e 1,2,3 one thread assigned for each after one thread completes its execution '4' goes to that thread.

for result in results:
    print(result)
final_t = time.time() - t
print(final_t)

# with this, even though the code sleeps for 1sec during each execution, we are still able to get out so quickly