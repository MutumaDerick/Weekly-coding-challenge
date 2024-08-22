# Task 1: Create a list of intergers and compute the sum

# Step 1: Accept user input and create a list of integers
intergers = input("Enter a list of intergers separated by a space: ")
interger_list = [int(x) for x in intergers.split()]

# Step 2: Compute the sum of the list
total_sum = sum(interger_list)

# Step 3: Display the sum
print(f"The sum of the list is: {total_sum}")



