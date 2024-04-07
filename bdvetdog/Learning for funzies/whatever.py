def add_task():
    '''
    vai criar um ficheiro para armazenar as tasks
    vai armazenar as tasks
    '''
    print("|_Add tasks_|".upper())
def remove_task():
    '''
    remove a task do ficheiro
    '''
    print("Remove tasks")
def manage_task():
    print("Manage tasks")
def main():
    select = int(input("Add Task (1)\nRemove Task (2)\nManage Tasks (3)\nQuit (4)\n"))
    if select == 1:
        add_task()
    elif select == 2:
        remove_task()
    elif select == 3:
        manage_task()
    elif select == 4:
        print("OK, quitting...")
        quit()
    else:
        print("Invalid command")

main()