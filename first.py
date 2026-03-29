def double_char(s):
    result = ""
    for c in s:
        result += c * 2
    return result

# Taking input from user
s = input("Enter a string: ")

# Calling function
output = double_char(s)

# Printing result
print("Output:", output)