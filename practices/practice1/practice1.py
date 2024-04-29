
from practices.data.dataXY import DataXY

dataXY = DataXY()

class Practice1:

    def __init__(self):
        self.x = 0
        self.y = 0

    def setDataXY(self, data:list=[], cant:int=0):
        dataXY.setDataXY(data, cant)

    def getDataXY(self):
        return dataXY.getDataXY()

    def insertDataXY(self, x:int, y:int)->None:
        dataXY.insertDataXY(x, y)

    def updateDataXYByInd(self, ind:int, x:int, y:int)->None:
        dataXY.updateDataXYByInd(ind, x, y)

    def updateXByInd(self, ind:int, x:int)->None:
        dataXY.updateXByInd(ind, x)

    def updateYByInd(self, ind:int, y:int)->None:
        dataXY.updateXByInd(ind, y)

    def getDataXYByInd(self, ind)->int:
        return dataXY.getDataXYByInd(ind)
    
    def getXByInd(self, ind)->int:
        return dataXY.getXByInd(ind)

    def getYByInd(self, ind)->int:
        return dataXY.getYByInd(ind)

    def setX(self, x)->int:
        self.x = dataXY.setX(x)

    def getX(self)->int:
        return dataXY.getX()
    
    def setY(self, y)->int:
        self.y = dataXY.setY(y)

    def getY(self)->int:
        return dataXY.getY()
    
    def deleteYXByInd(self, ind:int)->object:
        try:
            res = self.getDataXYByInd(ind)
            dataXY.deleteYXByInd(ind)
            return res
        except:
            return {}
