#Write a function that returns a string in which firstname is swapped with last name.
# Function to swap first and last name
def swap_name(name):
    parts = name.split()      # split into words
    return parts[1] + " " + parts[0]

# Input
name = input("Enter full name: ")
# Output
print("Result:", swap_name(name))
