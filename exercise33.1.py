# The previous exercise was changed and converted to a function that takes two arguments for the number and the increment
# The function can then be called and passed the two parameters
def print_numbers(n, inc):
    i = 0
    numbers = []
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)
        i = i + inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    print("The numbers: ")
    for num in numbers:
        print(num)


print_numbers(20, 2)
