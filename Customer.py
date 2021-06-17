class Customer:
    def __init__(self,id,name,family,username,password,valet=None):
        self.__id = id
        self.__name = name
        self.__family = family
        self.__username = username
        self.__password = password

        self.__valet = valet
        #self.__buying_list = Buying_list()
        #self.__favorit_list = Favorit_list()
    
    #setters and getters
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
    def family(self):
        return self.__family
     
    @family.setter
    def family(self,value): 
        self.__family = value
   #----------------------------------------
    
    @property
    def username(self):
        return self.__username
     
    @username.setter
    def username(self,value): 
        self.__username = value
   #----------------------------------------
    
    @property
    def password(self):
        return self.__password
     
    @password.setter
    def password(self,value): 
        self.__password = value
   #----------------------------------------
    
    @property
    def valet(self):
        return self.__valet
     
    @valet.setter
    def valet(self,value): 
        self.__valet = value
        
   #----------------------------------------
        