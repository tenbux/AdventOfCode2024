# Specify the path to the input file
file_path = 'input.txt'

# Initialize two empty lists to store the integers
list1 = []
list2 = []

# Open the file in read mode and read its contents line by line
with open(file_path, 'r') as file:
    for line in file:
        # Split the line by the delimiter "   "
        num1, num2 = line.strip().split("   ")
        # Convert the split strings to integers and append to respective lists
        list1.append(int(num1))
        list2.append(int(num2))

# Sort both lists
list1.sort()
list2.sort()

# Calculate the differences between corresponding elements
differences = [abs(a - b) for a, b in zip(list1, list2)]

# Calculate the total of the differences
total_difference = sum(differences)

# Print the sorted lists, their differences, and the total difference
print("List 1:", list1)
print("List 2:", list2)
print("Differences:", differences)
print("Total Difference:", total_difference)
