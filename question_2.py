# Input two strings
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate and store in a new variable
combined_str = str1 + str2

# Display the concatenated string
print("\nConcatenated String:", combined_str)

# Commonly used string methodsIGOT ALA
print("\n--- String Methods Results ---")
print("Uppercase       :", combined_str.upper())
print("Lowercase       :", combined_str.lower())
print("Title Case      :", combined_str.title())
print("Capitalized     :", combined_str.capitalize())
print("Reversed        :", combined_str[::-1])
print("Length          :", len(combined_str))
print("Is Alphabetic?  :", combined_str.isalpha())
print("Is Numeric?     :", combined_str.isnumeric())
print("Replaced 'a' with '@':", combined_str.replace('a', '@'))
print("Count of 'a'    :", combined_str.count('a'))
print("Starts with 'S' :", combined_str.startswith('S'))
print("Ends with 'h'   :", combined_str.endswith('h'))
