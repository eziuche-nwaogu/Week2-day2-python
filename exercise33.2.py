# The previous exercise was changed and converted to a function that takes two arguments for the number and the increment
# The function can then be called and passed the two parameters
# Here the while loop was converted to a for loop
def print_numbers(n, inc):
    numbers = []
    for i in range(0, n, inc):
        print(f"At the top i is {i}")
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)


print_numbers(20, 2)
