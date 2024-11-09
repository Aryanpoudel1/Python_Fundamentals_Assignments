def add_task(tasks, task):
    tasks.append(task)
    print(f"Task '{task}'is added to the list.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task '{removed_task}' is deleted.")
    else:
        print("Index is invalid")

def view_tasks(tasks):
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty!")