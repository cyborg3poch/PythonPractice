import multiprocessing
import time

start = time.perf_counter()


def do_something():
    print(f"Sleeping for 1 sec")
    time.sleep(1)
    print("Done Sleeping")


# Creating Processes
p1 = multiprocessing.Process(target=do_something)
p2 = multiprocessing.Process(target=do_something)

# https://stackoverflow.com/questions/18204782/runtimeerror-on-windows-trying-python-multiprocessing
if __name__ == "__main__":
    # staring the Processes
    p1.start()
    p2.start()

    # join means program will not proceed until Processes is done running
    p1.join()
    p2.join()
    finish = time.perf_counter()

    print(f"Program finished in {round(finish - start, 2)} seconds")



