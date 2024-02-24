 import json

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def add_task(self, title, description):
        task_id = len(self.tasks) + 1
        self.tasks.append({"id": task_id, "title": title, "description": description, "completed": False})
        print(f"Task added with ID: {task_id}")

    def list_tasks(self):
        for task in self.tasks:
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"ID: {task['id']}, Title: {task['title']}, Description: {task['description']}, Status: {status}")

    def mark_task_as_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                print(f"Task {task_id} marked as completed.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print("Task not found.")

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file)
        print("Tasks saved to file.")

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def run(self):
        while True:
            print("\nTo-Do List Application")
            print("1. Add task")
            print("2. List tasks")
            print("3. Mark task as complete")
            print("4. Delete task")
            print("5. Save tasks")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                self.add_task(title, description)
            elif choice == "2":
                self.list_tasks()
            elif choice == "3":
                task_id = int(input("Enter task ID to mark as complete: "))
                self.mark_task_as_complete(task_id)
            elif choice == "4":
                task_id = int(input("Enter task ID to delete: "))
                self.delete_task(task_id)
            elif choice == "5":
                self.save_tasks()
            elif choice == "6":
                self.save_tasks()
                print("Exiting...")
                break
            else:
                print("Invalid choice, please choose again.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
