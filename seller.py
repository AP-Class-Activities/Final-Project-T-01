class Seller:
    scores = [0]
    def __init__(self,name,Id,position,store_position,register_date,good=[]):
        self.__name=name
        self.__Id=Id
        self.__position = position
        self.__store=Store()
        self.__store.position = store_position
        self.__register_date = register_date
        self.__good_file = r'data\{}_good.dat'.format(self.__id)

 #helper methods to save/read data in/from files
    def __save_good(self): 
        with open(self.__good_file, 'wb') as file:
            pickle.dump(self.good, file)
    def __read_good(self): 
        with open(self.__good_file, 'rb') as file:
            self.__good = pickle.load(file)

    def set_score(self,score):
        self.scores.append(score)
    
 #add or remove elements
    def __add__(self, element): 
        if type(element) is Good: 
            if element not in self.__good:
                self.__good.append(element)
        else: 
             raise ValueError('the element you want to add should be of types [good]')
        return self
    def __sub__(self, element): 
        if type(element) is good: 
            if element  in self.__good:
                self.__good.remove(element)
        else: 
                 raise ValueError('the element you want to add should be of types [good]')
        return self

    def get_score(self):
        m = np.mean(np.array(self.scores))
        attrs = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond')
        diff = now - self.register_date 
        s = diff[0]*365*24 +diff[1]*30*24+diff[2]*24+diff[3]+diff[4]/60+diff[5]/3600
        f = np.sqrt(np.sum((np.array(self.position) - np.array(self.store.position))**2))
        return (m*50 + s*10 +f*20) /80 