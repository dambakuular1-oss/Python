# №1
def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def cube_of_square(n):
    return cube(square(n))

print(cube_of_square(3))


# №2
def capitalize_if_string(value):
    if isinstance(value, str):
        return value.capitalize()

def greet(name):
    name = capitalize_if_string(name)
    print(f"Привет, {name}!")

greet("иван")
greet("МАРИЯ")