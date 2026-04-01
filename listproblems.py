# 1. Create and print a list
numbers = [10, 20, 30, 40, 50]
print("1.", numbers)

# 2. Print the first element
print("2.", numbers[0])

# 3. Print the last element
print("3.", numbers[-1])

# 4. Find the length of a list
print("4.", len(numbers))

# 5. Add an element at the end
numbers1 = [10, 20, 30]
numbers1.append(40)
print("5.", numbers1)

# 6. Add an element at a specific position
numbers2 = [10, 20, 30]
numbers2.insert(1, 15)
print("6.", numbers2)

# 7. Remove an element
numbers3 = [10, 20, 30, 40]
numbers3.remove(30)
print("7.", numbers3)

# 8. Remove the last element
numbers4 = [10, 20, 30, 40]
numbers4.pop()
print("8.", numbers4)

# 9. Print all elements using a loop
numbers5 = [10, 20, 30, 40, 50]
print("9.")
for item in numbers5:
    print(item)

# 10. Find the sum of all elements
numbers6 = [10, 20, 30, 40, 50]
print("10.", sum(numbers6))

# 11. Find the maximum number
print("11.", max(numbers6))

# 12. Find the minimum number
print("12.", min(numbers6))

# 13. Find the average of list elements
average = sum(numbers6) / len(numbers6)
print("13.", average)

# 14. Check if an item exists in the list
print("14.")
if 30 in numbers6:
    print("Found")
else:
    print("Not Found")

# 15. Count how many times a value appears
numbers7 = [10, 20, 10, 30, 10, 40]
print("15.", numbers7.count(10))

# 16. Sort the list in ascending order
numbers8 = [40, 10, 30, 20, 50]
numbers8.sort()
print("16.", numbers8)

# 17. Sort the list in descending order
numbers9 = [40, 10, 30, 20, 50]
numbers9.sort(reverse=True)
print("17.", numbers9)

# 18. Reverse the list
numbers10 = [10, 20, 30, 40, 50]
numbers10.reverse()
print("18.", numbers10)

# 19. Copy a list
numbers11 = [10, 20, 30, 40]
new_list = numbers11.copy()
print("19.", new_list)

# 20. Merge two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged = list1 + list2
print("20.", merged)

# 21. Find even numbers in a list
numbers12 = [1, 2, 3, 4, 5, 6]
print("21.")
for item in numbers12:
    if item % 2 == 0:
        print(item)

# 22. Find odd numbers in a list
print("22.")
for item in numbers12:
    if item % 2 != 0:
        print(item)

# 23. Create a list of squares
numbers13 = [1, 2, 3, 4, 5]
squares = []
for item in numbers13:
    squares.append(item * item)
print("23.", squares)

# 24. Find the second largest number
numbers14 = [10, 40, 20, 50, 30]
numbers14.sort()
print("24.", numbers14[-2])

# 25. Remove duplicates from a list
numbers15 = [10, 20, 10, 30, 20, 40]
unique_numbers = []
for item in numbers15:
    if item not in unique_numbers:
        unique_numbers.append(item)
print("25.", unique_numbers)

# 26. Find common elements in two lists
list3 = [1, 2, 3, 4]
list4 = [3, 4, 5, 6]
print("26.")
for item in list3:
    if item in list4:
        print(item)

# 27. Find elements present in first list but not in second
print("27.")
for item in list3:
    if item not in list4:
        print(item)

# 28. Replace an element in a list
numbers16 = [10, 20, 30, 40]
numbers16[2] = 35
print("28.", numbers16)

# 29. Clear all elements from a list
numbers17 = [10, 20, 30, 40]
numbers17.clear()
print("29.", numbers17)

# 30. Create a list manually
numbers18 = [5, 15, 25, 35, 45]
print("30.", numbers18)

# 31. Find positive and negative numbers
numbers19 = [10, -5, 7, -2, 0, 8, -1]
print("31.")
for item in numbers19:
    if item > 0:
        print("Positive:", item)
    elif item < 0:
        print("Negative:", item)
    else:
        print("Zero:", item)

# 32. Multiply all numbers in a list
numbers20 = [1, 2, 3, 4]
result = 1
for item in numbers20:
    result = result * item
print("32.", result)

# 33. Find the smallest string in a list
words1 = ["apple", "kiwi", "banana", "fig"]
smallest = words1[0]
for word in words1:
    if len(word) < len(smallest):
        smallest = word
print("33.", smallest)

# 34. Find the longest string in a list
longest = words1[0]
for word in words1:
    if len(word) > len(longest):
        longest = word
print("34.", longest)

# 35. Convert all names to uppercase
names = ["ali", "sara", "john"]
upper_names = []
for name in names:
    upper_names.append(name.upper())
print("35.", upper_names)

# 36. Print list elements with index
numbers21 = [10, 20, 30, 40]
print("36.")
for i in range(len(numbers21)):
    print("Index:", i, "Value:", numbers21[i])

# 37. Find the index of a value
numbers22 = [10, 20, 30, 40]
print("37.", numbers22.index(30))

# 38. Slice the first three elements
numbers23 = [10, 20, 30, 40, 50]
print("38.", numbers23[:3])

# 39. Slice the last three elements
print("39.", numbers23[-3:])

# 40. Reverse a list using slicing
print("40.", numbers23[::-1])