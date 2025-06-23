numbers = [10, 5, 3, 8, 2]

smallest = min(numbers)

print("Smallest number is:", smallest)


numbers = [10, 5, 3, 8, 2]

# Remove the largest number first
max_num = max(numbers)
numbers.remove(max_num)

# Now find the new max (second largest)
second_greatest = max(numbers)

print("Second greatest number is:", second_greatest)


numbers = [10, 5, 3, 8, 2]

# Remove the smallest number first
min_num = min(numbers)
numbers.remove(min_num)

# Now find the new min (second smallest)
second_smallest = min(numbers)

print("Second smallest number is:", second_smallest)



