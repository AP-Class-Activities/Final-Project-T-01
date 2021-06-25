'''
This is a class defining a take in a store.

Usage:
   1) Create a new take:
        tk= Take(customer, seller, good, time, share)

   2) Print the course information:    
        print(tk)
'''
from Customer import Customer
from seller import Seller
from good import Good

class take:
    def __init__(self,Customer, Seller, Good, time,share):
        self.__customer = Customer
        self.__seller = Seller
        self.__good = Good
        self.__time = time
        self.__share = share

    #setters and getters
    @property
    def Customer(self):
        return self.__customer
     
    @Customer.setter
    def id(self,value):
        self.__customer = value
   #----------------------------------------
     
    @property
    def seller(self):
        return self.__seller
     
    @seller.setter
    def seller(self,value): 
        self.__seller = value
   #----------------------------------------
     
    @property
    def Good(self):
        return self.__good
     
    @Good.setter
    def id(self,value):
        self.__good = value

   #----------------------------------------

    @property
    def time(self):
        return self.__time
     
    @time.setter
    def time(self,value): 
        self.__time = value
   #----------------------------------------

    @property
    def share(self):
        return self.__share
     
    @share.setter
    def share(self,value): 
        self.__share = value

   #----------------------------------------

    def __str__(self): 
        return 'CUSTOMER --> {}\t\tSELLER--> {}\t\tGOOD --> {}\t\t time: {}\tshare: {}'\
            .format(self.Customer.ID,self.Seller.ID, self.Good.ID, self.time, self.share)