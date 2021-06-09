'''
This class is to give meaning to the product
'''


class product:
    def __init__(self,Price,Score=None,Number):

        self.__score=Score
        
        if Price<0 :
            raise ValueError(The price must be more than zero)
        self.__price=Price
        if Number<0 :
            raise ValueError(The Number must be more than zero)
            self.__number=Number
        
    #setters & getters
    @property
    def price(self): 
        return self.__price
    @price.setter(self)
    def price(self,price):
        if Price<0 :
            raise ValueError(The price must be more than zero)
    @property
    def Number(self): 
        return self.__price
    @number.setter(self)
    def Number(self,Number):
        if Number<0 :
            raise ValueError(The Number must be more than zero)
            self.__number=Number
    @property
    def Score(self): 
        return self.__score
    @Score.setter
    def Score(selfe,Score):
        self.__score= Score



    


