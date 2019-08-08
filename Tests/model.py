import json


class Account:
    filepath = "data.json"

    def __init__(self,username):
        self.username = username
        self.pin =  None
        self.balance = 0.0
        self.data = {}
        self.load() #everytime you call the init you load the data
    
    def load(self):
        try:
            with open(self.filepath) as json_file:
                self.data = json.load(json_file)
        
        except FileNotFoundError:
            pass #cant use continue as it only works for looping behaviour
        
        if self.username in self.data:
            self.balance = self.data[self.username]["balance"]
            self.pin = self.data[self.username]["pin"] #if username exists, load the balance and pin

    def save(self):
        self.data[self.username] = {
            "balance": self.balance,
            "pin": self.pin
        }

        with open(self.filepath,'w') as json_file:
            json.dump(self.data,json_file)

    def withdraw(self,amount):
        if amount > self.balance:
            self.balance -= amount
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    
    @classmethod
    def login(cls,username,pin): #cls calls the init method to create an instance, either get good instance or return None
        account = cls(username)
        if pin != account.pin:
            return None
        else:
            return account 
        