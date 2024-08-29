counter = 0
def fibonacci(n):
    global counter 
    counter += 1
    if n == 0 or n == 1:
        return n
    return fibonacci(n- 1) + fibonacci(n - 2)
    
print(fibonacci(35))
print(counter)

# Output:
# 9227465
# 29860703


# Memoization

memo = [None] * 100
count = 0

def fib(n):
    global count
    count += 1
    if memo[n]:
        return memo[n]
    
    if n == 0 or n == 1:
        return n
    
    memo[n] = fib(n - 1) + fib(n - 2)
    
    return memo[n]

print(fib(35))
print(count)

# Output:
# 9227465
# 69
