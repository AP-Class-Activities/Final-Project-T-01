class  Comment:    
    def __init__(self,good,customer,text,Id):
        self.__good = good
        self.__text = text
        self.__customer = customer 
        self.__Id = Id
    def get_good(self):
         return self.__good
    def get_customer(self):
        return self.__customer
    def get_text(self):\
        return self.__text