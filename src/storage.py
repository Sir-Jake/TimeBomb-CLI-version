from json import load, dump
import json
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_json(filename):
    filepath=os.path.join(DATA_DIR, filename)
    #if file does not exit create
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write("{}")
        return {}

    with open(filepath, "r") as f:
        try:
            data = json.load(f)
            # check the type of a value 
            if isinstance(data, list):
                return {}
            return data
        except json.JSONDecodeError:
            # If file is corrupted or empty return 
            return {}

# to save data to Json file
def save_json(filename,data):
    filepath=os.path.join(DATA_DIR,filename)
    with open(filepath,"w") as f:
        json.dump(data,f,indent=4)#convert python dic to json ,indent add space

#loading_account
def load_account(acc_id):
    with open("data/users.json", "r") as f:
        accounts = load(f)
        return accounts.get(acc_id)

#saving account
def save_account(acc_id, account):
    with open("data/users.json", "r") as f:
        accounts = load(f)
    
    accounts[str(acc_id)] = account

    with open("data/users.json", "w") as f:
        dump(accounts, f, indent=4)



#save users
def add_task(user_id, task):
    tasks = get_tasks()

    user_id = str(user_id)  # Ensure string key

    if user_id not in tasks:
        tasks[user_id] = []

    tasks[user_id].append(task)

    save_tasks(tasks)



def get_tasks():
    data=load_json("tasks.json")
    return data
def save_tasks(tasks):
    save_json("tasks.json",tasks)
    print("Tasks saved successfully.")


     

