'''
This class defines a store in The main store
As definition,
a store is a collection of customers, sellers and goods.
customers can take goods with a sellers.
Any store has a neme and store's oprator.
Usage:

1) Create a new store
'''
from Customer import Customer as cu
from seller import Seller as se
from good import Good as go
from take import take as ta
import pickle

class Store:
    #position= None
    def __init__(self,id,name,oprator,phone,customers=[],sellers=[],goods=[], takes=[]) :
        self.__id = id
        self.__name = name
        self.__oprator = oprator
        self.__phone = phone
        self.__customer_file = r'data\{}_customers__customers.dat'.format(self.__id)
        self.__seller_file = r'data\{}_sellers.dat'.format(self.__id)
        self.__good_file = r'data\{}_goods.dat'.format(self.__id)
        self.__take_file = r'data\{}_takes.dat'.format(self.__id)
        self.__customers = customers
        self.__sellers = sellers
        self.__goods = goods
        self.__takes = takes

        #setters and getters

    @property
    def ID(self):
        return self.__id
     
    @ID.setter
    def ID(self,value): 
        self.__id = value
   #----------------------------------------
    @property
    def name(self):
        return self.__name
     
    @name.setter
    def name(self,value): 
        self.__name = value
   #----------------------------------------

    @property
    def oprator(self):
        return self.__oprator
     
    @oprator.setter
    def oprator(self,value): 
        self.__oprator = value
   #----------------------------------------
    
    @property
    def phone(self): 
        return self.__phone

    @phone.setter
    def phone(self,value): 
        self.__phone = value
   #----------------------------------------

    @property
    def customers(self): 
        return self.__customers
   #----------------------------------------

    @property
    def sellers(self): 
        return self.__sellers
   #----------------------------------------
    
    @property
    def goods(self): 
        return self.__goods
   #----------------------------------------
    
    @property
    def takes(self): 
        return self.__takes
   #----------------------------------------

   #helper methods to save/read data in/from files
    def __save_customers(self): 
        with open(self.__customers_file, 'wb') as file:
            pickle.dump(self.customers, file)

    def __read_customers(self): 
        with open(self.__customers_file, 'rb') as file:
            self.__customers = pickle.load(file)
    
    def __save_sellers(self): 
        with open(self.__teacher_file, 'wb') as file:
            pickle.dump(self.sellers, file)

    def __read_sellers(self): 
        with open(self.__teacher_file, 'rb') as file:
            self.__sellers = pickle.load(file)
    
    def __save_goods(self): 
        with open(self.__course_file, 'wb') as file:
            pickle.dump(self.goods, file)

    def __read_goods(self): 
        with open(self.__course_file, 'rb') as file:
            self.__goods = pickle.load(file)

    def __save_takes(self): 
        with open(self.__take_file, 'wb') as file:
            pickle.dump(self.takes, file)

    def __read_takes(self): 
        with open(self.__take_file, 'rb') as file:
            self.__takes = pickle.load(file)
    
    def save_to_file(self): 
        self.__save_customers()
        self.__save_takes()
        self.__save_goods()
        self.__save_sellers()

    def read_from_file(self): 
        self.__read_customers()
        self.__read_goods()
        self.__read_takes()
        self.__read_sellers()


    #add or remove elements 
    def __add__(self, element): 
        if type(element) is cu: 
            if element not in self.__customers:
                self.__customers.append(element)
        
        elif type(element) is se: 
            if element not in self.__sellers:
                self.__sellers.append(element)
        
        elif type(element) is go: 
            if element not in self.__goods:
                self.__goods.append(element)
        
        elif type(element) is ta: 
            if element not in self.__takes:
                self.__takes.append(element)
        
        else: 
            raise ValueError('the element you want to add should be of types [Student, Teacher, Course, Take]')
        
        return self

    def __sub__(self, element): 
        if type(element) is cu: 
            if element  in self.__customers:
                self.__customers.remove(element)
        
        elif type(element) is se: 
            if element  in self.__sellers:
                self.__sellers.remove(element)
        
        elif type(element) is ta: 
            if element  in self.__takes:
                self.__takes.remove(element)
        
        else: 
            raise ValueError('the element you want to add should be of types [Student, Teacher, Course, Take]')
        
        return self


    def __str__(self): 
        S = '\n\n______________________________________________________________________________________________________\n\n'
        S += 'Store Name: {}    Oprator: {} {}     Phone Number: {}'.format(self.name, self.oprator.name, self.oprator.family, self.phone)
        S += '\n\n____________________________________________STUDENTS___________________________________________________\n\n'
        
        for i in self.customers: 
            S += '%s\n'%(i) 
        
        S += '\n\n____________________________________________TEACHERS___________________________________________________\n\n'        
        for i in self.sellers:
            S += '%s\n'%(i) 
        
        S += '\n\n____________________________________________COURCES___________________________________________________\n\n'        
        for i in self.goods:
            S += '%s\n'%(i) 

        S += '\n\n____________________________________________TAKES___________________________________________________\n\n'        
        for i in self.takes:
            S += '%s\n'%(i)

        S += '_______________________________________________________________________________________________________'
        return S