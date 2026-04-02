#Bob needs a fast way to calculate the volume of a rectangular cuboid with three values: the length, width and height of the cuboid.
#Write a function to help Bob with this calculation.
# Function to calculate volume
def volume_cuboid(length, width, height):
    return length * width * height

# Input
l = int(input("Enter length: "))
w = int(input("Enter width: "))
h = int(input("Enter height: "))

# Output
print("Volume:", volume_cuboid(l, w, h))
