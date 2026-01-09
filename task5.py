def display_tasks(task_list):
    """Prints all tasks in the list with their index."""
    if not task_list:
        print("\nYour task list is currently empty.")
    else:
        print("\n--- Your To-Do List ---")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")

def main():
    tasks = []
    print("Welcome to the Task Manager!")

    while True:
        print("\nOptions: [1] Add Task  [2] View Tasks  [3] Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print("Task added successfully.")
        
        elif choice == '2':
            display_tasks(tasks)
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()