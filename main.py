import json
import time
import os

def writeData(data):
    filename = "data.json"
    with open(filename, "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)

def loadData():
    filename = "data.json"
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
    else:
        data = []
    return data

def json_write(description, id, status, createdAt, updatedAt):
    filename = "data.json"
    data = loadData()
    new_data = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    }
    data.append(new_data)
    writeData(data)

def deleteData(id):
    data = loadData()
    original_count = len(data)
    data = [task for task in data if task["id"] != id]
    if len(data) < original_count:
        writeData(data)
        print(f"Task with ID {id} successfully deleted!")
    else:
        print(f"Error: Task with ID {id} not found.")

def updateData(id, description, updatedTime):
    filename = "data.json"
    data = loadData()
    for task in data:
        if task["id"] == id:
            task["updatedAt"] = updatedTime
            task["description"] = description
            print("Change successful!")
    writeData(data)

def id_chooser():
    filename = "data.json"
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        return 1
    with open(filename, "r", encoding="utf-8") as read_file:
        try:
            data = json.load(read_file)
            if not data:
                return 1
            all_ids = [task["id"] for task in data]
            return max(all_ids) + 1
        except json.JSONDecodeError:
            return 1

def listData(status=None):
    data = loadData()
    for task in data:
        if status and task["status"].lower() != status.lower():
            continue

        print("")
        print(f"[ID: {task['id']}] {task['description']}")
        print(f"    Status: {task['status']}")
        print(f"    Created: {task['createdAt']}")
        print(f"    Updated: {task['updatedAt']}")
        print("")
        print("--------------------------------------------------")

def markInProgress(id):
    data = loadData()
    for task in data:
        if task["id"] == id:
            task["status"] = "In-Progress"
            task["updatedAt"] = time.ctime()
    writeData(data)

def markDone(id):
    data = loadData()
    for task in data:
        if task["id"] == id:
            task["status"] = "Done"
            task["updatedAt"] = time.ctime()
    writeData(data)

print('Welcome to the TaskTrackerCLI. To find available commands type task-cli help')
while (True):
    userInput = str(input("> "))
    if "task-cli" not in userInput:
        print("Invalid Command")
        print("Type task-cli help for more commands")
        continue
    userInput = userInput.replace("task-cli ", "")
    userInput = userInput.split()
    if not userInput: continue
    match userInput:
        case ["help"]:
            print("TaskCLI Help")
            print('add - Used to add a task, ex: task-cli add "Buy Groceries"')
            print('update - Used to update a task based on task id, ex: task-cli update 1 "Buy groceries and cook dinner')
            print('delete - Used to delete a task besed on task id, ex: task-cli delete 1')
            print('mark-in-progress - Used to show that you have started a task, ex: task-cli mark-in-progress 1')
            print('mark-done - Used to show that you have finished a task, ex: task-cli mark-done 1')
            print('list - Used to list all tasks')
            print('list done - Used to list all finished tasks')
            print('list todo - Used to list all tasks that are not started yet')
            print('list in-progress - Used to list all in progress tasks')
        case ["add", *description]:
            description = " ".join(description)
            taskId = id_chooser()
            json_write(description, taskId, "Todo", time.ctime(), time.ctime())
            print(f"Task added successfully (ID: {taskId})")
        case ["update", task_id, *description]:
            if not description:
                print("Please provide a description argument for example: task-cli update 1 take the dogs out")
            else:
                clean_id = int(task_id)
                description = " ".join(description)
                updateData(clean_id, description, time.ctime())
        case ["list"]:
            listData()
        case ["list", status]:
            listData(status)
        case ["delete", task_id]:
            clean_id = int(task_id)
            deleteData(clean_id)
        case ["mark-in-progress", task_id]:
            clean_id = int(task_id)
            markInProgress(clean_id)
            print(f"[ID: {clean_id}] Status: In Progress")
        case ["mark-done", task_id]:
            clean_id = int(task_id)
            markDone(clean_id)
            print(f"[ID: {clean_id}] Status: Done")
        case _:
            print("TaskCLI Help")
            print('add - Used to add a task, ex: task-cli add Buy Groceries')
            print('update - Used to update a task based on task id, ex: task-cli update 1 Buy groceries and cook dinner')
            print('delete - Used to delete a task besed on task id, ex: task-cli delete 1')
            print('mark-in-progress - Used to show that you have started a task, ex: task-cli mark-in-progress 1')
            print('mark-done - Used to show that you have finished a task, ex: task-cli mark-done 1')
            print('list - Used to list all tasks')
            print('list done - Used to list all finished tasks')
            print('list todo - Used to list all tasks that are not started yet')
            print('list in-progress - Used to list all in progress tasks')

