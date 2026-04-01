# Function to add two numbers given as strings
#Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
def sum_strings(a, b):
    # If empty string, treat as 0
    if a == "":
        a = "0"
    if b == "":
        b = "0"
    
    # Convert to integer, add, then convert back to string
    result = int(a) + int(b)
    return str(result)

# Input
a = input("Enter first number: ")
b = input("Enter second number: ")

# Output
print("Result:", sum_strings(a, b))
