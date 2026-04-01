# Create a set
numbers = {10, 20, 30, 40, 50}

# Print the whole set
print("Set:", numbers)

# Find length of set
print("Length:", len(numbers))

# Add one element
numbers.add(60)
print("After adding 60:", numbers)

# Remove one element
numbers.remove(20)
print("After removing 20:", numbers)

# Check if a value exists
if 30 in numbers:
    print("30 is found")
else:
    print("30 is not found")

# Create another set
numbers2 = {40, 50, 60, 70, 80}

# Union of two sets
print("Union:", numbers.union(numbers2))

# Intersection of two sets
print("Intersection:", numbers.intersection(numbers2))

# Difference of two sets
print("Difference:", numbers.difference(numbers2))

# Symmetric difference
print("Symmetric Difference:", numbers.symmetric_difference(numbers2))

# Remove duplicates from a list using set
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(my_list)
print("Unique values from list:", unique_values)

# Loop through a set
print("Elements in set:")
for item in numbers:
    print(item)

# Clear all elements
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear:", temp_set)

# Find maximum and minimum
values = {5, 10, 15, 20}
print("Maximum:", max(values))
print("Minimum:", min(values))

# Find sum
print("Sum:", sum(values))