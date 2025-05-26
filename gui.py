import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from models import Transaction
from transaction_manager import TransactionManager


class FinanceGUI:
    def __init__(self, root, data_manager, transactionmanager):
        self.root = root
        self.dm = data_manager
        self.tm = transactionmanager

        self.root.title("FinTrack")
        self.root.geometry("900x700")

        self.setup_ui()

    def setup_ui(self):
        # Create side bar Frame
        self.side_bar_frame = tk.Frame(self.root, bg="#E3D2C3", width=200, height=700)
        self.side_bar_frame.grid(row=0, column=0, sticky="ns")

        buttons = ["Dashboard", "Transactions", "Investments", "Budget", "Reports"]

        for btn in buttons:
            button = tk.Button(self.side_bar_frame, text=btn, font=("Arial", 12), bg="#EAEAEA",
                               command=lambda b=btn: self.switch_view(b))
            button.pack(pady=30, padx=10, fill="x")

        # Main Frame
        self.mainframe = tk.Frame(self.root, bg="#66D2CE", width=400, height=700)
        self.mainframe.grid(row=0, column=1, sticky="nswe")

        self.root.columnconfigure(1, weight=1)  # Allow mainframe to expand
        self.root.rowconfigure(0, weight=1)

        self.load_dashboard()

    def load_dashboard(self):
        # Title Label
        self.title_label = tk.Label(self.mainframe, text="Financial Overview", font=("Arial", 16, "bold"), bg="#66D2CE")
        self.title_label.pack(pady=20, fill="x", anchor="n")

        # Income Label
        self.income_label = tk.Label(self.mainframe, text=f"Total Income: {self.tm.find_total('Income')}",
                                     font=("Arial", 14, "bold"), bg="#66D2CE")
        self.income_label.pack(padx=20, pady=40, anchor="w")

        # Expense Label
        self.expenses_label = tk.Label(self.mainframe, text=f"Total Expenses: {self.tm.find_total('Expenses')}",
                                       font=("Arial", 14, "bold"), bg="#66D2CE")
        self.expenses_label.pack(padx=20, pady=20, anchor="w")

    def clear_mainframe(self):
        for widget in self.mainframe.winfo_children():
            widget.destroy()

    def switch_view(self, view_name):
        ''' Clear current widget '''
        self.clear_mainframe()

        if view_name == "Dashboard":
            self.load_dashboard()
        elif view_name == "Transactions":
            self.load_transactions()
        elif view_name == "Investments":
            self.load_investment()
        elif view_name == "Budget":
            self.load_budget()
        elif view_name == "Reports":
            self.load_reports()

    def load_transactions(self):
        
        self.create_title(self.mainframe, "Transactions")
        self.create_input_frame()
        self.create_transaction_list()      

        

        

        

        

    def create_input_frame(self):
        # Transaction Input Frame
        input_frame = tk.Frame(self.mainframe, bg="#66D2CE")
        input_frame.pack(pady=10, fill='x')

        self.create_amount_widget(input_frame)
        self.create_category_widget(input_frame)
        self.create_date_widget(input_frame)
        self.create_transaction_type_widget(input_frame)
        self.create_add_button(input_frame,self.get_transaction)


    def create_amount_widget(self,frame):
        # Amount Label
        amount_label = tk.Label(frame, text="Amount:", bg="#66D2CE", font=("Arial", 14))
        amount_label.grid(row=0, column=0, padx=10, pady=5)

        # Amount Entry
        self.amount_entry = tk.Entry(frame, font=("Arial", 12))
        self.amount_entry.grid(row=0, column=1, padx=10)

    def create_category_widget(self,frame):
        # Category Label
        category_label = tk.Label(frame, text="Category", bg="#66D2CE", font=("Arial", 14))
        category_label.grid(row=0, column=2, padx=10, pady=5)

        # Category Dropdown
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(
            frame,
            textvariable=self.category_var,
            values=['Food', 'Rent', 'Transport', 'Salary', 'Other'],
            font=('Arial', 14)
        )
        self.category_dropdown.grid(row=0, column=3, padx=10, pady=5)

    def create_date_widget(self,frame):
        # Date Label
        self.date_label = tk.Label(
            frame,
            text="Date:",
            bg="#66D2CE",
            font=("Arial", 14)
        )
        self.date_label.grid(row=1, column=0, padx=10, pady=5)

        # Date Entry
        self.date_entry = DateEntry(frame, font=("Arial", 12), date_pattern="yyyy-mm-dd")
        self.date_entry.grid(row=1, column=1, padx=10, pady=5)
    
    def create_transaction_type_widget(self,frame):
        # Type Label
        type_label = tk.Label(
            frame,
            text="Type",
            bg="#66D2CE",
            font=("Arial", 14)
        )
        type_label.grid(row=2, column=0, padx=5)

        # Type Entry
        self.type_var = tk.StringVar()
        self.type_dropdown = ttk.Combobox(
            frame,
            text=self.type_var,
            values=["Expenses", "Investment", "Income"],
            font=("Arial", 14)
        )
        self.type_dropdown.grid(row=2, column=1, padx=10, pady=5)

    def create_add_button(self,frame,function):
        # Add Button
        add_button = tk.Button(
            frame,
            text="Add Transaction",
            font=("Arial", 12),
            command=function
        )
        add_button.grid(row=1, column=2, columnspan=2, pady=10)

    def create_transaction_list(self):
        # Transaction List Session
        list_frame = tk.Frame(self.mainframe, bg="#66D2CE")
        list_frame.pack(fill="both", expand=True, pady=10)

        transaction_list_label = tk.Label(
            list_frame,
            text="Transaction List",
            bg = "#66D2CE",
            font = ("Arial", 14, "bold")

        )
        transaction_list_label.pack(padx=5,pady=5)

        columns = ("Transaction Id", "Date", "Amount", "Category", "Type")
        self.transaction_tree = ttk.Treeview(
            list_frame,
            columns=columns,
            show="headings",
            height=10,
        )

        for cols in columns:
            self.transaction_tree.column(cols,anchor="center")
            self.transaction_tree.heading(cols, text=cols, anchor="center")
                          
        
         #Add vertical scroll bar
        v_scroll_bar = ttk.Scrollbar(list_frame, orient="vertical", command=self.transaction_tree.yview)
        v_scroll_bar.pack(side="right", fill="y")

        #Adding Horizontal scrollbar
        h_scroll_bar = ttk.Scrollbar(list_frame, orient="horizontal", command=self.transaction_tree.xview)
        h_scroll_bar.pack(side="bottom", fill="x")



 
        self.transaction_tree.configure(yscrollcommand=v_scroll_bar.set, xscrollcommand=h_scroll_bar.set)
        self.transaction_tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Context Menu
        self.context_menu = tk.Menu(list_frame, tearoff=0)
        self.context_menu.add_command(label="Edit", command=self.edit_transaction)
        self.context_menu.add_command(label="Delete", command=self.delete_transaction)

        # Binding Context menu to table
        self.transaction_tree.bind("<Button-3>", self.show_context_menu)

        # Load existing transactions into the table
        self.refresh_transaction_list()



    def show_context_menu(self, event):
        selected_item = self.transaction_tree.identify_row(event.y)
        if selected_item:
            self.transaction_tree.selection_set(selected_item)
            self.context_menu.post(event.x_root, event.y_root)

    def delete_transaction(self):
        selected_item = self.transaction_tree.selection()
        if selected_item:
            for item in selected_item:
                values = self.transaction_tree.item(item, "values")
                if not values:
                    print("Error could not take values")
                    return
                transaction_id = values[0]
                self.tm.delete_transaction(transaction_id)
            self.refresh_transaction_list()

    def edit_transaction(self):
        ''' Editing transaction '''
        selected_item = self.transaction_tree.selection()
        if not selected_item:
            self.message_box("Transaction not found")
            return

        values = self.transaction_tree.item(selected_item, "values")
        if not values:
            self.message_box("Transaction is empty")
            return

        # Getting Transaction id
        transaction_id = values[0]

        # Create Edit Window
        self.edit_window = tk.Toplevel(self.root,bg="#66D2CE")
        self.edit_window.title("Edit Transaction")
        self.edit_window.geometry("700x300")

        self.create_amount_widget(self.edit_window)
        self.create_category_widget(self.edit_window)
        self.create_date_widget(self.edit_window)
        self.create_transaction_type_widget(self.edit_window)

        save_button = tk.Button(
            self.edit_window,
            text="Save",
            font=("Arial", 12),
            command=lambda: self.update_transaction(transaction_id)
        )
        save_button.grid(row=4, column=1, padx=10, pady=10)

    def refresh_transaction_list(self):
        for row in self.transaction_tree.get_children():
            self.transaction_tree.delete(row)

        # Add transactions from DataManager
        transactions = self.dm.get_transactions()
        for _, transaction in transactions.iterrows():
            self.transaction_tree.insert("", "end", values=(
                transaction["Transaction Id"],
                transaction["Date"],
                f"${transaction['Amount']:.2f}",
                transaction["Category"],
                transaction["Type"],

            ))
        

    def get_transaction(self, tm.Transaction=None):
        try:
            self.tm.Transaction.Amount = float(self.amount_entry.get())
            self.tm.Transaction.Date = self.date_entry.get_date()
            self.tm.Transaction.Category = self.category_var.get()
            self.tm.Transaction.Type = self.type_var.get()
            
            if transaction_id is None:
                self.tm.Transaction.Transaction_id = self.tm.generate_unique_id()
            
            
            
            if self.tm.add_transaction(transaction):
                self.amount_entry.delete(0, tk.END)
                self.category_var.set("")
                self.date_entry.set_date(None)
                self.type_var.set("")
                self.refresh_transaction_list()
        except ValueError:
            self.message_box("Please enter a valid amount")

    def message_box(self, message):
        message_window = tk.Toplevel(self.root)
        message_window.title("Message")
        message_window.geometry("400x200")

        message_label = tk.Label(
            message_window,
            text=message,
            font=("Arial", 12)
        )
        message_label.pack(pady=10, padx=5)

    def update_transaction(self, transaction_id):
        
        amount = self.amount_entry.get()
        category = self.category_var.get()
        date = self.date_entry.get_date()
        transaction_type = self.type_var.get()
        transaction = self.tm.transactionize(transaction_id, date, amount, category, transaction_type)
        self.tm.update_transaction(transaction)
        self.edit_window.destroy()
        self.edit_window = None
        self.refresh_transaction_list()


    def create_title(self, frame , title):
         # Title Label
        self.title_label = tk.Label(frame, text=title, font=("Arial", 16, "bold"), bg="#66D2CE")
        self.title_label.pack(pady=20, fill="x", anchor="n")

    def create_sub_title(self,frame, subtitle):
        self.title_label = tk.Label(frame, text=subtitle, font=("Arial", 14, "bold"), bg="#66D2CE")
        self.title_label.pack(pady=20, fill="x", anchor="w")


        

    def load_investment(self):
        # Title Label         
        self.create_title(self.mainframe,"Investments")
        self.create_sub_title(self.mainframe, "Your Portfolio")
        self.create_portfolio_frame()
        self.create_portfolio_list()






    def show_values(self,frame, value_name, value,**kwargs):
        grid_values = {
            "row"  : None,
            "column" : None,
            "padx" : None,
            "pady" : None,
            "font" : ("Arial", 12, "bold"),
            "bg" : "#66D2CE",
            "sticky" : "w",
            "anchor" : "w"

        }

        grid_values.update(kwargs)
        values_label = tk.Label(
            frame,
            text = f"{value_name} : {value}",
            font = grid_values["font"],
            bg = grid_values["bg"],
            anchor= grid_values["anchor"]
            )
        values_label.grid(row=grid_values["row"],column=grid_values["column"], padx=grid_values["padx"], pady=grid_values["pady"],sticky=grid_values["sticky"] )

    def create_portfolio_frame(self):
        portfolio_frame = tk.Frame(self.mainframe,bg="#66D2CE")
        portfolio_frame.pack(padx=5, pady=10, fill="x", anchor="w")
        self.show_values(portfolio_frame, "Total Value", 0, row= 0, column=0, padx=5,pady=5, anchor="w")
        self.show_values(portfolio_frame, "Allocation", 0, row=1,column=0, padx =5, pady= 5, anchor="w")


    def create_portfolio_list(self):
        #Creating Portfolio List
        portfolio_list_frame = tk.Frame(self.mainframe,bg="#66D2CE")
        portfolio_list_frame.pack(padx=5,pady=10, fill="x")

        #Columns

        columns = ("Asset", "Type", "Current", "P/L", "ROI")

        self.portfolio_tree = ttk.Treeview(
            portfolio_list_frame,
            columns= columns,
            show= "headings",
            height= 10,
            

        )

        for cols in columns:

            self.portfolio_tree.column(cols, anchor="center")
            self.portfolio_tree.heading(column=cols, text=cols, anchor="center")
        
        self.portfolio_tree.pack(padx=5,pady=5, fill="x")








      

    def load_budget(self):
        # Title Label
        self.create_title(self.mainframe, "Budget")
        #Budget Overview 

    def load_reports(self):
        # Title Label
        self.create_title(self.mainframe, "Reports")

    