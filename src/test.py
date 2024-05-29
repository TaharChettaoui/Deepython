from multiprocessing import Process 
import os
import time

def square_aaa():
    print("start")
    for i in range(100):
        i * i
        time.sleep(0.1)

processes = []
num_processes = os.cpu_count()

if __name__ == '__main__':
    # create processes
    for i in range(num_processes):
        p = Process(target=square_aaa)
        processes.append(p)
    
    # start
    for p in processes:
        p.start()
        
    # join
    for p in processes:
        p.join()

    print("End Main")