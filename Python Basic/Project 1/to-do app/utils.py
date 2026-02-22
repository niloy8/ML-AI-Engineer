#Task logic funtion here


def loadtask():
    try:
        with open('tasks.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_task(tasks):
    with open("tasks.txt",'w') as file:
        for task in tasks:
            file.write(task+'\n')


def add_task(tasks,task):
    tasks.append(task)
    save_task(tasks)


def delete_task(tasks,index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_task(tasks)
    else:
        print("Invalid task number")