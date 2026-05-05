import json

FILE_NAME = "tasks.json"

def save_tasks(tasks):
    with open(FILE_NAME,"w") as file:
        json.dump(tasks,file)

def display_tasks(tasks):
    for i in range(len(tasks)):
        print(f'{i+1}. {tasks[i]["task"]}   done: {tasks[i]["done"]}')

print("choose option")
print("1.show tasks")
print("2.add task")
print("3.mark as done")
print("4.exit")

try:
    with open(FILE_NAME,"r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []
while True:
    choose = input("choose: ")
    if choose == "1":
        if not tasks:
            print("no tasks")
        else:
            display_tasks(tasks)
    elif choose == "2":
        tasks.append({
            "task": input("task: "),
            "done": False
            })
        save_tasks(tasks)
        print("task added")
    elif choose == "3":
        if not tasks:
            print("no tasks")
        else:
            display_tasks(tasks)
            mark=input("what task do we mark as done: ")
            try:
                mark=int(mark)
            except:
                print("wrong task")
                continue
            if mark in range(1,len(tasks)+1):
                if tasks[mark-1]["done"] == False:
                    tasks[mark-1]["done"] = True
                    save_tasks(tasks)
                    print("task marked as done")
                else:
                    print("this task is already marked as done")
            else:
                print("wrong task")
    elif choose =="4":
        break
    else:
        print("wrong option")