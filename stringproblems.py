# 1. Count vowels and consonants in a string
def counts_vowels_consonants(s):  # Define a function that takes a string s
    vowels = 'aeiouAEIOU'  # Store all uppercase and lowercase vowels
    vowels_count = sum(1 for char in s if char in vowels)  # Count how many characters in s are vowels
    consonants_count = sum(1 for char in s if char.isalpha() and char not in vowels)  # Count how many letters are consonants
    return vowels_count, consonants_count  # Return both counts

string = input("Enter the string: ")  
vowels, consonants = counts_vowels_consonants(string)  # Call the function and store the returned values
print("Number of vowels:", vowels)  # Print the number of vowels
print("Number of consonants:", consonants)  # Print the number of consonants

#2. Remove all vowels from a string
def remove_vowels(s):
    vowels = 'aeiouAEIOU'  # Store all uppercase and lowercase vowels
    result = ''.join(char for char in s if char not in vowels) #Create a new string that includes only chareacters that are not vowels
    return result
string = input ("Enter the string:")
print("String after removing vowels is ", remove_vowels(string))

#3. Check if two strings are anagrams
s1 = input("Enter first string: ").replace(" ", "").lower()  # Take first string, remove spaces, and convert to lowercase
s2 = input("Enter second string: ").replace(" ", "").lower()  # Take second string, remove spaces, and convert to lowercase

if sorted(s1) == sorted(s2):  # Compare the sorted characters of both strings
    print("Anagrams")  # Print if both strings are anagrams
else:
    print("Not anagrams")  # Print if both strings are not anagrams