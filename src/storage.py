from json import load, dump
import json
import os
import shutil

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

def get_users():
    data=load_json("users.json")
    return data

#save users
def add_tasks(task):
    tasks=get_tasks()
    tasks.append(task)
    save_tasks(tasks)

def save_users(users):
    save_json("users.json",users)

def get_tasks():
    data=load_json("tasks.json")
    return data
def save_tasks(tasks):
    storage.save_json("tasks.json",tasks)
    print("Tasks saved successfully.")

def move_file(filename,destination_folder):
    source_file=os.path.join(DATA_DIR,filename)
    #check does the file exist
    if not os.path.exists(source_file):
        print(f"File {filename} does not exist. Cannot move")
        return

    #creating a destination folder if it missing
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        #moving the file to the new folder
    shutil.move(source_file,os.path.join(destination_folder,filename))
    print(f"Moved {filename} to {destination_folder}")

if __name__ == "__main__":
    users=get_users()
    tasks=get_tasks()

    print("Users loaded:", users)
    print("Tasks loaded:",tasks)
    #adding a test user
    #users["player1"]={"health": 100, "score":0}
    #save_users(users)
    #print("Added player1 to users.json")
    move_file("users.json","backup")


     

