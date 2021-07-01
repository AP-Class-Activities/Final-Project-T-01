from utils import *
class Comment:
    def __init__(self,customer,good,text):
        self.__customer = customer
        self.__good = good
        self.__text = text

    def get_customer(self):
        return self.__customer
    def set_customer(self,customer):
        self.__customer = customer

    def get_good(self):
        return self.__good
    def set_good(self,good):
        self.__good = good

    def get_text(self):
        return self.__text

    def set_text(self,text):
        self.__text = text