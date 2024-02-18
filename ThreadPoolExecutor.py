import concurrent.futures
import time

start = time.perf_counter()


def do_something(second ):
    print(f"Sleeping for {second} sec")
    time.sleep(second)
    return "Done Sleeping"


# With thread Pool Executor we don't have to "join the thread" -> wait for completion explicitly
with concurrent.futures.ThreadPoolExecutor() as executor :
    f1 = executor.submit(do_something , 2)
    f2 = executor.submit(do_something, 2)

    print(f1.result())
    print(f2.result())


finish = time.perf_counter()

print(f"Program finished in {round(finish - start, 2)} seconds")