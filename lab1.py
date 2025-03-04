# 1. Reverse a String
# Write a Python program to reverse a string.
print(f"Reversed word is : {'salma'[::-1]}")



# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 2. Check if a String is a Palindrome
# Write a Python program to check if a string is a palindrome(reads the same backward as forward).

word1 = "goog"
print(f"Is palindrom : {word1[::-1]==word1}")


# == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# 3.Remove Duplicates from a String
# Write a Python program to remove duplicate characters from a string.

word2= "salma"
print (f"word without duplicate : {''.join(set(word2))}")


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 4.Find the Longest Word in a String

# Write a Python program to find the longest word in a given string.

text = "Python is a great programming language"
print (f"the longest word is : {max(text.split(' '))}")


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 5.Find Common Elements Between Two Tuples
# Write a Python program to find common elements between two tuples.
# ``` python
tuple1 = (1, 2, 3)
tuple2 = (2, 3, 4)
print (f"the common is : {tuple(set(tuple1).intersection(set(tuple2)))}")


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 6.Find the Maximum and Minimum Value in a Dictionary
# Write a Python program to find the maximum and minimum value in a dictionary.
# ``` Python

my_dict = {"a": 10, "b": 20, "c": 5}
print(f"the Max = {max(my_dict.values())}, the Min = {min(my_dict.values())} ")


# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 7 - Merge Two Dictionaries
# Write a Python program to merge two dictionaries.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

dict1.update(dict2)
print (f"the merged dictionaries is : {dict1}")



# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 8 - Find Common Keys in Two Dictionaries
# Write a Python program to find common keys in two dictionaries.
dict1_1 = {"a": 1, "b": 2, "c": 3}
dict2_1 = {"b": 2, "c": 4, "d": 5}
# # Output: {'b', 'c'}

print (f"the Common Dictionary is :{set(dict1_1.keys()).intersection(set(dict2_1.keys()))}")



# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# 9 - takes a string and prints the longest
# alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is : abdu 

# text = "abdulrahman"
text = "abcabcd"

longest = current = text[0]

for i in range(1, len(text)):
    if text[i] >= text[i - 1]:
        current += text[i]
    else:
        current = text[i]

    if len(current) > len(longest):
        longest = current

print(f"Longest substring in alphabetical order is:{longest}")
