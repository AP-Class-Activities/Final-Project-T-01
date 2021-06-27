class shop:
    def __init__(self,customer=[],seller=[],operator=[]):

        self.__customer_file = r'data\{}_customer.dat'.format(self.__id)
        self.__seller_file = r'data\{}_seller.dat'.format(self.__id)
        self.__operator_file = r'data\{}_operator.dat'.format(self.__id)

#helper methods to save/read data in/from files
    def __save_customer(self): 
        with open(self.__customer_file, 'wb') as file:
            pickle.dump(self.customer, file)

    def __read_customer(self): 
        with open(self.__customert_file, 'rb') as file:
            self.__customer = pickle.load(file)

    def __save_seller(self): 
        with open(self.__seller, 'wb') as file:
            pickle.dump(self.seller, file)

    def __read_seller(self): 
        with open(self.__seller_file, 'rb') as file:
            self.__seller = pickle.load(file)

    def __save_operator(self): 
        with open(self.__operator_file, 'wb') as file:
            pickle.dump(self.operator, file)
    
    def __read_operator(self): 
        with open(self.__operator_file, 'rb') as file:
            self.__operator = pickle.load(file)
  #add or remove elements 
    def __add__(self, element): 
        if type(element) is customer: 
            if element not in self.__customer:
                self.__customer.append(element)
        
        elif type(element) is seller: 
            if element not in self.__seller:
                self.__seller.append(element)
        
        elif type(element) is operator: 
            if element not in self.__operator:
                self.__operator.append(element)
        else: 
            raise ValueError('the element you want to add should be of types [seller,customer, operator]')
        
        return self

    def __sub__(self, element): 
        if type(element) is seller: 
            if element  in self.__seller:
                self.__seller.remove(element)
        
        elif type(element) is customer: 
            if element  in self.__customer:
                self.__customer.remove(element)
        
        elif type(element) is operator: 
            if element  in self.__operator:
                self.__operator.remove(element)
        
        else: 
            raise ValueError('the element you want to add should be of types [seller,customer, operator]')
        
        return self
