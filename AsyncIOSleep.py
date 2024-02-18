import asyncio
import time


async def say_something(delay, words):
    print(f"Before {words}")
    await asyncio.sleep(delay)
    print(f"After {words}")


async def main():
    start = time.perf_counter()
    # await say_something(1, "Task 1")
    # await say_something(2, "Task 2")

    task1 = asyncio.create_task(say_something(1, "Task 1"))
    task2 = asyncio.create_task(say_something(2, "Task 2"))
    finish = time.perf_counter()

    print(f"Program finished in {round(finish - start, 2)} seconds")

asyncio.run(main())