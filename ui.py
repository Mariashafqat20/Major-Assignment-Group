import tkinter as tk
from tkinter import ttk

class InventoryUI:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Smart Inventory System")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f0f0f0")
        self.var_id = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_category = tk.StringVar()
        self.var_quantity = tk.StringVar()
        self.var_price = tk.StringVar()
        self.var_search = tk.StringVar()

        self.setup_ui()
        def setup_ui(self):
        # Title
         title = tk.Label(self.root, text="Smart Inventory System", font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="white")
        title.pack(side=tk.TOP, fill=tk.X)
            def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Smart Inventory System", font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="white")
        title.pack(side=tk.TOP, fill=tk.X)

        # Input Frame (Left)
        input_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="white")
        input_frame.place(x=20, y=70, width=400, height=500)

        # Labels & Entries
        labels = ["Name", "Category", "Quantity", "Price"]
        vars = [self.var_name, self.var_category, self.var_quantity, self.var_price]

        for i, text in enumerate(labels):
            tk.Label(input_frame, text=text, font=("Arial", 12), bg="white").grid(row=i, column=0, pady=10, padx=20, sticky="w")
            tk.Entry(input_frame, textvariable=vars[i], font=("Arial", 12), bd=2, relief=tk.GROOVE).grid(row=i, column=1, pady=10, padx=20)

        # Buttons
        btn_frame = tk.Frame(input_frame, bg="white")
        btn_frame.place(x=10, y=350, width=380)
        tk.Button(btn_frame, text="Add", bg="green", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", bg="blue", fg="white").grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", bg="red", fg="white").grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Clear", bg="grey", fg="white").grid(row=0, column=3, padx=5)

        # Display Frame (Right)
        display_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE, bg="white")
        display_frame.place(x=440, y=70, width=540, height=500)

        # Table
        self.product_table = ttk.Treeview(display_frame, columns=("ID", "Name", "Category", "Qty", "Price"), show="headings")
        col_widths = [40, 140, 100, 70, 70]
        headers = ["ID", "Name", "Category", "Qty", "Price"]
        for col, width, head in zip(self.product_table["columns"], col_widths, headers):
            self.product_table.heading(col, text=head)
            self.product_table.column(col, width=width)
        self.product_table.place(x=10, y=60, width=515, height=420)
        self.product_table.bind("<ButtonRelease-1>", self.get_cursor)
        
        # Red tag for low stock
        self.product_table.tag_configure('low_stock', foreground='red')

    # === Logic Connections ===

