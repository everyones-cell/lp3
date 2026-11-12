# Recursive and non-recursive Fibonacci
def fib_loop(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_rec(n):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

n = int(input("Enter n: "))
print("Non-recursive:", fib_loop(n))
print("Recursive:", fib_rec(n))

# Loop: Time O(n), Space O(1)
# Recursive: Time O(2^n), Space O(n)
