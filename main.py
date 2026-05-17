from typing import List, Dict
import json
import argparse

save_file = "task.json"
memory = {}
count_task: int = 0

def is_file(exist_ok: bool = False) -> bool:
    from pathlib import Path
    path = Path(save_file)
    
    if not path.is_file() and not path.exists():
        if not exist_ok:
            return False
        
        with open(save_file, "w") as ff:
            json.dump(memory, ff)
        
    return True
    
def load_task() -> bool:
    """
    
    """
    global count_task, memory
    
    if not is_file(exist_ok=True):
        raise FileNotFoundError("file not found error, create 'task.json' manually")
    
    with open(save_file, "r") as task:
        response: dict = json.load(task)
        
        memory = response
        count_task = len(response.keys())
    
    return True

def write_task() -> bool:
    """
    
    """
    with open(save_file, "w") as task:
        json.dump(memory, task)
        
        return True
    
    return False
    
class task:
    def __init__(self):
        pass
    
    def create(self, object: str) -> bool:
        global count_task, memory
        names = [y['title'] for x,y in memory.items()]

        if not object:
            raise ValueError("object must be str, not empty")
        
        if object in names:
            return False, "Already added"
        
        count_task += 1
        memory[count_task] = {"title": object, "status": "todo"}
        write_task()
        
        return True,count_task
    
    def update(self, task_id: int, status: str = None, title: str = None) -> bool:
        if not task_id:
            raise ValueError("task_Id must be int, not empty")
        
        if not status and not title:
            print(f"[+] Nothing changes")
            return False
        
        for id, object in memory.items():
            id = int(id)
            
            if task_id == id:
                if status:
                    print(f"[+] {task_id} changed status from {object['status']} -> {status}")
                    object["status"] = status
                    
                elif title:
                    print(f"[+] {task_id} changed status from {object['title']} -> {title}")
                    object["title"] = title
                    
                write_task()
                return True
            
        else:
            print("[+] Nothing changes by task..")
            return False
    
    def read(self) -> List[Dict[str, str | int]]:
        """
        
        """
        return memory
    
    def delete(self, task_id: int) -> bool:
        if not task_id:
            raise ValueError("task_id must be int, not str or empty")
        
        for id, object in memory.items():
            if task_id == int(id):
                del memory[str(task_id)] 
                
                write_task()
                return True
            
        return False
    
    # QUERY :>
    def filter_with_status(self, status: str) -> Dict[str, dict]:
        status = status.lower()
        
        trust_mode = ["todo", "progress", "done", "all"]
        data = {}
        
        if status not in trust_mode:
            return {}
        
        if status == trust_mode[3]:
            return memory
        
        for task_id, object in memory.items():
            if object["status"] == status:
                data[task_id] = object
            
            continue
        
        return data
        

parse = argparse.ArgumentParser(
    prog="Task Tracker CLI",
    description="manage your task easily with task tracker CLI",
    epilog="use --help for help :D"
)

load_task()

subparser = parse.add_subparsers(dest="Command", required=True)

add_subparse = subparser.add_parser("add")
add_subparse.add_argument("title", type=str, help="task title")

update_subparse = subparser.add_parser("update")
update_subparse.add_argument("id", type=int)
update_subparse.add_argument("title", type=str)

delete_subparse = subparser.add_parser("delete")
delete_subparse.add_argument("id", type=int)

mark_progress_subparse = subparser.add_parser("mark-in-progress")
mark_progress_subparse.add_argument("id", type=int, help="task id")

mark_done_subparse = subparser.add_parser("mark-done")
mark_done_subparse.add_argument("id", type=int)

list_subparse = subparser.add_parser("list")
list_subparse.add_argument("status", 
                           nargs="?",
                           choices=["todo", "progress", "done", "all"],
                           default="all",
                           help="Just filter")

# :D
if 1+1 == 2:
    args = parse.parse_args()
    tasks = task()
    
    if args.Command == "add":
        status, response = tasks.create(args.title)
        if status:
            print(f"Task Added Successfully (ID: {response})")
        else:
            print(f"Failed to add: {status} - {response}")
        
    elif args.Command == "update":
        tasks.update(task_id=args.id, title=args.title)
    
    elif args.Command == "delete":
        tasks.delete(args.id)
        
    elif args.Command == "mark-in-progress":
        tasks.update(task_id=args.id, status="progress")
    
    elif args.Command == "mark-done":
        tasks.update(task_id=args.id, status="done")
    
    elif args.Command == "list":
        response = tasks.filter_with_status(status=args.status)
        
        for idx, (task_id, object) in enumerate(response.items()):
            print(f"[{idx}] - {task_id} | title : {object['title']} | status : {object['status']}")
        else:
            print(f"There's not task with status : {args.status}")
    else:
        print(f"unknown command: {args}")