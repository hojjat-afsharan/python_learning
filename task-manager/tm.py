class Task: 
    def __init__(self, id, name, done = False) :
        self.id = id
        self.name = name
        self.done = done
    

class TaskManager: 
    def __init__(self):
        self.tasks = []

    def get_tasks(self):
        return self.tasks

    def add_task(self, id, name):
        self.tasks.append(Task(id,name))
        print("Task {0} added".format(name))


def main():
    while True:
        print("1. Add task")
        print("2. List tasks")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            id = int(input("Enter task id: "))
            name = input("Enter task name: ")
            task_manager.add_task(id, name)
        elif choice == "2":
            for task in task_manager.get_tasks():
                print("Task {0} is {1}".format(task.name, "done" if task.done else "not done"))
        elif choice == "3":
            break
        else:
            print("Invalid choice")

task_manager = TaskManager()
main()  





    