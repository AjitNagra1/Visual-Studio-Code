task_list=[]
task_input=[]

while task_input != "":
    task_input=input("Enter task: ")
    task_list.append(task_input)
    
if task_input == "":
    task_list.remove("")
    print(task_list)