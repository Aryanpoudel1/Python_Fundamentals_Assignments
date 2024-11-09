import todo_operations
import utils

tasks = []

def menu():
    print("--- To-Do List ---")
    print("\n1. Add a New Task \t 2. View All Tasks \t3. Delete a Task by Index \t4. Clear Screen \t5. Exit")

def main():
    while True:
        menu()
        choice = input("Please enter your choice : ")

        if choice == '1':
            task = input("Enter the new task: ")
            todo_operations.add_task(tasks, task)
        elif choice == '2':
            todo_operations.view_tasks(tasks)
        elif choice == '3':
            try:
                index = int(input("Enter the index of the task that you want delete: "))
                todo_operations.delete_task(tasks, index)
            except ValueError:
                print("Input is invalid.")
        elif choice == '4':
            utils.clear_screen()
        elif choice == '5':
            print("Exited from the app")
            break
        else:
            print("Your Choice is invalid")

if __name__ == "__main__":
    main()