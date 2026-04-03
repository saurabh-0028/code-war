#Given three integers a, b, and c, return the largest number obtained after inserting the operators +, *, and parentheses (). 
#In other words, try every combination of a, b, and c with the operators, without reordering the operands, and return the maximum value.

# Function to find maximum value
def max_expression(a, b, c):
    return max(
        a + b + c,
        a * b * c,
        a * (b + c),
        (a + b) * c,
        a + b * c
    )

# Input
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# Output
print("Maximum value:", max_expression(a, b, c))s
