# 0/1 Knapsack using Dynamic Programming
n = int(input("Number of items: "))
weights, values = [], []
for i in range(n):
    w, v = map(int, input("Enter weight and value: ").split())
    weights.append(w)
    values.append(v)

capacity = int(input("Capacity: "))
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for c in range(capacity + 1):
        dp[i][c] = dp[i-1][c]
        if weights[i-1] <= c:
            dp[i][c] = max(dp[i][c],
                           values[i-1] + dp[i-1][c-weights[i-1]])

print("Maximum value:", dp[n][capacity])
# Time O(nW), Space O(nW)
