import json
import os
import shutil

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_json(filename):
    filepath=os.path.exists(DATA_DIR, filename)
    #if file does not exit 
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

def get_users():
    data=load_json("users.json")
    return data

#save users
def save_users(users):
    save_json("users.json",users)

def get_tasks():
    save_json("tasks.json",)

def save_tasks(tasks):
    save_json("tasks.json",tasks)

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
    

