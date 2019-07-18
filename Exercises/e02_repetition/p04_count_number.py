# 1~1000에서 각 숫자의 개수
counts = [0] * 10

for i in range(1, 10):
    counts[i] += 1
for i in range(10, 100):
    counts[i // 10] += 1
    counts[i % 10] += 1
for i in range(100, 1000):
    counts[i // 100] += 1
    counts[(i % 100) // 10] += 1
    counts[i % 10] += 1
for i in range(1000, 1001):
    counts[i // 1000] += 1
    counts[(i % 1000) // 100] += 1
    counts[(i % 100) // 10] += 1
    counts[i % 10] += 1

print(counts)
