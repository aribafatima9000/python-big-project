

tasks = []   

while True:
    print("\n---- To-Do List Menu ----")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Mark Task as Done")
    print("5. Update Task")
    print("6. Clear All Tasks")
    print("7. Search Task")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"name": task, "done": False})
        print(f"'{task}' added to the list.")

    elif choice == "2":
        if not tasks:
            print("List is empty. Nothing to remove.")
        else:
            task = input("Enter task to remove: ")
            found = False
            for t in tasks:
                if t["name"] == task:
                    tasks.remove(t)
                    found = True
                    print(f"'{task}' removed.")
                    break
            if not found:
                print("Task not found.")

    elif choice == "3":
        if not tasks:
            print("Your list is empty.")
        else:
            print("Your To-Do List:")
            for i, t in enumerate(tasks, start=1):
                status = " Done" if t["done"] else " Pending"
                print(f"{i}. {t['name']} ({status})")

    elif choice == "4":
        task = input("Enter task to mark as done: ")
        found = False
        for t in tasks:
            if t["name"] == task:
                t["done"] = True
                found = True
                print(f"'{task}' marked as done ")
                break
        if not found:
            print("Task not found.")

    elif choice == "5":
        old_task = input("Enter task to update: ")
        found = False
        for t in tasks:
            if t["name"] == old_task:
                new_task = input("Enter new task name: ")
                t["name"] = new_task
                found = True
                print(f"'{old_task}' updated to '{new_task}'.")
                break
        if not found:
            print("Task not found.")

    elif choice == "6":
        tasks.clear()
        print("All tasks cleared.")

    elif choice == "7":
        task = input("Enter task to search: ")
        found = False
        for t in tasks:
            if t["name"] == task:
                print(f"'{task}' found! Status: {'Done ' if t['done'] else 'Pending ⏳'}")
                found = True
                break
        if not found:
            print("Task not found.")

    elif choice == "8":
        print("Exiting... Goodbye! ")
        break

    else:
        print("Invalid choice. Try again.")
