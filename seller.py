class Seller:
    scores = [0]
    def __init__(self,name,Id,position,store_position,register_date):
        self.__name=name
        self.__Id=Id
        self.position = position
        self.store=Store()
        self.store.position = store_position
        self.register_date = register_date
    def set_score(self,score):
        self.scores.append(score)

    def get_score(self):
        m = np.mean(np.array(self.scores))
        attrs = ('year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond')
        diff = now - self.register_date 
        s = diff[0]*365*24 +diff[1]*30*24+diff[2]*24+diff[3]+diff[4]/60+diff[5]/3600
        f = np.sqrt(np.sum((np.array(self.position) - np.array(self.store.position))**2))
        return (m*50 + s*10 +f*20) /80 