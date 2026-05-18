while True:
    name = input("дамба")
    
    if len(name) > 6:
        print("Имя слишком длинное!")
        break
    else:
        print(f"Привет, {name}!")
        break  # Останавливаем цикл в любом случае после одной итерации
