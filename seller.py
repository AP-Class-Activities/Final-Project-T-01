class Seller:
    scores = [0]
    def __init__(self,id,name,family,address,phone,year,usename,password,valet=None,score=None):
        self.__id=id
        self.__name=name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__year = year
        self.__username = usename
        self.__password = password

        self.__valet = valet
        self.__score = score
        #self.store=Store()
        #self.store.position = store_position
        #self.register_date = register_date

    #def set_score(self,score):
        #self.scores.append(score)

    #def get_score(self):
        #m = np.mean(np.array(self.scores))
        #attrs = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond')
        #diff = now - self.register_date 
        #s = diff[0]*365*24 +diff[1]*30*24+diff[2]*24+diff[3]+diff[4]/60+diff[5]/3600
        #f = np.sqrt(np.sum((np.array(self.position) - np.array(self.store.position))**2))
        #return (m*50 + s*10 +f*20) /80 

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
    def address(self):
        return self.__address
     
    @address.setter
    def address(self,value): 
        self.__address = value
   #----------------------------------------

    @property
    def phone(self):
        return self.__phone
     
    @phone.setter
    def phone(self,value): 
        self.__phone = value
   #----------------------------------------
    @property
    def year(self):
        return self.__year
     
    @year.setter
    def year(self,value): 
        self.__year = value
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
    @property
    def score(self):
        return self.__score
     
    @score.setter
    def score(self,value): 
        self.__score = value
   #----------------------------------------