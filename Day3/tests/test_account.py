from unittest import TestCase
from app.model import Account

import os

Account.filepath = "_test.json"

class TestAccount(TestCase):

    def setUp(self): #always need this set up function to define functions
        mikebloom = Account("mikebloom") #Account is an object
        mikebloom.balance = 1000.0
        mikebloom.pin = 1234
        mikebloom.save()

    def testLogin(self):
        mike = Account.login("mikebloom","1234")
        self.assertIsInstance(mike,Account,"login loads an Account object with good credentials") #basically says login does what it shoul
        notmike = Account.login("mikebloom","1111")
        self.assertIsNone(notmike,"login returns None for bad credentials") #check if Account.login is returning None due to bad credentials

    def testNewAccount(self):
        greg = Account("greg")
        greg.balance = 9.0
        greg.pin = "9999"
        greg.save()

        greg2 = Account.login("greg","9999") #if we can login and data (balance) exists then function working correctly
        self.assertEqual(greg2.balance,greg.balance,"saved account can be loaded")

    def testWithdraw(self):
        mike = Account.login("mikebloom","1234") 
        mike.withdraw(500.0)
        self.assertAlmostEqual(mike.balance, 500.0,"withdraw accurately changes balance")
         #testing whether the withdraw function works by subtracting $500 from initial bal
    
    def testDeposit(self):
        mike = Account.login("mikebloom","1234") 
        mike.deposit(20.0)
        self.assertAlmostEqual(mike.balance, 1020.0,"deposit accurately changes balance")

    def testSaveOldAccount(self):
        mike = Account.login("mikebloom","1234")
        mike.deposit(100.0)
        mike.save()
        #see if we have saved the account object to see if function actually working
        newmike = Account.login("mikebloom","1234")
        self.assertAlmostEqual(newmike.balance, 1100.0,"accounts updated by save")
    
    def tearDown(self):
        pass 