import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os


class TodoListManager:
    def __init__(self):
        # Database path setup
        self.db_folder = os.path.join(os.getcwd(), "Todo_List")
        self.db_path = os.path.join(self.db_folder, "todo_data.db")
        self.init_db()

        # Create the main application window
        self.window = tk.Tk()
        self.window.title("Akash's Todo")
        self.window.geometry("600x500")
        self.window.maxsize(600,500)

        # Load and set the background image
        try:
            bg_image = Image.open("background.png")  # Replace with your image file path
            bg_image = bg_image.resize((600, 500))
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.bg_label = tk.Label(self.window, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load background image: {e}")

        # Create and pack a label above the task list to display "Your Tasks"
        self.label_title = tk.Label(self.window, text="Your Tasks", font=("Arial", 18), bg="#f0f0f0", fg="black")
        self.label_title.pack(pady=10)

        # Create a frame to contain the listbox and scrollbar for tasks
        self.frame_tasks = tk.Frame(self.window, bg="#f0f0f0")
        self.frame_tasks.pack(pady=30)

        # Create a listbox to display tasks and pack it to the left
        self.list_tasks = tk.Listbox(self.frame_tasks, width=70, font=("Arial", 12), bd=2, relief="solid")
        self.list_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

        # Create a scrollbar and pack it to the right of the listbox
        self.scroll_tasks = tk.Scrollbar(self.frame_tasks)
        self.scroll_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

        # Configure the listbox to work with the scrollbar
        self.list_tasks.config(yscrollcommand=self.scroll_tasks.set)
        self.scroll_tasks.config(command=self.list_tasks.yview)

        # Create a frame to contain the input entry and add/edit button
        self.frame_input = tk.Frame(self.window, bg="#f0f0f0")
        self.frame_input.pack(pady=10)

        # Create an entry widget for task input with a placeholder
        self.entry_task = tk.Entry(self.frame_input, width=50, font=("Arial", 12), fg='grey', bd=2, relief="solid")
        self.entry_task.pack(side=tk.LEFT)
        self.entry_task.insert(0, "Enter your task here...")
        self.entry_task.bind("<FocusIn>", self.on_entry_click)
        self.entry_task.bind("<FocusOut>", self.on_focus_out)

        # Create an "Add Task" button with a green background
        self.btn_add = tk.Button(self.frame_input, text="Add Task", command=self.add_task, bg="green", fg="white",
                                 font=("Arial", 12), relief="groove", bd=2)
        self.btn_add.pack(side=tk.LEFT, padx=10)

        # Create a "Remove Task" button
        self.btn_remove = tk.Button(self.window, text="Remove Task", command=self.remove_task, bg="salmon", fg="white",
                                    font=("Arial", 12), relief="groove", bd=2)
        self.btn_remove.pack(pady=10)

        # Create an "Edit Task" button
        self.btn_edit = tk.Button(self.window, text="Edit Task", command=self.edit_task, bg="blue", fg="white",
                                  font=("Arial", 12), relief="groove", bd=2)
        self.btn_edit.pack(pady=10)

        # Load tasks from the database
        self.load_tasks()

    def init_db(self):
        """Initialize the SQLite database and ensure folder structure."""
        if not os.path.exists(self.db_folder):
            os.makedirs(self.db_folder)

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)"
        )
        self.conn.commit()

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
        """Add a task to the database and display it in the listbox."""
        task = self.entry_task.get().strip()
        if task and task != "Enter your task here...":
            self.cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
            self.conn.commit()
            self.list_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
            self.on_focus_out(None)
            messagebox.showinfo("Success", "Task added successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        """Remove the selected task from the database and listbox."""
        try:
            selected_index = self.list_tasks.curselection()
            if selected_index:
                task_text = self.list_tasks.get(selected_index)
                self.cursor.execute("DELETE FROM tasks WHERE task = ?", (task_text,))
                self.conn.commit()
                self.list_tasks.delete(selected_index)
                messagebox.showinfo("Success", f"Task '{task_text}' removed successfully.")
            else:
                messagebox.showwarning("Warning", "No task selected.")
        except IndexError:
            messagebox.showwarning("Warning", "Invalid selection.")

    def edit_task(self):
        """Edit the selected task."""
        try:
            selected_index = self.list_tasks.curselection()
            if selected_index:
                task_text = self.list_tasks.get(selected_index)
                new_task = self.entry_task.get().strip()
                if new_task and new_task != "Enter your task here...":
                    self.cursor.execute("UPDATE tasks SET task = ? WHERE task = ?", (new_task, task_text))
                    self.conn.commit()
                    self.list_tasks.delete(selected_index)
                    self.list_tasks.insert(selected_index, new_task)
                    self.entry_task.delete(0, tk.END)
                    self.on_focus_out(None)
                    messagebox.showinfo("Success", "Task updated successfully.")
                else:
                    messagebox.showwarning("Warning", "Please enter a new task to update.")
            else:
                messagebox.showwarning("Warning", "No task selected.")
        except IndexError:
            messagebox.showwarning("Warning", "Invalid selection.")

    def load_tasks(self):
        """Load tasks from the database into the listbox."""
        self.cursor.execute("SELECT task FROM tasks")
        tasks = self.cursor.fetchall()
        for task in tasks:
            self.list_tasks.insert(tk.END, task[0])

    def run(self):
        """Start the Tkinter main event loop to run the application."""
        self.window.mainloop()


# Create an instance of TodoListManager and run the application
if __name__ == "__main__":
    todo_list = TodoListManager()
    todo_list.run()
