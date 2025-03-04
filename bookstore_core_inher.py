# Name = Muhammad Imran



# importing datetime module
import datetime
"""
The class Person serve as a base clase for Customer.
is for adding information of customer such as name, phone number and email address
Each attribute has a getter and setter method
"""
class Person:
  # this constructor intitalize details of customer having name, phone, email attributes
  def __init__(self, name: str, phone: str, email: str):
    self._name = name
    self._phone = phone
    self._email = email

  """
  getter for customer's name which access the attribute name 
  returns customer's name
  """    
  @property
  def get_name(self):
    return self._name
  
  """
  setter for the customer's name
  updates or changes the customer name where needed or valid
  """
  @get_name.setter
  def set_name(self, name):
    self._name = name
    
  """
  getter for customer's phone which access the attribute phone
  returns customer's phone
  """    
  @property
  def get_phone(self):
    return self._phone
  
  """
  setter for the customer's phone
  updates or changes the customer phone where needed or valid
  """
  @get_phone.setter
  def set_phone(self, phone):
    self._phone = phone
  
  """
  getter for customer's email which access the attribute email
  returns customer's email
  """    
  @property
  def get_email(self):
    return self._email
  
  """
  setter for the customer's email
  updates or changes the customer email where needed or valid
  """
  @get_email.setter
  def set_email(self, email):
    self._email = email
    
""" 
The class Customer is inherited from Person class
"""
class Customer(Person):
# Constructor to initialize a Customer object by reusing the Person constructor via super().
  def __init__(self, name, phone, email):
    super().__init__(name, phone, email)

"""
The class Product serve as a base clase for Stock.
is for adding information of stock such as bookname and price
Each attribute has a getter and setter method
"""   
class Product:
# Constructor to initialize a Product object with name and price attributes.
  def __init__(self, name: str, price: float):
    self.Name = name
    self.Price = price
    
  """
  getter for book name which access the attribute name
  returns bookname
  """    
  @property
  def get_Name(self):
    return self.Name
  
  """
  setter for the book name
  updates or changes the book name where needed or valid
  """
  @get_Name.setter
  def set_Name(self, name):
    self.Name = name
    
  """
  getter for price which access the attribute price
  returns price
  """    
  @property
  def get_Price(self):
    return self.Price
  
  """
  setter for the price
  updates or changes the book name where needed or valid
  """
  @get_Price.setter
  def set_Price(self, price):
    self.Price = price
    
    
"""
The class Stock is inherited from Product class
"""  
class Stock(Product):
# Constructor to initialize a Stock object by reusing the Product constructor via super().
# Also has a private attribute for author
  def __init__(self, name,author: str, price):
    super().__init__(name, price)   
    self._author = author
    
  """
  getter for author which access the attribute author
  returns author
  """    
  @property
  def get_author(self):
    return self._author
  
  """
  setter for the author
  updates or changes the author where needed or valid
  """
  @get_author.setter
  def set_author(self, author):
    self._author = author 
 
 
    
"""  
Here I copied the class Order, Shipping, Invoice, BookStore from bookstore_core.py
and used for importing these in part 3 which is bookstore_gui.py

"""
    
    
    
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
      self.total_cost = self._stock.Price + self._ship_order._ship_cost
    return self.total_cost
  

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
