# Normal and multithreaded matrix multiplication (one thread per row)
import threading
import time

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
n = len(A)
C = [[0] * n for _ in range(n)]

def multiply_row(i):
    for j in range(n):
        C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))

start = time.time()
normal = [[sum(A[i][k] * B[k][j] for k in range(n))
           for j in range(n)] for i in range(n)]
normal_time = time.time() - start

start = time.time()
threads = [threading.Thread(target=multiply_row, args=(i,)) for i in range(n)]
for t in threads:
    t.start()
for t in threads:
    t.join()
thread_time = time.time() - start

print("Normal result:", normal)
print("Threaded result:", C)
print("Normal time:", normal_time)
print("Threaded time:", thread_time)
# Small matrices may be slower with threads due to thread overhead.
