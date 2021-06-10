'''
This class is to give meaning to the buyer
'''

from person import Person

class buyer(Person):
    def __init__(self, id, name, family, address, phone, password, sex, year,number_of_purchases):
        super(buyer,self).__init__(id, name, family, address, phone, password, sex, year)

        self __.number_of_purchases=number_of_purchases
        if number_of_purchases<0 :
            raise ValueError(The number_of_purchases must be more than zero)    
            self.__ number_of_purchases = number_of_purchases

    @property
    def number_of_purchases(self): 
        return self.__ number_of_purchases
    @number_of_purchases.setter(self)
    def number_of_purchases(self,number_of_purchases):
        if number_of_purchases<0 :
            raise ValueError(The number_of_purchases must be more than zero)
            self.__ number_of_purchases = number_of_purchases    

