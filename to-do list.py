print("----Welcome to Task Management System----")


todoList =[]

def add_list():
    no_of_task = int(input("enter the number of task you want to add in your today's to-do list: "))
    for i in range(1, no_of_task+1):
        tasks = input(f"enter task{i} to add in your today's to-do list: ")
        todoList.append(tasks)
    print("All Tasks are added successfully!\n")

def update_list():
    old_task =input("enter the task you want to update: ")
    idx = todoList.index(old_task)
    new_task = input("enter th new task you want to add: ")
    todoList[idx] = new_task
    print("Task Updated!")


def delete_list():
    del_task = input("enter the task you want to delete: ")
    idx= todoList.index(del_task)
    del todoList[idx]
    print("Task Deleted!")

def view_list():
    for task in todoList:
        print(task)

while True:
    choice = int(input("\npress '1' for Adding a Task\npress '2' for Updating the Task\npress '3' for Viewing a Task\npress '4' for Deleting a Task\npress '5' for Exiting\n"))

    if(choice == 1):
        add_list()
    elif(choice == 2):
        update_list()
    elif(choice == 3):
        view_list()
    elif(choice == 4):
        delete_list()
    elif(choice == 5):
        print("Exiting the System...")
        break
    else:
        print("INVALID CHOICE\nDo make a Valid Choice: ")

