from datamanager import DataManager
from models import Investment

class InvestmentManager:

    def __init__(self, data_manager:DataManager):
        
        self.dm = data_manager
    

    def add_investment(self):

        self.dm.add_investment()
