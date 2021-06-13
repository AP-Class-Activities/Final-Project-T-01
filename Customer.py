class Customer:
    def __init__(self,name,last_name,username,password):
        self.__valet = Valet()
        self.__buying_list = Buying_list()
        self.__favorit_list = Favorit_list()
        self.__name = name
        self.__last_name = last_name
        self.__username = username
        self.__password = password