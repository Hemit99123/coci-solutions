limit = int(input())

counter = 0
total_sum = 0 

for row in range(limit + 1):
    # by adding this range which uses an ever increasing row, you can limiting the range of iterations by 1 each time 
    # this way not all combinations are accounted for just the ones that are needed (i.e 8,2 wouldnt be accounted for because 2,8 would have added that sum)
    
    for column in range(row, limit + 1):
        total_sum += row + column

print(total_sum)
