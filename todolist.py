import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.tasks = []
        self.create_widgets()

    def create_widgets(self):
        self.add_task_entry = tk.Entry(self.master)
        self.add_task_entry.pack()

        self.add_task_button = tk.Button(
            self.master, text="Add Task", command=self.add_task)
        self.add_task_button.pack()

        self.task_listbox = tk.Listbox(self.master)
        self.task_listbox.pack()

        self.delete_task_button = tk.Button(
            self.master, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

    def add_task(self):
        task = self.add_task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.add_task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do App")
    app = TodoApp(root)
    root.mainloop()