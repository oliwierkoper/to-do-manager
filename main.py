print("choose option")
print("1.show tasks")
print("2.add task")
print("3.mark as done")
print("4.exit")

tasks=[]

while True:
    choose = input("choose: ")
    if choose == "1":
        if not tasks:
            print("no tasks")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choose == "2":
        tasks.append(input("task: "))
        print("task added")
    elif choose == "3":
        if not tasks:
            print("no tasks")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            mark=input("what task do we mark as done: ")
            try:
                mark=int(mark)
            except:
                print("wrong task")
                continue
            if mark in range(1,len(tasks)+1):
                del tasks[mark-1]
                print("task marked as done")
            else:
                print("wrong task")
    elif choose =="4":
        break
    else:
        print("wrong option")