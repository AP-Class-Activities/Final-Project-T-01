class Good:
     scores = []
     def __init__(self,id,name,price,number,deposit_date,seller):
        self.seller = seller
        self.__id=id
        self.__name=name
        self.__price=price
        self.__number=number
        
        self.deposit_date = deposit_date
      
      #setters & getters
      @property
      def id(self):
         return self.__id

      @id.setter
      def id(self,value):
         self.__id = value 


      