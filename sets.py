# Step 1: Accept user input to create two sets of integers

set1 = set(map(int, input("Enter a set of integers separated by a space: ").split()))
set2 = set(map(int, input("Enter another set of integers separated by a space: ").split()))

# Step 2: Find the common elements in the two sets
common_elements = set1.intersection(set2)

# Step 3: Display the common elements
print(f"The common elements in the two sets are: {common_elements}")