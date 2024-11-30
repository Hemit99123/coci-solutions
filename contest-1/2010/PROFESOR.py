# Input number of pairs
n = int(input(""))

# Dictionary to store frequencies
freq_dict = {}

# Input n pairs of numbers
for _ in range(n):
    x, y = map(int, input().split())
    
    # Increment the frequency of both numbers
    if x not in freq_dict:
        freq_dict[x] = 0
    if y not in freq_dict:
        freq_dict[y] = 0
    
    freq_dict[x] += 1
    freq_dict[y] += 1

# Find the number with the highest frequency
number = None
max_frequency = 0

for num, freq in freq_dict.items():
    if freq > max_frequency or (freq == max_frequency and num < number):
        number = num
        max_frequency = freq

# Output the result

# Here we are checking if we can add everyone to a desk
# Since a desk can only have 2 per desk, if we have an uneven amount
# It means a student must be kicked out so the number becomes even again

if (max_frequency % 2 == 1 and max_frequency != 1):
    max_frequency -= 1
    
print(max_frequency, number)
