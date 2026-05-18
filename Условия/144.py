# №1. Пример с целым числом
tst = 12
if isinstance(tst, int):
    print('integer')

# №2. Пример с числом с плавающей точкой
tst = 3.14
if isinstance(tst, float):
    print('float')

# №3. Пример со строкой
tst = "Hello"
if isinstance(tst, str):
    print('string')

# №4. Пример со словарём
tst = {"name": "Alice", "age": 25}
if isinstance(tst, dict):
    print('dictionary')

# №5. Пример с множеством
tst = {1, 2, 3, 4}
if isinstance(tst, set):
    print('set')

# №6. Пример с кортежем
tst = (1, 2, 3)
if isinstance(tst, tuple):
    print('tuple')

# №7. Пример со списком
tst = [1, 2, 3, 4, 5]
if isinstance(tst, list):
    print('list')
