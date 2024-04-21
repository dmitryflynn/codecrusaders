from cmu_graphics import *

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False

class TaskManagerApp(App):
    def __init__(self):
        super().__init__()
        self.tasks = []

    def setup(self):
        # Create GUI components
        self.label_task = Text("Task:")
        self.entry_task = TextBox(200)
        self.label_due_date = Text("Due Date (YYYY-MM-DD):")
        self.entry_due_date = TextBox(200)
        self.button_add_task = Button("Add Task", self.add_task)
        self.text_tasks = TextBox(600, 300, multiline=True)
        self.button_view_tasks = Button("View Tasks", self.view_tasks)
        self.button_exit = Button("Exit", self.save_and_exit)

        # Layout components
        self.label_task.move_to(50, 50)
        self.entry_task.move_to(200, 50)
        self.label_due_date.move_to(50, 100)
        self.entry_due_date.move_to(200, 100)
        self.button_add_task.move_to(400, 100)
        self.text_tasks.move_to(50, 150)
        self.button_view_tasks.move_to(50, 500)
        self.button_exit.move_to(150, 500)

    def add_task(self):
        description = self.entry_task.get_text()
        due_date_str = self.entry_due_date.get_text()

        try:
            due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
            new_task = Task(description, due_date)
            self.tasks.append(new_task)
            show_message("Success", "Task added successfully.")
            self.entry_task.set_text("")
            self.entry_due_date.set_text("")
            self.save_tasks()
        except ValueError:
            show_message("Error", "Invalid date format. Please use YYYY-MM-DD.")

    def view_tasks(self):
        tasks_text = ""
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Pending"
            tasks_text += f"{index}. {task.description} - Due: {task.due_date} - Status: {status}\n"
        self.text_tasks.set_text(tasks_text)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(f"{task.description}|{task.due_date}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    description, due_date_str = line.strip().split("|")
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d").date()
                    self.tasks.append(Task(description, due_date))
        except FileNotFoundError:
            pass

    def save_and_exit(self):
        self.save_tasks()
        self.close()

def main():
    app = TaskManagerApp()
    app.load_tasks()  # Load tasks when the app starts
    app.run()

if __name__ == "__main__":
    main()
