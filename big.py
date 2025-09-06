import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("400x500")
        self.root.config(bg="#f5f5f5")

        self.tasks = load_tasks()

        # Title Label
        tk.Label(self.root, text="My To-Do List", font=("Arial", 16, "bold"), bg="#f5f5f5").pack(pady=10)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(self.root, width=40, height=15, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Scrollbar
        scrollbar = tk.Scrollbar(self.task_listbox)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        # Entry field
        self.task_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        self.task_entry.pack(pady=5)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", width=10).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", width=10).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Mark Done", command=self.mark_done, bg="#2196F3", fg="white", width=10).grid(row=0, column=2, padx=5)

        self.load_into_listbox()

    def load_into_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✔️" if task["done"] else "❌"
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"title": task, "done": False})
            save_tasks(self.tasks)
            self.task_entry.delete(0, tk.END)
            self.load_into_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            selected = self.task_listbox.curselection()[0]
            task = self.tasks.pop(selected)
            save_tasks(self.tasks)
            self.load_into_listbox()
            messagebox.showinfo("Deleted", f"Task '{task['title']}' deleted!")
        except:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_done(self):
        try:
            selected = self.task_listbox.curselection()[0]
            self.tasks[selected]["done"] = True
            save_tasks(self.tasks)
            self.load_into_listbox()
            messagebox.showinfo("Done", f"Task marked as done!")
        except:
            messagebox.showwarning("Warning", "Please select a task to mark done!")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
