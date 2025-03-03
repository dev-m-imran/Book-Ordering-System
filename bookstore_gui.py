# Name = Muhammad Imran
# Student ID = 24821222

# Importing required libraries
# for validating email using regular expression
import re
# for building GUI 
import tkinter as tk
# for advanced widets and messagebox
from tkinter import ttk, messagebox
# for date and time
import datetime
# for bookstore operations importing logic 
from bookstore_core_inher import *


# Regular expression pattern to validate email addresses
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'



"""
The class BookOrderingSystem is main application class and it:
Initialize the root window
Set window title
Define window size
Initialize core data structures
List to store customer objects
List to store book objects
List to store order objects
Create an instance of BookStore class
Load the main page with tabs
"""
class BookOrderingSystem:
    def __init__(self, root):
        self._root = root
        self._root.title("Book Ordering System")
        self._root.geometry("600x600")
        
        self._customers = []
        self._books = []
        self._orders = []
        self._bookstores = BookStore()
        # self.invoices = Invoice()
        
        
        self.main_page()
    
    """ 
    This method creates a tabbed interface using Notebook widget
    It allow tabs to expand and fill space
    it has customer tab, book tab, order tab. invoice tab
    """  
    def main_page(self):
        #Creating tabs
        notebook = ttk.Notebook(self._root)
        notebook.pack(expand=True, fill="both")
        
        # Customer Tab
        customer_form = ttk.Frame(notebook)
        notebook.add(customer_form, text="Customer")
        self.inside_customer_form(customer_form)
        
        # Stock Tab
        book_form = ttk.Frame(notebook)
        notebook.add(book_form, text="Book")
        self.inside_book_form(book_form)
        
        # Order Tab
        order_form = ttk.Frame(notebook)
        notebook.add(order_form, text="Order")
        self.inside_order_form(order_form)
        
        # Invoice Tab
        invoice_tab = ttk.Frame(notebook)
        notebook.add(invoice_tab, text="Invoices")
        self.inside_invoice_tab(invoice_tab)
    
    """
    This method creates the form inside the customer tab
    It has a label Customer Form, Three entry fields Name, Phone and Email Address
    form also comes with 'Add Customer' button and 'Customer List'
    when 'Add Customer' button is pressed, it first checks the input fields
    if all input fields are correct, it adds customer details to 'Customer List'
    otherwise it will show an error.
    """
    def inside_customer_form(self, form):
        # Add header label for customer form
        label_main = tk.Label(form, text="Customer Form", font=("Arial", 20))
        label_main.pack(pady=10)
        
        # Create a frame for input fields
        frame_form = tk.Frame(form)
        frame_form.pack(pady=10)
        
        # Input field for customer name
        label_name = tk.Label(frame_form, text="Name")
        label_name.grid(row=0, column=0, padx=5, pady=5)
        self._customers_entry_name = tk.Entry(frame_form)
        self._customers_entry_name.grid(row=0, column=1, padx=5, pady=5)

        # Input field for customer phone number
        label_phone = tk.Label(frame_form, text="Phone Number")
        label_phone.grid(row=1, column=0, padx=5, pady=5)
        self._customers_entry_phone = tk.Entry(frame_form)
        self._customers_entry_phone.grid(row=1, column=1, padx=5, pady=5)

        # Input field for customer email address
        label_email = tk.Label(frame_form, text="Email Address")
        label_email.grid(row=2, column=0, padx=5, pady=5)
        self._customers_entry_email = tk.Entry(frame_form)
        self._customers_entry_email.grid(row=2, column=1, padx=5, pady=5)
        
        # Button to add a customer
        customer_btn = tk.Button(frame_form, text= "Add Customer", command=self.add_customers)
        customer_btn.grid(row=4, column=1, columnspan=2, pady=20)
        
        # Label for customers list section
        customer_list_label = tk.Label(form, text="Customers List", font=("Arial", 14))
        customer_list_label.pack(pady=10)
        
        # Header row for customers list
        header_frame = tk.Frame(form)
        header_frame.pack(pady=10)

        # Labels for headers in customers list
        hdr_label_1 = tk.Label(header_frame, text="Name", width=8)
        hdr_label_1.grid(row=0, column=0)
        hdr_label_2 = tk.Label(header_frame, text="Phone", width=16)
        hdr_label_2.grid(row=0, column=2)
        hdr_label_3 = tk.Label(header_frame, text="Email", width=20, anchor="w")
        hdr_label_3.grid(row=0, column=4)
        
        # Listbox to Display Customers
        self.customers_listbox = tk.Listbox(form, width=50, height=10,)
        self.customers_listbox.pack(pady=10)
    
        # Storage for Customers data
        self.customer = []  

    """
    This method is specifically for 'Add Customer' button, when button is pressed
    it check for condition and adds customers details to 'Customer List'
    the condition first check that if all the entry fields are present,
    the phone number is valid and check for valid email address
    if these condtions are true it will add details to list in a formated way
    it clears the entry fields after addition and also updates the customer dropdown menu in order management
    """
    def add_customers(self):
        # Get input values from fields
        name = self._customers_entry_name.get().strip()
        phone = self._customers_entry_phone.get().strip()
        email = self._customers_entry_email.get().strip()
        
        # Validate input fields
        if not name or not phone or not email:
            messagebox.showerror("Error", "All fields required!")
            return
        
        # Validate phone number
        if not phone.isdigit() or not (len(phone)>9 and len(phone)<13):
            messagebox.showerror("Error", "Invalid Phone number!")
            return
        
        # Validate email using regex
        if not re.match(email_pattern, email):
            messagebox.showerror("Error", "Invalid email address!")
            return
        
    
        # Format the data for Listbox
        formatted_customer = f"{name:<20} {phone:<15} {email:<30}"
        self.customers_listbox.insert(tk.END, formatted_customer)

        # Create a Customer object and store it in the list
        customer = Customer(name, phone, email)
        self._customers.append(customer)
        messagebox.showinfo("Success", f"Customer {name} added!")
        
        # Clear entry fields after successful addition
        self._customers_entry_name.delete(0, tk.END)
        self._customers_entry_phone.delete(0, tk.END)
        self._customers_entry_email.delete(0, tk.END)
        
        # Update dropdown for customers in order tab
        self.customer_dropdown['values'] = [c.get_name for c in self._customers]
    
    """
    This method creates the form inside the book tab
    It has a label Book Form, Three entry fields Book Name, Author and Price
    form also comes with 'Add Book' button and 'Books List'
    when 'Add Book' button is pressed, it first checks the input fields
    if all input fields are correct, it adds books details to 'Book List
    otherwise it will show an error.'
    """   
    def inside_book_form(self, form):
        # Add header label for book form
        label_book = tk.Label(form, text="Book Form", font=("Arial", 20))
        label_book.pack(pady=10)
        
        # Create a frame for input fields
        frame_form = tk.Frame(form)
        frame_form.pack(pady=10)
        
        # input field for book name
        label_book = tk.Label(frame_form, text="Book Name")
        label_book.grid(row=0, column=0, padx=5, pady=5)
        self.bookname_entry = tk.Entry(frame_form)
        self.bookname_entry.grid(row=0, column=1, padx=5, pady=5)   

        # input field for author name
        label_author = tk.Label(frame_form, text="Author")
        label_author.grid(row=1, column=0, padx=5, pady=5)
        self.author_entry = tk.Entry(frame_form)
        self.author_entry.grid(row=1, column=1, padx=5, pady=5)

        # input field for price
        label_price = tk.Label(frame_form, text="Price")
        label_price.grid(row=2, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(frame_form)
        self.price_entry.grid(row=2, column=1, padx=5, pady=5)

        # button to add customer
        book_btn = tk.Button(frame_form, text="Add Book", command=self.add_books)
        book_btn.grid(row=3, column=1, columnspan=2, pady=20)
        
        # label for customer list section
        book_list_label = tk.Label(form, text="Books List", font=("Arial", 14))
        book_list_label.pack(pady=10)
        
        # header row for book list
        header_frame = tk.Frame(form)
        header_frame.pack(pady=10)

        # labels for headers in book list
        hdr_label_1 = tk.Label(header_frame, text="Book name", width=8)
        hdr_label_1.grid(row=0, column=1)
        hdr_label_2 = tk.Label(header_frame, text="Author", width=16)
        hdr_label_2.grid(row=0, column=3)
        hdr_label_3 = tk.Label(header_frame, text="Price", width=20, anchor="w")
        hdr_label_3.grid(row=0, column=5)
        
        
        # Listbox to Display Books
        self.book_listbox = tk.Listbox(form, width=50, height=10,)
        self.book_listbox.pack(pady=10)
    
        # Storage for Books
        self.book = []
        
    """ 
    This method is for 'Add Book' button, when button is pressed
    it check for condition and adds book details to 'Book List'
    the condition first check that if all the entry fields are present
    and the price is valid
    if these condtions are true it will add details to list in a formated way
    it clears the entry fields after addition and also updates the book dropdown menu in order management
    """    
    def add_books(self):
        # get input values from entry fields
        bookname = self.bookname_entry.get().strip()
        author = self.author_entry.get().strip()
        price = self.price_entry.get().strip()
        
        # validate input entry field
        if not bookname or not author or not price:
            messagebox.showerror("Error", "All fields are required!")
            return

        # validate price
        try:
            price = float(price)
        except ValueError:
            messagebox.showerror("Error", "Invalid price!")
            return

        # formated version of book to display in list
        formatted_books = f"{bookname:<20} {author:<15} {price:<30}"
        self.book_listbox.insert(tk.END, formatted_books)
    
        # create a book object and store in list
        book = Stock(bookname, author, price)
        self._books.append(book)
        messagebox.showinfo("Success", f"Book {bookname} added!")
        
        # Clear entry fields after addition
        self.bookname_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        
        # updates dropdown for books in order tab
        self.book_dropdown['values'] = [b.get_Name for b in self._books]


    """ 
    This method creates the form inside the order tab
    inside order tab we have 'Order Placement' Label and two dropdown menu
    customer and input,
    three buttons place order, calculate shipping, generate invoice
    a checkbox urgent shipping
    for generating invoice shipping needs to be calculated
    for calculated shipment, placing order is necessary
    for placing order and calculating shipment dropdown menu needs to be filled 
    shipping cost is shown in form and invoice details is added to listbox in invoice tab
    also message of invoice is also showed
    """
    def inside_order_form(self, form):
        
        # add header label for order placement
        label_order = tk.Label(form, text="Order Placement", font=("Arial", 20))
        label_order.pack(pady=10)
        
        # create a frame for input fields
        frame_form = tk.Frame(form)
        frame_form.pack(pady=10)
        
        # dropdown menu for customers
        label_cstmr = tk.Label(frame_form, text="Customer")
        label_cstmr.grid(row=0, column=0, padx=5, pady=5)
        self.customer_dropdown = ttk.Combobox(frame_form, values=[c.get_name for c in self._customers])
        self.customer_dropdown.grid(row=0, column=1, padx=5, pady=5)

        # dropdown menu for books
        label_bk = tk.Label(frame_form, text="Book")
        label_bk.grid(row=1, column=0, padx=5, pady=5)
        self.book_dropdown = ttk.Combobox(frame_form,values=[b.get_Name for b in self._books])
        self.book_dropdown.grid(row=1, column=1, padx=5, pady=5)
        
        # button for placing order
        order_btn = tk.Button(frame_form, text="Place Order", command=self.place_order)
        order_btn.grid(row=2, column=0, columnspan=2, pady=10)

        # checkbox for urgent or regular shipment
        self.is_urgent = tk.BooleanVar()
        urg_check_btn = tk.Checkbutton(frame_form, text="Urgent Shipping", variable=self.is_urgent)
        urg_check_btn.grid(row=3, column=0, columnspan=2, pady=10) 
        
        # shipment button for calculating shipment cost
        shipping_btn = tk.Button(frame_form, text="Calculate Shipping", command=self.calculate_shipping)
        shipping_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
        # invoice button for generating invoices
        gen_invc_btn = tk.Button(frame_form, text="Generate Invoice", command= self.generate_invoice)
        gen_invc_btn.grid(row=5, column=0, columnspan=2, pady=10)

        # label to store shipment cost
        self.shipping_cost_label = tk.Label(frame_form, text="")
        self.shipping_cost_label.grid(row=6, column=0, columnspan=2, pady=10)
        
    """ 
    This method is for 'Place Order button'
    when button is pressed it checks for certain condition and placed the order
    for placing order both customer name and book name needs to be selected
    if either of them is not selected it will show an error.
    """
    def place_order(self):
        
        # get the selected customer and book from dropdown menus
        customer_name = self.customer_dropdown.get()
        book_name = self.book_dropdown.get()

        # find the customer and book matching the selected name
        customer = next((c for c in self._customers if c.get_name == customer_name), None)
        book = next((b for b in self._books if b.get_Name == book_name), None)

        # if one of the dropdown is not selected, displays an error
        if not customer or not book:
            messagebox.showerror("Error", "Select a valid customer and book!")
            return

        # create an order object and save for later operations
        order = Order(customer_name, book_name)
        self.placing_order = order
        messagebox.showinfo("Success", 
                            f"Order placed successfully")
        
        
    """ 
    This method is for 'Calculate shipping' button
    when button is pressed it check that order is placed or not
    if yes it'll further check the urgent checkbox if urgent checkbox is marked 
    it'll calculate shipping as urgent, otherwise it'll calculate as normal
    """ 
    def calculate_shipping(self):
        # checks if order is placed or not
        if  hasattr(self, 'placing_order'):
            # Get the selected customer and book from dropdown menus
            customer_name = self.customer_dropdown.get()
            book_name = self.book_dropdown.get()

            customer = next((c for c in self._customers if c.get_name == customer_name), None)
            book = next((b for b in self._books if b.get_Name == book_name), None)

            if not customer or not book:
                messagebox.showerror("Error", "Select a valid customer and book!")
                return

            order = Order(customer, book)
            shipping = Shipping(order, datetime.date.today())
            shipping.calc_ship_cost(self.is_urgent.get())

            # store the shipping object for invoice generation
            self.current_shipping = shipping
            self.shipping_cost_label.config(text=f"Shipping Cost: £{shipping._ship_cost:.2f}")
        else:
            messagebox.showerror("Error", "Please place the order first!" )
            return

        self.customer_dropdown.set("")
        self.book_dropdown.set("")

    """ 
    This method is for 'Generate Invoice'
    when it pressed, it checks that whether the shipping cost is calculated or not
    if shipping cost is calculated, it'll generate an invoice and add to invoice list
    in the invoice tab and also displays a message of invoice details
    """    
    def generate_invoice(self):
        # check if shipping has been calculated
        if not hasattr(self, 'current_shipping'):
            messagebox.showerror("Error", "Please calculate shipping first!")
            return

        # generate an invoice numbee
        invoice_number = f"INV{len(self._bookstores.get_invoices) + 1:04d}"
        invoice = Invoice(invoice_number, self.current_shipping._order._stock, self.current_shipping)
        self._bookstores.addInvoice(invoice)

        self.shipping_cost_label.config(text="")
        # display a message showing invoice details
        messagebox.showinfo(
            "Invoice Generated",
            f"Invoice: {invoice_number}\n"
            f"Book: {self.current_shipping._order._stock.get_Name}\n"
            f"Total Cost: £{invoice.invoice():.2f}\n"
            f"Date: {self.current_shipping._ship_date}"
            )
        return 
        
    """ 
    this method is for creating form inside the invoice tab
    it has label at the top and a listbox to store invoices
    a button 'View all invoices' which when clicked show the invoices in the list
    a frame including search invoice label, an entry field for invoice
    and a button to search a particular invoice. 
    """
    def inside_invoice_tab(self, form):
        
        # add header label for invoice management
        invc_label = tk.Label(form, text="Invoice Management", font=("Arial", 20))
        invc_label.pack(pady=10) 
        
        # add label for invoice list
        list_hd_label = tk.Label(form, text="Invoice List", font=("Arial", 14))
        list_hd_label.pack(pady=10)
        
        # create a frame for header label
        header_frame = tk.Frame(form)
        header_frame.pack(pady=10)
    
        # header label for invoice list
        hdr_label_1 = tk.Label(header_frame, text="Invoice #", width=8)
        hdr_label_1.grid(row=0, column=4)
        hdr_label_2 = tk.Label(header_frame, text="Product", width=8)
        hdr_label_2.grid(row=0, column=6)
        hdr_label_3 = tk.Label(header_frame, text="Cost", width=12, anchor="w")
        hdr_label_3.grid(row=0, column=8)
        hdr_label_4 = tk.Label(header_frame, text="Date", width=16, anchor="w")
        hdr_label_4.grid(row=0, column=11)
        
        # listbox to display invoices
        self.invoices_listbox = tk.Listbox(form, width=50, height=15)
        self.invoices_listbox.pack(pady=10)

        # button to view all invoices
        view_invc_btn = tk.Button(form, text="View All Invoice", command=self.view_all_invoices)
        view_invc_btn.pack(pady=5)
        
        # frame for searching invoices
        search_form = tk.Frame(form)
        search_form.pack(pady=10)
        
        # label and entry field for searching invoices
        sch_label = tk.Label(search_form, text="Search Invoices")
        sch_label.grid(row=0, column=0, padx=5, pady=5)
        self.invoice_search_entry = tk.Entry(search_form)
        self.invoice_search_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # button to search invoices
        srch_invc_btn = tk.Button(search_form, text="Search", command=self.search_invoice)
        srch_invc_btn.grid(row=0, column=2, padx=5, pady=5)
        
    """
    This method is for 'View all Invoices' button 
    when button is pressed it first check that whether the invoices are generated or not
    if yes then it'll display all the invoice.
    """ 
    def view_all_invoices(self):
        # clear listbox first and get invoices and display them
        self.invoices_listbox.delete(0, tk.END)
        invoices = self._bookstores.get_invoices  # Assuming this returns a list of all invoices
        if not invoices:
            messagebox.showerror("Error", "No invoice is generated!")
            return
        for invoice in invoices:
            self.invoices_listbox.insert(
                tk.END,
                f"{invoice.getinvoice_nbr} - {invoice._stock.get_Name} - £{invoice.invoice():.2f} - {invoice._ship_order._ship_date}"
            )


    """
    This method is for 'search invoice' button
    when button is pressed it first check that whether the invoices are generated or not
    if yes then it'll look for invoices in list, if invoice is present,it'll display that
    otherwise in any case it'll display an error
    """
    def search_invoice(self):
        # get invoice number from the search field
        invoice_number = self.invoice_search_entry.get().strip()
        if not invoice_number:
            messagebox.showerror("Error", "Please enter an invoice number to search!")
            return

        invoices = self._bookstores.get_invoices
        # validating in case of no invoice is generated
        if not invoices:
            messagebox.showerror("Error", "No invoice is generated!")
            return
        invoice = Invoice(invoice_number, self.current_shipping._order._stock, self.current_shipping)
        # Search for the invoice in the stored invoices
        found_invoice = next((inv for inv in invoices if inv.getinvoice_nbr == invoice_number), None)

        if found_invoice:
            self.invoices_listbox.delete(0, tk.END)
            self.invoices_listbox.insert(
                tk.END,
                f"{invoice.getinvoice_nbr} - {invoice._stock.get_Name} - £{invoice.invoice():.2f} - {invoice._ship_order._ship_date}"
            )
            messagebox.showinfo(
                "Success", "Invoice number found!\n"
                f"Invoice: {invoice_number}\n"
                f"Book: {self.current_shipping._order._stock.get_Name}\n"
                f"Total Cost: £{invoice.invoice():.2f}\n"
                f"Date: {self.current_shipping._ship_date}"
            )
        else:
            messagebox.showerror("Error", f"Invoice {invoice_number} not found!")

# runs the program
if __name__ == "__main__":
    root = tk.Tk()
    app = BookOrderingSystem(root)
    root.mainloop()