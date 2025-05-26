import uuid
from datamanager import DataManager
from models import Transaction

class TransactionManager:
    def __init__(self, data_manager: DataManager, transaction: Transaction):
        self.dm = data_manager
        self.transaction = transaction
    
    def transactionize(self, transaction_id, date, amount, category, transaction_type):
        return Transaction(
            Transaction_id=transaction_id,
            Date=date,
            Amount=float(amount),
            Category=category,
            Type=transaction_type
        )
    
    def validate_transaction(self, transaction):
        if not transaction.Date or not transaction.Category or not transaction.Type:
            return False
        if transaction.Amount <= 0:
            return False
        return True
    
    def add_transaction(self, transaction):
        if not self.validate_transaction(transaction):
            print("Invalid Transaction")
            return False
        
        transaction.Transaction_id = self.generate_unique_id()
        self.dm.add_transaction(transaction)
        return True
        
    def delete_transaction(self, transaction_id):
        self.dm.delete_transaction(transaction_id)
    
    def generate_unique_id(self):
        return str(uuid.uuid4())[:8]
    
    def update_transaction(self, transaction):
        if not self.validate_transaction(transaction):
            print("Invalid Transaction")
            return False
        
        self.dm.update_transaction(transaction)
        return True

    def find_total(self, transaction_type):
        transactions = self.dm.get_transactions()
        filtered = transactions[transactions["Type"] == transaction_type]
        return filtered["Amount"].sum() if not filtered.empty else 0.0