# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

# Function
def problem(a):
    if type(a) == str:
        return "Error"
    return a * 50 + 6

# Input
a = input("Enter value: ")

# Check if number or string
if a.lstrip('-').replace('.', '', 1).isdigit():
    a = float(a) if '.' in a else int(a)

# Output
print(problem(a))
