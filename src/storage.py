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



def move_files(working_dir,filename,prompt=True):
    destination_path=os.path.join(working_dir,filename)
    
    source=os.path.join(working_dir,filename)

    isdir=os.path.isdir(destination_path)

