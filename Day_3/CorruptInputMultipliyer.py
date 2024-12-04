import re

# Specify the path to the input file
file_path = 'input.txt'

# Initialize a list to store the matched inputs
matched_inputs = []

# Initialize a variable to store the total
total = 0

# Initialize a variable to track whether mul instructions are enabled
mul_enabled = True

# Define the regular expression patterns
mul_pattern = re.compile(r"mul\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*\)")
do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

# Open the file in read mode and read its contents line by line
with open(file_path, 'r') as file:
    for line in file:
        # Find all do() and don't() instructions and mul(x, y) matches
        instructions = re.findall(r"do\(\)|don't\(\)|mul\(\s*\d{1,3}\s*,\s*\d{1,3}\s*\)", line)
        for instruction in instructions:
            if do_pattern.match(instruction):
                mul_enabled = True
            elif dont_pattern.match(instruction):
                mul_enabled = False
            else:
                match = mul_pattern.match(instruction)
                if match and mul_enabled:
                    matched_inputs.append(f"mul({match.group(1)}, {match.group(2)})")
                    x = int(match.group(1))
                    y = int(match.group(2))
                    total += x * y

# Print the matched inputs and the total
print("Matched Inputs:", matched_inputs)
print("Total:", total)
