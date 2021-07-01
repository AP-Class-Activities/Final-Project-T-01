from datetime import datetime
import numpy as np
from operator import attrgetter
from utils import *
from source.Good import Good


class Seller:
    scores = [0]
    def __init__(self,name,username,password,position,store_position,register_date):
        self.__name=name
        self.__position = position
        self.__username = username
        self.__password = password
        self.__storeposition = store_position
        self.__register_date = register_date
        self.confirmed = False
        self.__valet = 0

    def add_good(self,name,price,img,quant):
        good = Good(name,price,img,self,quant)
        goods = load_pkl("./databases/goods.pkl")
        goods.append(good)
        save_pkl("./databases/goods.pkl",goods)

    def add_to_valet(self,money):
        self.__valet += money
    def widraw(self,money):
        self.__valet -= money
    def get_valet(self):
        return self.valet
    def getpassword(self):
        return self.__password

    def setpassword(self,password):
        self.__password = password

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name
    def getconfirmed(self):
        return self.__confirmed

    def setconfirmed(self,bool):
        self.__confirmed = bool

    def getname(self):
        return self.__name

    def setlast_name (self,last_name):
        self.__last_name = last_name
    def getusername(self):
        return self.__username

    def setusername(self,username):
        self.__username = username

    def getpassword(self):
        return self.__password

    def setname(self,password):
        self.__password = password

    def getposition (self):
        return self.__position

    def setstore(self,position ):
        self.__position = position


    def getregister_date (self):
        return self.__register_date

    def setstore(self,register_date ):
        self.__register_date = register_date


    def get_score(self):
        m = np.mean(np.array(self.scores))
        attrs = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond')
        now = np.array(attrgetter(*attrs)(datetime.now()))
        diff = now - np.array(attrgetter(*attrs)(self.__register_date))
        print(diff)
        s = diff[0]*365*24 +diff[1]*30*24+diff[2]*24+diff[3]+diff[4]/60+diff[5]/3600
        f = np.sqrt(np.sum((np.array(self.__position) - np.array(self.__storeposition))**2))
        return (m*50 + s*10 +f*20) /80

    def signup(self):
        sellers = load_pkl("./databases/sellers.pkl")
        sellers.append(self)
        save_pkl("./databases/sellers.pkl",sellers)
