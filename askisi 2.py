import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(tasks))

def main():
    tasks = load_tasks()
    while True:
        print("\n--- Task List App ---")
        print("1. Προσθήκη εργασίας")
        print("2. Διαγραφή εργασίας")
        print("3. Προβολή εργασιών")
        print("4. Έξοδος")
        choice = input("Επιλογή: ")

        if choice == "1":
            task = input("Γράψε την εργασία: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            for i, t in enumerate(tasks):
                print(f"{i+1}. {t}")
            try:
                index = int(input("Αριθμός εργασίας προς διαγραφή: ")) - 1
                if 0 <= index < len(tasks):
                    del tasks[index]
                    save_tasks(tasks)
                else:
                    print("Μη έγκυρος αριθμός.")
            except ValueError:
                print("Μη έγκυρη είσοδος.")
        elif choice == "3":
            if tasks:
                print("\nΕργασίες:")
                for i, t in enumerate(tasks):
                    print(f"{i+1}. {t}")
            else:
                print("Καμία εργασία.")
        elif choice == "4":
            print("Έξοδος...")
            break
        else:
            print("Μη έγκυρη επιλογή.")

main()
