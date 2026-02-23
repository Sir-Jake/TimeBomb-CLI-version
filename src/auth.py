#Authentication
from time import sleep
import storage

#login 
def login(attempts = 0, account = None, login_attempts = 1  ):
    
    if attempts >= 4:
        print("Maximum attempts reached.")
        print("Contact Jake [> _ *]")
        account["locked"] = True
        storage.save_account(account)
        return None

    acc_id = input("Enter Account ID no. : ")

    account = storage.load_account(acc_id)

    if not account:
        print("Account not found.")
        return login(attempts + 1)

    print("Game Login")
    print("Attempt no." ,attempts)
    password=input("Enter account password")

    if account["locked"]:
        print("Account is locked.")
        return None

    if account["password"] != password:
        print("Incorrect password.")
        return login(attempts + 1)

    print("___________Welcome____________")
    print(f"{account['name']}")
    print("___________Welcome____________")
    return account
    
login()