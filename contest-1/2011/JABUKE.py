position = input().split()

n = int(position[0])  # Total number of columns
m = int(position[1])  # Width of the boat

j = int(input())  # Number of apples

fallen_apples = []

# Initial boat position: leftmost M columns (0 to M-1)
current_boat_pos = 0
movement = 0

# Input positions of fallen apples
for _ in range(j):
    apple_pos = int(input())
    fallen_apples.append(apple_pos)

# Process each fallen apple
for pos in fallen_apples:
    # If the apple falls outside the current boat's range
    if pos < current_boat_pos or pos >= current_boat_pos + m:
        # Move the boat to the best possible position that minimizes the movement
        # Find the closest column where the boat can fully cover the apple
        new_pos = max(0, min(pos, n - m))  # New position must stay within bounds of the screen
        movement += abs(new_pos - current_boat_pos)  # Calculate distance moved
        current_boat_pos = new_pos  # Update the boat's position

print(movement + 1)
