# Asynchronous vs. Synchronous
- Sync => run 1 task at a time
- Async => run multiple tasks at the same time (non-linear)

# Subroutines vs. Coroutines
1. Subroutine => block of code called **"as needed"**
        * main thread => control to subroutine => main thread
        * can't be paused and resumed => they run until `done`
        * definition: subset of a larger program
2. Coroutine => executions can be **paused and resumed**
        * Maintain their `state` between pauses
        * Works well for tasks that need to `wait` for something:
            * I/O operations
            * Database Queries
            * HTTP Requests
        * definition: runs cooperatively with another program -> `async programming`


# Concurrency vs. Parallelism
1. Concurrency
    * Start and stop times of multiple coroutines can overlap.
2. Parallelism
    * Different threads can execute simultaneously.

# Async and Await
- `async` allows faster run time and allows every function to run at same time regardless of time. 
- `await` can only be used with commands that are `awaitable`
- Example:
        * `time.sleep(3)` is not "awaitable"
        * however, `asyncio.sleep(3)` is "awaitable"

# Coroutine call options - batch vs. individual (create tasks)
1. Batch
    * `asyncio.gather()` allows you to group coroutines for simultaneous execution as a "batch".
    * Example batch call:
        `batch = asyncio.gather(brewCoffee(), toastBagel())`
        `result_coffee, result_bagel = await batch`
    * The downside of this is you need to wait for the batch call to finish.
    * Can only use `await` if a function is `async`
    * To call this function you need to use `asyncio.run()`
2. Individual (create task)
    * Creates a task out of each coroutine.
    * Use `asyncio.create_task()`
    * Example create task call:
        `coffee_task = asyncio.create_task(brewCoffee())`
        `toast_task = asyncio.create_task(toastBagel())`
    * Then `await` each coroutine response individually:
        `result_coffee = await coffee_task`
        `result_bagel = await toast_task`



# Summary
* Batch vs. Individual processing depends on your use case(s).