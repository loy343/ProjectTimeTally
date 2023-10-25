numbers = list(range(1, 31))

# Find the index where 16 is located
split_index = numbers.index(16)

# Split the list into two parts
first_half = numbers[:split_index]
second_half = numbers[split_index:]

print("First Half:", first_half)
print("Second Half:", second_half)