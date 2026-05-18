# №1
num1 = 2
num2 = 3

def func(num1, num2):
    return num1 + num2

res = func(num1, num2)
print(res)


# №2
tst1 = 'abc'
tst2 = 'def'

def func1(txt):
    return txt.upper()

def func2(txt1, txt2):
    return txt1 + txt2

res = func2(func1(tst1), tst2)
print(res)