#!/usr/bin/env python3

import model_tt
import view_tt
from model_tt import Bankaccount
bank = model_tt.Bankaccount()

def run():
    bank.load()
    view_tt.main_menu()
    selection = view_tt.get_input()
    mainmenu(selection)

def mainmenu(selection):
    while True:
        if selection == '3':
            bank.save()
            exit()
        elif selection == '1':
            firstname = view_tt.First()
            lastname = view_tt.Last()
            genpin = view_tt.create_PIN()
            bank.create_account(firstname,lastname,genpin)
            bank.save()
            run()
        elif selection == '2':
            checkac = view_tt.login_ac()
            checkpin = view_tt.login_pin()
            if bank.login_verify(checkac,checkpin) == True:
                secondary() 
            else:
                run()
        else:
            view_tt.bad_input()
            run()

def secondary():
    view_tt.logged_in()
    selection2 = view_tt.get_secondinput()
    secondmenu(selection2,bank)

def secondmenu(selection2,bank):
    while True:
        if selection2 == '4':
            bank.save()
            exit()
        elif selection2 == '1':
            balance = bank.getBalance()
            view_tt.check_bal(balance)
            secondary()
        elif selection2 == '2':
            withdr = float(view_tt.withdraw())
            bank.withdrawal(withdr)
            bal = bank.getBalance()
            view_tt.new_bal(bal)
            bank.save()
            secondary()
        elif selection2 == '3':
            deps = float(view_tt.deposit())
            bal = bank.depositor(deps)
            view_tt.new_bal(bal)
            bank.save()
            secondary()
        else:
            view_tt.bad_input()
            run()

if __name__ == "__main__":
    run()