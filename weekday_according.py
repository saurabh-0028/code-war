#Complete the function which returns the weekday according to the input number:
#1 returns "Sunday"
# Function to return weekday
def whatday(num):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }

    return days.get(num, "Wrong, please enter a number between 1 and 7")

# Input
num = int(input("Enter a number (1-7): "))

# Output
print(whatday(num))
