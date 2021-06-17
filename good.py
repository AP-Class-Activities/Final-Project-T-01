class Good:
   scores = []  
   def __init__(self,seller,id,name,price,number,deposit_date):
      self.__seller = seller
      self.__id=id
      self.__name=name
      self.__price=price
      self.__number=number
        
      self.__deposit_date = deposit_date
   #----------------------------------------
   #setters & getters
   @property
   def seller(self):
      return self.__seller
#----------------------------------------
   @property
   def id(self):
      return self.__id

   @id.setter
   def id(self,value):
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
   def price(self):
      return self.__price

   @price.setter
   def price(self,value):
      self.__price = value    
#----------------------------------------
   @property
   def number(self):
      return self.__number

   @number.setter
   def number(self,value):
      self.__number = value    
#----------------------------------------
   @property
   def deposit_date(self):
      return self.__deposit_date

   @deposit_date.setter
   def deposit_date(self,value):
      self.__deposit_date = value       
#----------------------------------------


      