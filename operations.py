import pandas as pd
from datamanager import DataManager
import uuid

class FinanceOperations:

    def __init__(self,data_manager):
        
        self.dm = data_manager
    
    def transactionize(self, transaction_id,date, amount, category, transaction_type):
        if transaction_id == None:
            transaction_id = self.generate_unique_id()
        
        transaction = {
            "Transaction Id" : transaction_id,
            "Date" : date,
            "Amount" : float(amount),
            "Category" : category,
            "Type" : transaction_type
        }

        return transaction
    
    def validate_transaction(self, transaction):

        if not transaction.get("Amount") or float(transaction.get("Amount")) <= 0 :
            print("Invalid Amount")
            return False
        elif not transaction.get("Date") :
            print("Please enter the Date")
            return False
        elif not transaction.get("Category"):
            print("Please enter the category")
            return False
        elif not transaction.get("Type"):
            print("Please Enter Type")
        
        return True
    
    def add_transaction(self,transaction):

        #Validate transaction
        if not self.validate_transaction(transaction):
            print("Invalid Transaction")
            return  False
        else :
            self.dm.add_transaction(transaction)
            return True
        
    def delete_transaction(self, transaction_id):
        self.dm.delete_transaction(transaction_id)
    

    def generate_unique_id(self):
        ''' Generate unique id'''
        return str(uuid.uuid4())[:8]
    

    def update_transaction(self,transaction):
        #Validate Transaction
        if not self.validate_transaction(transaction):
            print("Invalid Transaction")
        else:
            self.dm.update_transaction(transaction)




    def find_total(self,type):
        self.total_income = self.dm.transaction[self.dm.transaction["Type"] == type]["Amount"].sum()
        return self.total_income
    

 
               
    