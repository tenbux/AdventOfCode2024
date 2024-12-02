# Specify the path to the input file
file_path = 'input.txt'

# Initialize a list to store the reports
reportList = []

# Open the file in read mode and read its contents line by line
with open(file_path, 'r') as file:
    for line in file:
        # Split the line by spaces and convert the split strings to integers
        report = [int(num) for num in line.strip().split()]
        reportList.append(report)

# Initialize a variable to store the total number of safe reports
total_safe_reports = 0


def is_safe(report_levels):
    increasing = True
    decreasing = True
    for i in range(1, len(report_levels)):
        diff = abs(report_levels[i] - report_levels[i - 1])
        if diff <= 0 or diff >= 4:
            return False
        if report_levels[i] > report_levels[i - 1]:
            decreasing = False
        elif report_levels[i] < report_levels[i - 1]:
            increasing = False
    return increasing or decreasing


# Iterate through each report in the report list
for report in reportList:
    if is_safe(report):
        total_safe_reports += 1
    # Added in part 2
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if is_safe(modified_report):
                total_safe_reports += 1
                break

# Print the total number of safe reports
print("Total Safe Reports:", total_safe_reports)
