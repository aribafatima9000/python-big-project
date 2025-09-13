

import os

TASK_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from file into a list of dicts."""
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    title, done = line.rsplit("|", 1)
                    tasks.append({"title": title, "done": done == "1"})
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            done_flag = "1" if task["done"] else "0"
            f.write(f"{task['title']}|{done_flag}\n")

def list_tasks(tasks):
    """Print all tasks."""
    if not tasks:
        print("No tasks found!")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✗"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter new task: ").strip()
    if title:
        tasks.append({"title": title, "done": False})
        print(f" Task added: {title}")
    else:
        print("⚠ Empty task ignored.")

def mark_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"✔ Marked complete: {tasks[num-1]['title']}")
        else:
            print("⚠ Invalid number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def remove_task(tasks):
    list_tasks(tasks)
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑 Removed: {removed['title']}")
        else:
            print("⚠ Invalid number.")
    except ValueError:
        print("⚠ Please enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task complete")
        print("4. Remove task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(" Tasks saved. Goodbye!")
            break
        else:
            print("⚠ Invalid choice, try again.")

if __name__ == "__main__":
    main()
