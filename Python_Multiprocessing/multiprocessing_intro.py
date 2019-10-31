import os
from multiprocessing import Process,current_process

def square(number):
    result = number*number
    # we can use the 'os' module in Python to print out the process ID assigned to the call of this function
    # assigned by the operating system
    process_ID = os.getpid()
    print(f"Process ID is:{process_ID}")

    # we can also use the 'current_process' function to get the name of the Process Object that is currently running
    # you can see os.getpid() gets us a random process it. Instead current_process().name gets us a number between 1 and n
    # where n is the total number of threads that we are using
    process_name = current_process().name
    print(f'Process name is:{process_name}')

    print(f"The number {number} squares to {result}.")
    print()

if __name__=='__main__':
    processes=[]
    numbers = [1,2,3,4]
    for number in numbers:
        process = Process(target=square,args=(number,))
        processes.append(process)

        process.start()