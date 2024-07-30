import tkinter as tk
from tkinter import messagebox

class TodoListManager:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

        # Create the main application window
        self.window = tk.Tk()
        self.window.title("Akash's Todo")

        # Create and pack a label above the task list to display "Your Tasks"
        self.label_title = tk.Label(self.window, text="Your Tasks", font=("Arial", 18))
        self.label_title.pack(pady=10)

        # Create a frame to contain the listbox and scrollbar for tasks
        self.frame_tasks = tk.Frame(self.window)
        self.frame_tasks.pack(pady=30)

        # Create a listbox to display tasks and pack it to the left
        self.list_tasks = tk.Listbox(self.frame_tasks, width=70)
        self.list_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar and pack it to the right of the listbox
        self.scroll_tasks = tk.Scrollbar(self.frame_tasks)
        self.scroll_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Configure the listbox to work with the scrollbar
        self.list_tasks.config(yscrollcommand=self.scroll_tasks.set)
        self.scroll_tasks.config(command=self.list_tasks.yview)

        # Create a frame to contain the input entry and add button
        self.frame_input = tk.Frame(self.window)
        self.frame_input.pack(pady=10)

        # Create an entry widget for task input with a placeholder
        self.entry_task = tk.Entry(self.frame_input, width=50, fg='grey')
        self.entry_task.pack(side=tk.LEFT)
        self.entry_task.insert(0, "Enter your task here...")
        self.entry_task.bind("<FocusIn>", self.on_entry_click)
        self.entry_task.bind("<FocusOut>", self.on_focus_out)

        # Create an "Add Task" button with a green background
        self.btn_add = tk.Button(self.frame_input, text="Add Task", command=self.add_task, bg="green", fg="white")
        self.btn_add.pack(side=tk.LEFT, padx=10)

        # Create a "Remove Task" button with a salmon background
        self.btn_remove = tk.Button(self.window, text="Remove Task", command=self.remove_task, bg="salmon", fg="white")
        self.btn_remove.pack(pady=10)

    def on_entry_click(self, event):
        """Clear the placeholder text when the entry is clicked and change text color to black."""
        if self.entry_task.get() == "Enter your task here...":
            self.entry_task.delete(0, tk.END)
            self.entry_task.config(fg='black')

    def on_focus_out(self, event):
        """Restore the placeholder text if the entry is empty when it loses focus and change text color to grey."""
        if not self.entry_task.get():
            self.entry_task.insert(0, "Enter your task here...")
            self.entry_task.config(fg='grey')

    def add_task(self):
        """Add a task to the task list and display it in the listbox."""
        task = self.entry_task.get()
        if task and task != "Enter your task here...":
            self.tasks.append(task)
            self.list_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
            self.on_focus_out(None)
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        """Remove the selected task from the task list and listbox."""
        try:
            selected_index = self.list_tasks.curselection()
            if selected_index:
                index = int(selected_index[0])
                removed_task = self.tasks.pop(index)
                self.list_tasks.delete(selected_index)
                messagebox.showinfo("Success", f"Task '{removed_task}' removed successfully.")
            else:
                messagebox.showwarning("Warning", "No task selected.")
        except IndexError:
            messagebox.showwarning("Warning", "Invalid selection.")

    def run(self):
        """Start the Tkinter main event loop to run the application."""
        self.window.mainloop()

# Create an instance of TodoListManager and run the application
if __name__ == "__main__":
    todo_list = TodoListManager()
    todo_list.run()
