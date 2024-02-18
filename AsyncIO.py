import asyncio


async def main():
    print("Shivank")
    await show()


async def show():
    print("Show is called")


asyncio.run(main())
