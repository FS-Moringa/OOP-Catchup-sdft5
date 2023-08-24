#  Product 

# attributes -> name, price, quantity, description
# methods -> addQuantity, buy, calcuatetax
# from functools import singledispatch, dispatch


#Access Modifiers -> determine the scope of an attribute
# public, 
# private __
# protected _
from abc import ABC, abstractclassmethod


class ProductBase(ABC):

    @abstractclassmethod
    def calculate_tax():
        pass

    
    @abstractclassmethod
    def add_quantity():
        pass

class Product(ProductBase):

    def __init__(self,name, price, quantity):
        self.name = name
        self.__price = price
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"<Product: {self.name}>"
    
    def buy(self, qty):
        self.quantity-=qty
        return qty
    
    def calculate_tax(self):
        return f"32% VAT"
     
    def add_quantity(self):
        pass

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self,value):
        self.__price = value

    # def get_price(self):
    #     return self.__price
    
    # def set_price(self, value):
    #     self.__price = value


p1 = Product("Milk", 65, 12)
p2 = Product("Bread", 60, 56)
p3 = Product("Salt", 10, 30)

# name mangling
# getter and setter methods
# print(p1.price)
print(p1.calculate_tax())
p1.price = 50
# print(p1.weight)
# print(p1.price)

# instance methods, classmethod, helper methods 
# print(p2.name)
# print(p3.name)
# print(p1.set_price(50))
# print(p1.get_price())
from datetime import timedelta, datetime
from multipledispatch import dispatch

class Bread(Product):
    kebs_approved = False

    def __init__(self, name, price, quantity, weight):
        super().__init__(name, price, quantity)
        self.weight= weight
        self.expiry_date = datetime.now() + timedelta(days=5) 
    
    def check_expiry(self):
        return  self.expiry_date 
    
    def vat():
        return 16
    
    @classmethod
    def number_of_slices(cls):
        return 20
    
    @dispatch(int)
    def buy(self,qty):
        self.quantity-=qty
        return f' You have bought {qty} loaf(s) of bread'
    
    @dispatch(int, str)
    def buy(self, qty, cust_name):
        self.quantity-=qty
        return f' {cust_name} you have bought {qty} loaf(s) of bread'

b1 = Bread("Supaloaf",65,30,'400g')
b2 = Bread("Festive",60,30,'400g')
b3 = Bread("United",55,30,'400g')

print(b1.price)
print(b1.weight)
print(b1.check_expiry())
print(b1.buy(1,"Steve"))
print(b1.quantity)
# print(p2.name)
print(b1.quantity)
print(Bread.number_of_slices())
print(b2.number_of_slices())
print(b3.kebs_approved)
print(Bread.kebs_approved)

# print(p3.quantity)
# print(p3.buy(5))
# print(p3.quantity)


        


