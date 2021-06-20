'''
This is a class defining a take in a store.

Usage:
   1) Create a new take:
        tk= Take(customer, seller, good, time, share)

   2) Print the course information:    
        print(tk)
'''
from Customer import Customer as cu
from seller import Seller as se
from good import Good as go

class take:
    def __init__(self,customer, seller, good, time ,share ):
        self.__customer = customer
        self.__seller = seller
        self.__good = good
        self.__time = time
        self.__share = share

    #setters and getters
    @property
    def customer(self):
        return self.__customer
     
    @customer.setter
    def ID(self,value): 
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
    def good(self):
        return self.__good
     
    @good.setter
    def ID(self,value): 
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
            .format(self.customer.ID,self.seller.ID, self.good.ID, self.time, self.share)