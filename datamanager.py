import pandas as pd
import os 
from models import Investment, Transaction


class DataManager:
    def __init__(self, transaction: Transaction, investment: Investment):
        self.transaction_path = 'transactions.csv'
        self.investment_path = 'investments.csv'
        self.transaction = self.load_transaction_data()
        self.investment = self.load_investment_data()

    def load_transaction_data(self):
        if os.path.exists(self.transaction_path):
            return pd.read_csv(self.transaction_path)
        return pd.DataFrame(columns=['Transaction Id', 'Date', 'Amount', 'Category', 'Type'])

    def load_investment_data(self):
        if os.path.exists(self.investment_path):
            return pd.read_csv(self.investment_path)
        return pd.DataFrame(columns=['Name', 'Type', 'Current', 'PL', 'ROI'])

    def save_transaction(self):        
        self.transaction.to_csv(self.transaction_path, index=False)

    def add_transaction(self, transaction):
        new_transaction = pd.DataFrame([transaction.__dict__])

        if self.transaction.empty:
            self.transaction = new_transaction
        else:
            new_transaction = new_transaction.reindex(columns=self.transaction.columns)
            self.transaction = pd.concat([self.transaction, new_transaction], ignore_index=True)
            
        self.save_transaction()
        print("Transaction added")

    def get_transactions(self):
        return self.transaction
    
    def delete_transaction(self, transaction_id):
        self.transaction = self.transaction[self.transaction["Transaction Id"] != transaction_id]
        self.save_transaction()

    def update_transaction(self, transaction):
        transaction_id = transaction.Transaction_id
        self.delete_transaction(transaction_id)
        self.add_transaction(transaction)