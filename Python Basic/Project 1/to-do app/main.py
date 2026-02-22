from utils import add_task,loadtask,delete_task


def show_task(tasks):
    if not tasks:
        print("No tasks Avaiable")
        return

    for i, task in enumerate(tasks):
        print(f'{i +1} : {task}')

def show_completetask(task1):
    for task in task1:
        print(f'{task} completed')

def save_complete(tasks,index):
    if not tasks:
        print("Invalid task number try to add task first")
        return
    else:
        print(f'Task {index} is complete : {tasks}')

task1 = []


def mark_complete(tasks,index):
    if 0<= index < len(tasks):
         task = tasks.pop(index)

         task1.append(task)
         save_complete(task,index)

         print("The task is complete")
    else:
        print("Invalid task")



def main():
    tasks = loadtask()
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")

        print("3. Delete Task")
        print("4. Exit")
        print("5. Mark Complete")
        print("6. Show Completed task")

        choice = input("Choose option: ")

        if choice == "1":
            show_task(tasks)

        elif choice == "2":
            task = input("Enter new task: ")
            add_task(tasks, task)

        elif choice == "3":
            show_task(tasks)
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)

        elif choice == "4":
            print("Goodbye!")
            break
        elif choice == "5":
            show_task(tasks)
            index = int(input("Enter the task number - "))
            mark_complete(tasks,index)
        elif choice == "6":
            show_completetask(task1)
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()