limit = int(input())

counter = 0
total_sum = 0  # Renamed to avoid overwriting the built-in sum function

for row in range(limit + 1):
    for column in range(row, limit + 1):
        total_sum += row + column

print(total_sum)