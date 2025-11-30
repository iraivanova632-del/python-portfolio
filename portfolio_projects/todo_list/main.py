tasks = []

def show_tasks():
    print("Ваши задачи:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

while True:
    cmd = input("Введите команду (add/show/exit): ")
    if cmd == "add":
        task = input("Новая задача: ")
        tasks.append(task)
    elif cmd == "show":
        show_tasks()
    elif cmd == "exit":
        break