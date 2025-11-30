def calc():
    while True:
        expr = input("Введите выражение (или 'exit'): ")
        if expr == "exit":
            break
        try:
            print("Результат:", eval(expr))
        except Exception as e:
            print("Ошибка:", e)

calc()