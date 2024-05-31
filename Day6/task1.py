class Task:
    cnt = 0 
    def __init__(self, title, due_date, created_at, user):
        self.id = Task.cnt
        self.title = title
        self.due_date = due_date
        self.created_at = created_at
        self.user = user
        Task.cnt += 1
        
    def __str__(self):
        return f"""{'#' * 30}
ID --> {self.id}
Title --> {self.title}
Due date --> {self.due_date}
Created at --> {self.created_at} 
User --> {self.user}
{'#' * 30}"""

################################################################################################################################################  

task_list = []
class TaskManager:
    def add_task(self, title, due_date, created_at, user):
        new_task = Task(title, due_date, created_at, user)
        task_list.append(new_task)
        print("Task added successfully")

    def get_tasks(self):
        for i in task_list:
            print(i)
        print("#" * 30)
        
    def get_task_by_id(self, id):
        for task in task_list:
            if task.id == id:
                return task
        return False
    
    def edit_task_by_id(self, id):
        task = self.get_task_by_id(id)
        if task:
            task.title = input("Enter new title --> ")
            task.due_date = input("Enter new due date --> ")
            task.created_at = input("Enter new created at --> ")
            task.user = input("Enter new user --> ")
            print("Editing task completed successfully")
        else:
            print("Invalid Id !")
            
    def delete_task(self, id):
        task_to_delete = self.get_task_by_id(id)
        if task_to_delete:
            task_list.remove(task_to_delete)
            print("Task deleted successfully")
        else:
            print("Invalid Id")

################################################################################################################################################  

tasks = TaskManager()
while True:
    print("_" * 30)
    print("1. Add task")
    print("2. Get tasks")
    print("3. Get by id")
    print("4. Edit by id")
    print("5. Delete by id")
    print("0. Exit")
    print("_" * 30)
    choice = input("Enter your choice --> ")
    print("_" * 30)

    match choice:
        case "1":
            tasks.add_task(input("Enter Your Title --> "), input("Due date --> "), input("Created at --> "), input("Enter Your name --> "))
        case "2":
            tasks.get_tasks()
        case "3":
            task = tasks.get_task_by_id(int(input("Enter task ID --> ")))
            if task:
                print(task)
            else:
                print("Task not found")
        case "4":
            task_id = int(input("Enter task ID --> "))
            tasks.edit_task_by_id(task_id)
        case "5":
            tasks.delete_task(int(input("Enter task id --> ")))
        case "0":
            break
