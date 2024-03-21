import json
import os
from datetime import datetime

class Task:
    def __init__(self, title, priority, due_date=None, completed=False):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __repr__(self):
        return f"Title: {self.title}, Priority: {self.priority}, Due Date: {self.due_date}, Completed: {self.completed}"

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                for task_data in data:
                    task = Task(**task_data)
                    self.tasks.append(task)

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            data = [task.__dict__ for task in self.tasks]
            json.dump(data, f, indent=4)

    def add_task(self, title, priority, due_date=None):
        task = Task(title, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Invalid task index.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
            self.save_tasks()
        else:
            print("Invalid task index.")

    def display_tasks(self):
        print("------ TO-DO LIST ------")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. {task}")
        print("------------------------")

def main():
    todo_list = TodoList("tasks.json")

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ")
            due_date = input("Enter due date (YYYY-MM-DD), leave empty if none: ")
            if due_date:
                due_date = datetime.strptime(due_date, "%Y-%m-%d")
            todo_list.add_task(title, priority, due_date)
        elif choice == '2':
            index = int(input("Enter index of task to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter index of task to mark as completed: ")) - 1
            todo_list.mark_task_completed(index)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
