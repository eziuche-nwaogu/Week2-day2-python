# Here the code has been changed a bit. The element variable has been changed and the for loop has been removed
# The code her has been changed a bit
the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]
# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")
# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")
# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")
# we can also build lists, first start with an empty one
elements = list(range(0, 6))
# # now we can print them out too
# The print statement has been formatted to give a better output
for i in elements:
    print(f"Element {i+1} is: {i}")
