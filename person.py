'''
This is the class that defines the common
characteristics of seller and buyer

authors: 
Amirhossein Noruzi
matin mirzaei

Usage:
    1)Create a new person:
        p= Person(ID, person_name, person_family , address, phone_nuumber, password, sex, interance_year, valet)

   2) Print the Person information:    
        print(p)
'''

class Person:
    def __init__(self,id,name,family,address,phone,password,sex,year,valet=None):
        self.__id = id
        self.__name = name
        self.__family = family
        self.__address = address
        self.__phone = phone
        self.__password = password
        
        if sex not in ['male','female']:
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = sex
        
        if year > 1400 or year < 1395: 
            raise ValueError('the year for a student should be in rnage 1395 ... 1400')
        self.__year = year

        if valet<1000:
            raise ValueError('money transfer should be more than 1000')
        self.__valet = valet

    #setters & getters
    @property
    def ID(self): 
        return self.__id
    
    @ID.setter
    def ID(self,value): 
        self.__id = value

    @property
    def name(self): 
        return self.__name

    @name.setter
    def name(self,value): 
        self.__name = value

    @property
    def family(self): 
        return self.__family

    @family.setter
    def family(self,value): 
        self.__family = value

    @property
    def address(self): 
        return self.__address
    
    @address.setter
    def address(self,value): 
        self.__address = value

    @property
    def phone(self): 
        return self.__phone

    @phone.setter
    def phone(self,value): 
        self.__phone = value
    
    @property
    def valet(self): 
        return self.__valet

    @valet.setter
    def valet(self,value): 
        if value<1000:
            raise ValueError('money transfer should be more than 1000')
        self.__valet = value

    @property
    def sex(self): 
        return self.__sex

    @sex.setter
    def sex(self,value): 
        if value not in ['male', 'female']: 
            raise ValueError('the value of sex should be [male or female] ')
        self.__sex = value
    

    @property
    def year(self): 
        return self.__year

    @year.setter
    def year(self,value): 
        if value > 1400 or value < 1395: 
            raise ValueError('the year for a student should be in range 1395 ... 1400')
        self.__year = value
    
    @property
    def password(self): 
        return self.__password

    @password.setter
    def password(self,value): 
        if len(value)<8: 
            raise ValueError('Password must be at least 8 characters long')
        self.__password = value

    def __str__(self): 
        return 'ID: {}   name: {} {}    andress: {}   phone: {}     sex: {}    year: {}     valet: {}'\
            .format(self.ID,self.name, self.family, self.address, self.phone, self.sex, self.year, self.valet)

'''
#example client code:  
p = Person(1, 'amir', 'noruzi', 'Mazandaran, tonekabon', '09365838438', 'final_project', 'male', 1400, 150000 )

print(p)
'''