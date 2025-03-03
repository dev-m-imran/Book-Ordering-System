# Name = Muhammad Imran
# Student ID = 24821222


# This is to import the datetime module to use date and time
import datetime


"""
The class Customer is for adding information for customer such as name, phone number and email address
Each attribute has a getter and setter method
"""
class Customer:
  # this constructor intitalize details of customer having name, phone, email attributes
  def __init__(self, name: str, phone: str, email:str):
    self._name = name
    self._phone = phone
    self._email = email 
    
  """
  getter for customer's name which access the attribute name 
  returns customer's name
  """
  @property
  def getname(self):
    return self._name
  
  """
  setter for the customer's name
  updates or changes the customer name where needed or valid
  """
  @getname.setter
  def setname(self, name):
      self._name = name
  
  """
  getter for customer's phone number accessing phone attribute
  returns the phone number
  """
  @property
  def getphone(self):
    return self._phone
  
  """
  setter for phone number  
  update the phone
  """
  @getphone.setter
  def setphone(self, phone):
    self._phone = phone
  
  """
  getter for email address
  returns customers email
  """
  @property
  def getemail(self):
    return self._email
  
  """
  setter for customer email address
  updates the customer's email
  """
  @getemail.setter
  def setemail(self, email):
    self._email = email  
    

"""
the class Stock is for managing stock information for books such as book name, author and price
has a getter and setter method for each attribute
"""
class Stock:
  # constructor to intilize book name, author and price attributes
  def __init__(self, book_name: str, author: str, price: float):
    self._book_name = book_name
    self._author = author
    self._price = price
    
  """
  getter for bookname 
  return book name
  """
  @property
  def getbook_name(self):
    return self._book_name
  
  """
  setter for book name
  this will update the book name if valid
  """
  @getbook_name.setter
  def set_book_name(self, book_name):
    self._book_name = book_name
    
  """
  getter for author name 
  returns the author name
  """
  @property
  def getauthor(self):
    return self._author
  
  """
  setter for author name
  updates the author name
  """
  @getauthor.setter
  def setauthor(self, author):
    self._author = author
    
  """
  getter for price of book
  returns the price 
  """
  @property
  def getprice(self):
    return self._price
  
  """
  setter for price
  updates the price
  """ 
  @getprice.setter
  def setprice(self, price):
    self._price = price
    

"""
the class Order controls the orders using class Customer and Stock
constructor has two atrributes, order object of Order class
and stock Object of Stock class
"""
class Order:
  """  
  #constructor to initialize order details,
  here attributes are objects of previous classes such as 
  customer is object of Customer class and stock is object of Stock class"""
  def __init__(self, customer: Customer, stock: Stock):
    self._customer = customer
    self._stock = stock
    
  """
  getter for customer
  returns the customer
  """ 
  @property
  def getcustomer(self):
    return self._customer
  
  """
  getter for stock
  returns stock
  """
  @property
  def getstock(self):
    return self._stock
  
    

"""
the class Shipping is for shipping and it's details
class has class level attribute count_urgent
constructor has two atrributes order object of Order and
ship_date to use date from the imported datetime module
"""
class Shipping:
  # Class-level attribute to count the number of urgent shipments
  count_urgent = 0
  """
  this constructor is for intializing shipping details
  attribute order is object of class Order 
  attribute ship_date gives the date from the module imported at the top
  """
  def __init__(self, order: Order, ship_date: datetime.date):
    self._order = order
    self._ship_date = ship_date
    self._ship_cost = 0.0
  
  """
  getter for shipping date 
  return the date of shipping
  """
  @property
  def getship_date(self):
    return self._ship_date
  

  """
  getter for the shipping cost
  return the cost of shipping
  """
  @property
  def getship_cost(self):
    return self._ship_cost
  
  """
  setter for shipping cost
  updates the shipping cost
  """
  @getship_cost.setter
  def set_ship_cost(self, ship_cost):
    self._ship_cost = ship_cost
    
  """
  method to calculate the shipping cost
  checks if the shipping is urgent or not
  if it is urgent then program will go in if
  Set a high shipping cost for urgent shipping equals 5.45
  update the class-level variable by incrementing if shipment is urgent
  if shipment is not urgent the program go in else
  set a low cost for normal shipping equals 3.95
  returns the calculate shipping charges either 5.45 or 3.95
  """
  def calc_ship_cost(self, is_urgent: bool):
    if is_urgent:
      self._ship_cost = 5.45
      Shipping.count_urgent += 1
    else:
      self._ship_cost = 3.95
    return self._ship_cost
  

"""
the class Invoice is for generating and managing the invoices
has a constructor having attributes, invoice_nbr, stock, ship_order
has a getter for invoice_nbr
method to calculate the total cost
"""
class Invoice:
  """
  the constructor intializing the attributes for Invoice
  the attribute stock is the object of class Stock
  ship_order is the attribute of class Shipping
  self.total_cost is to intialize the total cost
  """
  def __init__(self, invoice_nbr: str, stock: Stock, ship_order: Shipping):
    self._invoice_nbr = invoice_nbr
    self._stock = stock
    self._ship_order = ship_order
    self.total_cost = 0.0
  
  
  """
  getter for the invoice number
  returns the invoice number
  """
  @property
  def getinvoice_nbr(self):
    return self._invoice_nbr
    
  """
  this method is to calculate the total cost of order for invoice
  check if the stock and shipping order is present
  calculate the total cost from price of book in stock and shipping cost from shipping order
  updates the above intialize total cost
  returns the total cost
  """
  def invoice(self):
    if self._stock and self._ship_order:
      self.total_cost = self._stock.setprice + self._ship_order._ship_cost
    return round(self.total_cost, 2)
  

