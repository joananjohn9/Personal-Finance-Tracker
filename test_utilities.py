import tkinter as tk
from tkinter import messagebox

class FinanceTracker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Personal Finance Tracker")

    def test_ui(self):
        # Test the user interface
        self.window.geometry("500x500")
        label = tk.Label(self.window, text="Personal Finance Tracker")
        label.pack()
        button = tk.Button(self.window, text="Add Transaction", command=self.add_transaction)
        button.pack()
        self.window.mainloop()

    def add_transaction(self):
        # Add a new transaction
        transaction_window = tk.Toplevel(self.window)
        transaction_window.title("Add Transaction")
        # Add input fields and buttons to the transaction window
        label = tk.Label(transaction_window, text="Transaction Amount:")
        label.pack()
        entry = tk.Entry(transaction_window)
        entry.pack()
        button = tk.Button(transaction_window, text="Add", command=lambda: self.save_transaction(entry.get()))
        button.pack()

    def save_transaction(self, amount):
        # Save the transaction
        # Save the transaction to a file or database
        # For now, just print the transaction amount
        print("Transaction amount:", amount)

finance_tracker = FinanceTracker()
finance_tracker.test_ui()