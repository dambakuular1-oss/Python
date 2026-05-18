def square(n):
    print(n ** 2)

def multiply(a, b):
    print(a * b)

def is_even(n):
    if n % 2 == 0:
        print(f"{n} — чётное")
    else:
        print(f"{n} — нечётное")

def sum_of_squares(numbers):
    return sum(x ** 2 for x in numbers)


square(5)
multiply(3, 4)
is_even(7)
is_even(8)
print(sum_of_squares([1, 2, 3, 4]))