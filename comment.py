class  Comment:    
    def __init__(self,good,customer,text):
        #self.__Id = ID
        self.__good = good
        self.__text = text
        self.__customer = customer 

    #getter
    @property    
    def get_good(self):
        return self.__good

    @property
    def get_customer(self):
        return self.__customer

    @property
    def get_text(self):
        return self.__text