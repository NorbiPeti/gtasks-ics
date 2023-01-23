import json
from ics import Todo, Calendar, utils

f = open('Tasks.json')
lists = json.load(f)

for tasklist in lists["items"]:
    cal = Calendar()
    for task in tasklist["items"]:
        todo = Todo()
        todo.name = task["title"]
        if "created" in task:
            todo.created = utils.get_arrow(task["created"])
        else:
            todo.created = utils.get_arrow(task["updated"])  # Not ideal but what can you do
        if "notes" in task:
            todo.description = task["notes"]
        if "due" in task:
            todo.due = task["due"]
        if task["status"] == "needsAction":
            todo.status = "NEEDS-ACTION"
        elif task["status"] == "completed":
            todo.status = "COMPLETED"
            todo.completed = utils.get_arrow(task["completed"])
            todo.percent = 100
        cal.todos.add(todo)
    of = open(tasklist["title"] + ".ics", 'w')
    of.write(cal.serialize())
    of.close()

f.close()
