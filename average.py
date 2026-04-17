#Write a function which calculates the average of the numbers in a given array.
Note: Empty arrays should return 0.

# Function to calculate average
def find_average(arr):
    if len(arr) == 0:
        return 0
    return sum(arr) / len(arr)

# Input
arr = list(map(int, input("Enter numbers: ").split()))

# Output
print("Average:", find_average(arr))
