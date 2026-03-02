#Authentication
from time import sleep
from src import storage
from src.models import Player
import hashlib

#Account creation
def new_account():
    name = input("Enter your name : ")
    password = input("Enter your password : ")
    acc_id = int(input("Enter your account ID : "))
    
    account = {
        "name": name,
        "password":hashlib.sha256(password.encode()).hexdigest(),
        "acc_id": acc_id,
        "health": 100,
        "locked": False
    }
    storage.save_account(acc_id, account)
    print("Account created successfully.")
    return Player(account['acc_id'], account['name'])

#login 
def login(attempts = 0, account = None ):
    
    if attempts >= 4:
        print("Maximum attempts reached.")
        print("Contact Admin [> _ *]")
        account["locked"] = True
        storage.save_account(acc_id, account)
        return None

    acc_id = input("Enter Account ID no. : ")

    account = storage.load_account(acc_id)

    if not account:
        print("Account not found.")
        return login(attempts + 1)

    print("Game Login")
    print(f"Attempts : {attempts + 1}")
    password=input("Enter account password: ")

    if account["locked"]:
        print("Account is locked.")
        return None

    if account["password"] != hashlib.sha256(password.encode()).hexdigest():
        print("Incorrect password.")
        sleep(2)
        return login(attempts + 1)

    print("___________Welcome____________")
    print(f"{account['name']} has logged in successfully.")
    print("___________Welcome____________")
    return Player(account['acc_id'], account['name'], account.get('health', 100))
    
#Entry point - choose login or signup
def authenticate():
    print("========= TimeBomb CLI ============")
    print("1.Work/Play Login")
    print("2.Create Account")
    print("===================================")
    
    choice = input("Choose one... (1 or 2): ")

    if choice == "1":
        return login()
    elif choice == "2":
        return new_account()
    else:
        print("Invalid option. Go away.")
        sleep(10)
        return authenticate()

if __name__ == "__main__":
    authenticate()