""" 
The class BookStore is to manage the invoices in diferrent ways:
adding invoices to a list
searching invoice from the list
and printing message if the invoice is not in the list
"""
class BookStore:
  """  
  constructor to intialize BookStore attributes
  empty list to store invoices
  default message for missing invoices
  """
  def __init__(self):
    self._invoices = []
    self.message = "Invoices not found"
    
  """ 
  getter for the invoices list
  returns the list of invoices
  """
    
  @property
  def get_invoices(self):
    return self._invoices
  
  """
  this method is to add invoices to the list(self_invoices)
  append the invoice to the list
  """
  def addInvoice(self, invoice):
    self._invoices.append(invoice)
    
  """
  this method is to search invoices by it's number by using given attributes
  iterate through the list of invoices(self._invoices)
  checks if the current invoice matches the invoice we want to search
  returns the matching invoice
  print the message if no matching invoice is found
  """
  def search_invoice(self, nbr):
    for invoice in self._invoices:
      if invoice == nbr:
        return invoice
    print(self.message)
    return None

  
# this class is to test the functionality of the program
class Test:
  def main():
    
    # Creating customer instances with name, phone, and email
    customer1 = Customer("imran", "28254455", "imran@gmail.com")
    print(f"Customer1({customer1._name}, {customer1._phone}, {customer1._email})")
    customer2 = Customer("Abdul", "07863016121","abdul@gmail.com")
    print(f"Customer2({customer2._name}, {customer2._phone}, {customer2._email})")
    customer3 = Customer("Afaq", "07863016121","afaq@gmail.com")
    print(f"Customer3({customer3._name}, {customer3._phone}, {customer3._email})")
    
    # Creating stock instances with book name, author, and price
    stock1 = Stock("To Kill a Mockingbird", "Harper Lee", 10.99)
    print(f"Stock1({stock1._book_name}, {stock1._author}, £{stock1._price})")
    stock2 = Stock("1984", "George Orwell", 8.49)
    print(f"Stock2({stock2._book_name}, {stock2._author}, £{stock2._price})")
    stock3 = Stock("The Great Gatsby", "F. Scott Fitzgerald", 7.99)
    print(f"Stock3({stock3._book_name}, {stock3._author}, £{stock3._price})")
    
    # Creating order instances with customer and stock
    order1 = Order(customer1, stock1)
    print(f"Order({order1._customer._name}, £{order1._stock._price})")
    order2 = Order(customer2, stock2)
    print(f"Order({order2._customer._name}, £{order2._stock._price})")
    order3 = Order(customer3, stock3)
    print(f"Order({order3._customer._name}, £{order3._stock._price})")
    
    # Creating shipping instances with order and today's date
    shipping1 = Shipping(order1, datetime.datetime.today())
    shipping2 = Shipping(order2, datetime.datetime.today())
    shipping3 = Shipping(order3, datetime.datetime.today())
    
    # Calculating shipping cost
    shipping1.calc_ship_cost(True)
    shipping2.calc_ship_cost(False)
    shipping3.calc_ship_cost(True)
    
    # Creating invoice instances with invoice number, stock, and shipping
    invoice1 = Invoice("INV0001", stock1, shipping1)
    print(f"Invoices({invoice1._invoice_nbr}, {invoice1._stock._book_name}, £{invoice1.invoice()}, {invoice1._ship_order._ship_date})")
    invoice2 = Invoice("INV0002", stock2, shipping2)
    print(f"Invoices({invoice2._invoice_nbr}, {invoice2._stock._book_name}, £{invoice2.invoice()}, {invoice2._ship_order._ship_date})")
    invoice3 = Invoice("INV0003", stock3, shipping3)
    print(f"Invoices({invoice3._invoice_nbr}, {invoice3._stock._book_name}, £{invoice3.invoice()}, {invoice3._ship_order._ship_date})")
    
    # Creating a bookstore instance and adding invoices
    bookstore = BookStore()
    bookstore._invoices.append(invoice1)
    bookstore._invoices.append(invoice2)
    bookstore._invoices.append(invoice3)
    
    # Printing number of urgent shipments and invoice total costs
    print(f"Number of urgent shipments: {shipping1.count_urgent}")
    print(f"Invoice 1 total cost: £{invoice1.invoice(): .2f}")
    print(f"Invoice 2 total cost: £{invoice2.invoice(): .2f}")
    print(f"Invoice 3 total cost: £{invoice3.invoice(): .2f}")
    
    # Searching for an invoice by invoice number
    bookstore.search_invoice("INV0004")
    
if __name__ == "__main__":
    Test.main()