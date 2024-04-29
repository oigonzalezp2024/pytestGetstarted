
class DataXY:

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__data = []

    def setDataXY(self, data:list=[], cant:int=0):
        self.__data = []
        val = True
        if (len(data)>0):
            for i in data:
                if(type(i) == type({})):
                    keys = []
                    for ii in i.keys():
                        keys.append(ii)
                    if(len(keys)!=2):
                        val = False
                        break
                else:
                    val = False
                    break
            if(val):
                self.__data = data
        i=0
        while(i<cant):
            self.__data.append({"x":i,"y":i})
            i+=int(1)

    def getDataXY(self):
        return self.__data

    def insertDataXY(self, x:int, y:int)->object:
        self.setX(x)
        self.setY(y)
        reg = {
                'x':self.getX(),
                'y':self.getY()
            }
        self.__data.append(reg)
        return reg

    def updateDataXYByInd(self, ind:int, x:int, y:int)->None:
        self.updateXByInd(ind, x)
        self.updateYByInd(ind, y)
        return self.__data[ind]

    def updateXByInd(self, ind:int, x:int)->object:
        self.__data[ind]['x'] = x
        return self.__data[ind]

    def updateYByInd(self, ind:int, y:int)->object:
        self.__data[ind]['y'] = y
        return self.__data[ind]

    def getDataXYByInd(self, ind)->int:
        return self.__data[ind]
    
    def getXByInd(self, ind)->int:
        return self.__data[ind]['x']

    def getYByInd(self, ind)->int:
        return self.__data[ind]['y']

    def setX(self, x)->int:
        self.__x = x

    def getX(self)->int:
        return self.__x
    
    def setY(self, y)->int:
        self.__y = y

    def getY(self)->int:
        return self.__y
    
    def deleteYXByInd(self, ind:int)->object:
        try:
            res = self.__data[ind]
            del self.__data[ind]
            return res
        except:
            return {}

