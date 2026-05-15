# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#Example (Input => Output):
#35231 => [1,3,2,5,3]
#0     => [0]
# ArraysFundamentals
# Function to reverse digits into array

def digitize(n):
    result = []
    
    for digit in str(n)[::-1]:
        result.append(int(digit))
    
    return result

# Input
n = int(input("Enter number: "))

# Output
print(digitize(n))
