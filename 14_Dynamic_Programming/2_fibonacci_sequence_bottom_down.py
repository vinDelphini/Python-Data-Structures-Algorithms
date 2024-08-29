counter = 0

def fib(n):
    global counter
    fib_list = [0, 1]

    for i in range(2, n + 1):
        counter += 1
        next_fib = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(next_fib)
    return fib_list[n]

print(fib(35))
print(counter)
