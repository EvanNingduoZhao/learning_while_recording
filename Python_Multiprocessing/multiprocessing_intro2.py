import os
import time
from multiprocessing import Process,current_process

def square(number):

    for number in numbers:
        result = number*number
        time.sleep(0.5)

        print(f"The number {number} squares to {result}.")
        print()

if __name__=='__main__':
    processes=[]
    numbers = range(100)
    for i in range(50 ):
        process = Process(target=square,args=(numbers,))
        processes.append(process)

        process.start()

    # use the join function to make sure that all the processes are completed before we move on
    for process in processes:
        process.join()
    print('Multiprocess Complete')