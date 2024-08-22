# Step 1: Create a list of words

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi", "lemon"]

# Step 2: Use list comprehension to filter words with odd number of characters
odd_words = [word for word in words if len(word) % 2 != 0]

# Step 3: Display the list of odd words
print(f"Words with odd number of characters: ", odd_words)