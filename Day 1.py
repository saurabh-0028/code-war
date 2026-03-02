#Create a function that gives a personalized greeting. This function takes two parameters: name and owner.
#Use conditionals to return the proper message


def greet(name, owner):
    if name == owner:
        return f"Hello, boss {name}!"
    else:
        return f"Hello, {name}!"