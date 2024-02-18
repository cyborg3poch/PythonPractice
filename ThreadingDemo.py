import threading
import time

start = time.perf_counter()


def do_something(second ):
    print(f"Sleeping for {second} sec")
    time.sleep(second)
    print("Done Sleeping")


# Creating threads
t1 = threading.Thread(target=do_something, args=[2])
t2 = threading.Thread(target=do_something, args=[2])

# staring the thread
t1.start()
t2.start()

# join means program will not proceed until thread is done running
t1.join()
t2.join()
finish = time.perf_counter()

print(f"Program finished in {round(finish - start, 2)} seconds")
