# Principiumx Sr. Back-End Developer Hiring Test through HACKER_RANK

def foo(value):
    while True:
        value = (yield value)

bar = foo(1)
print(next(bar))
print(next(bar))
print(bar.send(2))

def dec1(func):
    def wrapper(*args, **kwargs):
        print("Entering dec1")
        result = func(*args, **kwargs)
        print("Exiting dec1")
        return result
    return wrapper

def dec2(func):
    def wrapper(*args, **kwargs):
        print("Entering dec2")
        result = func(*args, **kwargs)
        print("Exiting dec2")
        return result
    return wrapper

@dec1
@dec2
def greet(message):
    print(message)

greet("Hello World")


# Question 3:
class Meta(type):

    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        return x

class MyClass(metaclass=Meta):
    pass

print(MyClass.attr)

# Q4

# what will the function do?
def foo(a, b, c): pass

# defines an empty class foo
# defines a list foo
# defines a function, which does nothing
# none of the above

# Q5
b = [0,1,2,3,4,5,6,7,8,9]
print(b[::3])

# Q6
# what error message do you get when executing:
# hello = world

# Q7

# A script that makes use of python's asyncio to handle concurrent tasks
# is under development. It has three asynchronous functions named 
# task1(), task2(), task3()

import asyncio

async def task1():
    await asyncio.sleep(1)
    print('Task1 completed')
    return 'task1'

async def task2():
    await asyncio.sleep(2)
    print('Task2 completed')
    return 'task2'

async def task3():
    await asyncio.sleep(3)
    print('Task3 completed')
    return 'task3'

# These tasks must run such that task2() waits for task1() to complete,
# and task3() waits for both task1() and task2() to complete. If any
# the tasks fail, the other tasks should be canceled. Which of the
# following code snippets achieves this?

# ANSWER:

async def main():
    try:
        # Ensure task2 waits for task1, and task3 waits for both task1 and task2
        result1 = await task1()  # Wait for task1 to complete
        result2 = await task2()  # Wait for task2 to complete after task1
        result3 = await task3()  # Wait for task3 to complete after task1 and task2
        print(result1, result2, result3)
    except Exception as e:
        print(f"An error occurred: {e}")

asyncio.run(main())
