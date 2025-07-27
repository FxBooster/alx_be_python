# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through each row
while row < size:
    # For each row, use a for loop to print asterisks side by side
    for col in range(size):
        print("*", end="")
    # After finishing one row, move to the next line
    print()
    row += 1
