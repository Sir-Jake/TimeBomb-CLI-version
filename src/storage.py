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
    