from collections import Counter

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

# Count the occurrences of each number in the right list
count_list2 = Counter(list2)

# Calculate the total similarity score
total_similarity_score = sum(num * count_list2[num] for num in list1)

# Print the total similarity score
print("Total Similarity Score:", total_similarity_score)
