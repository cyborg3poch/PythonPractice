import concurrent.futures
import time

start = time.perf_counter()


def do_something(second ):
    print(f"Sleeping for {second} sec")
    time.sleep(second)
    return f"Done Sleeping for {second} sec"


# With thread Pool Executor we don't have to "join the thread" -> wait for completion explicitly
with concurrent.futures.ThreadPoolExecutor() as executor :
    secs = [5,4,3,2,1]
    # results = executor.map(do_something,secs) --> prints in order or execution

    # prints in order of starting 
    results = [executor.submit(do_something , sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())

finish = time.perf_counter()

print(f"Program finished in {round(finish - start, 2)} seconds")