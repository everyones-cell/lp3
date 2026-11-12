# Fractional Knapsack - Greedy
n = int(input("Number of items: "))
items = []
for i in range(n):
    w, v = map(float, input("Enter weight and value: ").split())
    items.append((v / w, w, v))

capacity = float(input("Capacity: "))
items.sort(reverse=True)

total = 0
for ratio, weight, value in items:
    if capacity <= 0:
        break
    take = min(weight, capacity)
    total += take * ratio
    capacity -= take

print("Maximum value:", total)
