from gui import FinanceGUI
import tkinter as tk
from models import Transaction,Investment
from datamanager import DataManager
from transaction_manager import TransactionManager



if __name__ == "__main__":
    #Create root window

    root = tk.Tk()

    transaction = Transaction(Transaction_id="", Date="", Amount=0.0, Category="", Type="")
    investment = Investment(Name="", Type="", Current=0.0, PL=0.0, ROI=0.0)

    
    dm = DataManager(transaction,investment)

    tm = TransactionManager(dm,transaction)

   

    app = FinanceGUI(root,dm,tm)

    root.mainloop()