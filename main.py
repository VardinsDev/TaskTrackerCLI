import json
import time
import os

def json_write(description, id, status, createdAt, updatedAt):
    filename = "data.json"

    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r", encoding="utf-8") as read_file:
            data = json.load(read_file)
    else:
        data=[]

    new_data = {
        "id": id,
        "description": description,
        "status": status,
        "createdAt": createdAt,
        "updatedAt": updatedAt
    }

    data.append(new_data)

    with open(filename, "w", encoding="utf-8") as write_file:
        json.dump(data, write_file, indent=4)

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

print('Welcome to the TaskTrackerCLI. To find available commands type task-cli help')
while (True):
    userInput = str(input("> "))
    if "task-cli" not in userInput:
        print("Invalid Command")
        print("Type task-cli help for more commands")
        continue
    userInput = userInput.replace("task-cli ", "")
    if "help" in userInput:
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
    if "add" in userInput:
        userInput = userInput.replace("add ", "")
        taskId = id_chooser()
        json_write(userInput, taskId, "todo", time.ctime(), time.ctime())
        print("Task added successfully (ID: " + str(taskId) + ")")
    if "update" in userInput:
        userInput = userInput.replace("update ", "")

