# Create a tuple
numbers = (10, 20, 30, 40, 50)

# Print the whole tuple
print("Tuple:", numbers)

# Print first element
print("First element:", numbers[0])

# Print last element
print("Last element:", numbers[-1])

# Find length of tuple
print("Length:", len(numbers))

# Find maximum value
print("Maximum:", max(numbers))

# Find minimum value
print("Minimum:", min(numbers))

# Find sum of all values
print("Sum:", sum(numbers))

# Find average
average = sum(numbers) / len(numbers)
print("Average:", average)

# Check if 30 exists in tuple
if 30 in numbers:
    print("30 is found")
else:
    print("30 is not found")

# Print all elements using loop
print("All elements:")
for item in numbers:
    print(item)

# Slice first 3 elements
print("First 3 elements:", numbers[:3])

# Slice last 2 elements
print("Last 2 elements:", numbers[-2:])

# Count how many times 20 appears
numbers2 = (10, 20, 30, 20, 40, 20)
print("Count of 20:", numbers2.count(20))

# Find index of 40
print("Index of 40:", numbers.index(40))

# Merge two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged = tuple1 + tuple2
print("Merged tuple:", merged)

# Repeat a tuple
print("Repeated tuple:", tuple1 * 2)

# Convert list to tuple
my_list = [7, 8, 9]
my_tuple = tuple(my_list)
print("List to tuple:", my_tuple)