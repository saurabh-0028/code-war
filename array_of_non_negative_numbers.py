# Define a function that removes duplicates from an array of non negative numbers and returns it as a result. 
#The order of the sequence has to stay the same
# Function to remove duplicates
def remove_duplicates(arr):
    result = []
    
    for i in arr:
        if i not in result:
            result.append(i)
    
    return result

# Input
arr = list(map(int, input("Enter numbers: ").split()))
# Output
print(remove_duplicates(arr))
