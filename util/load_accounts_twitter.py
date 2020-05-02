import json

def load_db_accounts():
    data_result = {}
    with open('./accountsTwitter.json', 'r') as accounts:
         data_result = json.load(accounts)

    return data_result

