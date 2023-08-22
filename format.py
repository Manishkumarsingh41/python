import matplotlib.pyplot as plt

data = {
    'IT': 3486169,
    'Finance': 1665117,
    'Sales': 1498675,
    'Human Resources': 1212017,
    'Engineering': 1880959,
    'Marketing': 1672935,
    'Accounting': 824275,
}

# Convert the salary values to integers (removing commas)
for department, salary in data.items():
    data[department] = int(salary.replace(',', ''))

# Extract department names and salaries as separate lists
departments = list(data.keys())
salaries = list(data.values())

# Plot the data as a bar graph
plt.figure(figsize=(10, 6))
plt.bar(departments, salaries, color='skyblue')
plt.xlabel('Department')
plt.ylabel('Average Annual Salary ($)')
plt.title('Average Annual Salary by Department')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Show the graph
plt.show()
