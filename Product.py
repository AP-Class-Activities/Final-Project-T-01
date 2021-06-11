'''
This class is to give meaning to the product
'''


class product:
    def __init__(self,id,name,Price,number,Score=None):
        self.__id = id
        self.__name = name
        self.__score=Score
        
        if Price<0 :
            raise ValueError('The price must be more than zero')
        self.__price=Price
        if number<0 :
            raise ValueError('The Number must be more than zero')
        self.__number =number
        
    #setters & getters
    @property
    def id(self): 
        return self.__id

    @id.setter
    def id(self,value):
        self.__id=value

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value):
        self.__name=value

    @property
    def price(self): 
        return self.__price

    @price.setter
    def price(self,value):
        if value<0 :
            raise ValueError('The price must be more than zero')
        self.__price=value

    @property
    def number(self): 
        return self.__number
    
    @number.setter
    def number(self,value):
        if value<0 :
            raise ValueError('The Number must be more than zero')
        self.__number=value

    @property
    def Score(self): 
        return self.__score

    @Score.setter
    def Score(self,value):
        self.__score= value



    


