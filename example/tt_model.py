import json
import os
import random 
from random import randint
from random import seed
from collections import defaultdict

PATH = os.path.dirname(__file__)
DATA = "data.json"
DATAPATH = os.path.join(PATH,DATA)

class Account:
    data_path = DATAPATH # ensures the same file used for all underlying functions and classes, all classes will inherit from datapath changed on top

    def __init__(self, account_num="",pin="",balance=""):
        #populate self.attributes for a bank account
        self.account_num = account_num
        self.pin = pin
        self.balance = balance
    
    def validate(self):
        #return True or False if an account num ad pin are in the data
        # TODO: add logic to open our data so we can check it
        if self.account_num in data:
            if data[self.account_num]["pin"] == self.pin:
                return True
        return False
    
    def load(self):
        # load the account with the objects self.account_num from the  datafile and set its attributes
        ser = Account(account_num="account num", pin="1234")
        if user.validate():
            user.load()

    def save(self):
        #update te json data with this accounts data either creating a new record or updating an existing 

        

# if choice == 'create account':
#     new_ac = Account()
#     new_ac.account_num = generate_account_num()
#     new_ac.pin = view.get_pin()
#     new_ac.balance = view.initial_deposit
#     new_ac.save()
#         pass