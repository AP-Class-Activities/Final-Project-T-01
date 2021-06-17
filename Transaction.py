from Customer import Customer
from good import Good
from seller import Seller


class Transaction:
    def __init__(self,id,customer= [],good = [],seller = []):
        self.__id = id
        self.__customer = customer
        self.__good = good
        self.__seller = seller

    #setters and getters

    @property
    def id(self):
        return self.__id
     
    @id.setter
    def id(self,value): 
        self.__id = value

    @property
    def customer(self):
        return self.__customer
     
    @property
    def good(self):
        return self.__good

    @property
    def seller(self):
        return self.__seller