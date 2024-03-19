# create 2 functions
import asyncio
import time

# function 1 - sleep function used to simulate command that takes 3 seconds to execute
async def brewCoffee():
    print("Start brewCoffee()")
    await asyncio.sleep(3)
    print("End brewCoffee()")
    return "Coffee ready"

# function 2 - sleep function used to simulate command that takes 2 seconds to execute
async def toastBagel():
    print("Start toastBagel()")
    await asyncio.sleep(2)
    print("End toastBagel()")
    return "Bagel toasted"


# main function for start and stop time experiment
async def main():
    # start time
    start_time = time.time()

    # batch call example
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # result_coffee, result_bagel = await batch

    # create task method
    coffee_task = asyncio.create_task(brewCoffee())
    toast_task = asyncio.create_task(toastBagel())
    # then await each coroutine individually
    result_coffee = await coffee_task
    result_bagel = await toast_task

    # standard function calls
    #result_coffee = brewCoffee()
    #result_bagel = toastBagel()
    # end time
    end_time = time.time()
    # elapsed time
    elapsed_time = end_time - start_time

    # print results
    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBagel: {result_bagel}")
    print(f"Total time elapsed: {elapsed_time:.2f} seconds")

# call main function
if __name__ == "__main__":
    asyncio.run(main())