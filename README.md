# CODING-SAMURAI-INTERNSHIP-TASK
# To-Do List Application

This Python-based command-line application offers a simple yet effective way to manage your daily tasks. With an easy-to-use interface, you can add tasks, view them, mark them as completed, delete them, and save them to a file for persistence across sessions. This application is perfect for anyone looking to get organized without the overhead of a complex task management system.

## Features

- Add Tasks: Users can add new tasks with a title and description, making it easy to keep track of what needs to be done.
- List Tasks: View all current tasks, along with their details such as title, description, status (completed or not completed), and a unique task ID.
- Mark Tasks as Complete: Easily mark tasks as completed, allowing for a clear view of what's left to be done.
- Delete Tasks: Remove tasks that are no longer needed or have been completed.
- Save Tasks: All tasks are saved to a `tasks.json` file, ensuring that your to-do list is preserved even after the program is closed.
- Load Tasks: Upon starting the application, tasks are automatically loaded from the `tasks.json` file, so you can pick up right where you left off.

## How to Run

To use the To-Do List application, follow these simple steps:

1. Ensure you have Python installed on your machine.
2. Download the `todo_list.py` script to your local machine.
3. Open your command-line interface (CLI) and navigate to the directory containing the script.
4. Run the script by entering `python todo_list.py` or `python3 todo_list.py`, depending on your Python installation.
5. Follow the on-screen prompts to manage your tasks.

## Dependencies

- Python (This application was developed and tested with Python 3.8.5. It should be compatible with Python 3.x versions.)
- No external Python libraries are required, as it only uses the built-in `json` module for file handling.

## User Guide

The application presents a menu with the following options:

1. Add task: Enter the title and description for the new task.
2. List tasks: Displays all tasks with their ID, title, description, and completion status.
3. Mark task as complete: Enter the ID of the task you wish to mark as completed.
4. Delete task: Enter the ID of the task you wish to delete.
5. Save tasks: Saves the current list of tasks to the file. (Note: This is also done automatically when exiting the application.)
6. Exit: Closes the application after saving the current tasks.

Enjoy using this application to stay organized and on top of your tasks!
