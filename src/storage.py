from json import load, dump
#loading account
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

import json
import os
import shutil

# Path to data folder
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_json(filename):
    filepath = os.path.join(DATA_DIR, filename)

    # If file does not exist, create empty dictionary
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            json.dump({}, f)
        return {}

    with open(filepath, "r") as f:
        try:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            return {}


def save_json(filename, data):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# USER FUNCTIONS
# -----------------------------
def get_users():
    return load_json("users.json")


def save_users(users):
    save_json("users.json", users)
    print("Users saved successfully.")

def get_tasks():
    return load_json("tasks.json")


def save_tasks(tasks):
    save_json("tasks.json", tasks)
    print("Tasks saved successfully.")


def add_task(user_id, task):
    tasks = get_tasks()

    user_id = str(user_id)  # Ensure string key

    if user_id not in tasks:
        tasks[user_id] = []

    tasks[user_id].append(task)

    save_tasks(tasks)


# -----------------------------
# MOVE FILE TO BACKUP
# -----------------------------
def move_file(filename, destination_folder):
    source_file = os.path.join(DATA_DIR, filename)

    if not os.path.exists(source_file):
        print(f"File {filename} does not exist. Cannot move.")
        return

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    shutil.move(source_file, os.path.join(destination_folder, filename))
    print(f"Moved {filename} to {destination_folder}")