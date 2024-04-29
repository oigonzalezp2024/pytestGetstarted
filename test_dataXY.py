

from practices.data.dataXY import DataXY

dataXY = DataXY()

def test_setDataXY_01():
    data=[{"x":1, "y":1}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == data

def test_setDataXY_02():
    data=[{"x":1, "y":2},{"x":2, "y":3}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == data

def test_setDataXY_03():
    data=[{"x":1, "y":2}]
    cant=0
    dataXY.setDataXY(data, cant)
    assert dataXY.getDataXY() == data

def test_setDataXY_04():
    data=[{"x":33, "y":44}]
    cant=1
    dataXY.setDataXY(data, cant)
    assert dataXY.getDataXY() == [{"x":33, "y":44},{"x":0, "y":0}]

def test_setDataXY_05():
    data=[{"x":1, "y":2}]
    cant=-10
    dataXY.setDataXY(data, cant)
    assert dataXY.getDataXY() == data

def test_setDataXY_06():
    data=[{"x":1, "y":2}, 1]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_07():
    data=[{"x":1, "y":2}, "1"]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_08():
    data=[{"x":1, "y":2}, {}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_09():
    data=[{"x":1, "y":2}, []]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_10():
    data=[1, {"x":1, "y":2}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_11():
    data=["1", {"x":1, "y":2}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_12():
    data=[{}, {"x":1, "y":2}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_13():
    data=[[], {"x":1, "y":2}]
    dataXY.setDataXY(data)
    assert dataXY.getDataXY() == []

def test_setDataXY_14():
    cant=-1
    dataXY.setDataXY(cant=cant)
    assert dataXY.getDataXY() == []

def test_setDataXY_15():
    cant=0
    dataXY.setDataXY(cant=cant)
    assert dataXY.getDataXY() == []

def test_setDataXY_16():
    cant=1
    dataXY.setDataXY(cant=cant)
    assert dataXY.getDataXY() == [{"x":0, "y":0}]

def test_getDataXYByInd():
    dataXY.setDataXY(cant=100)
    assert dataXY.getDataXYByInd(3) == {"x":3, "y":3}

def test_setGetX():
    dataXY.setX(2)
    assert dataXY.getX() == 2

def test_setGetY():
    dataXY.setY(3)
    assert dataXY.getY() == 3

def test_getXByInd():
    dataXY.setDataXY(cant=100)
    assert dataXY.getXByInd(33) == 33

def test_getYByInd():
    dataXY.setDataXY(cant=100)
    assert dataXY.getYByInd(22) == 22

def test_insertDataXY():
    x, y = 11, 22
    assert dataXY.insertDataXY(x, y) == {"x":11, "y":22}

def test_updateDataXYByInd():
    ind, x, y = 33, 44, 55
    dataXY.setDataXY(cant=100)
    assert dataXY.updateDataXYByInd(ind, x, y) == {"x":44, "y":55}

def test_updateXByInd():
    ind, x, y, xn = 33, 44, 55, 66
    dataXY.updateDataXYByInd(ind, x, y)
    assert dataXY.updateXByInd(ind, xn) == {"x":66, "y":55}

def test_updateYByInd():
    ind, x, y, yn = 33, 77, 88, 99
    dataXY.updateDataXYByInd(ind, x, y)
    assert dataXY.updateYByInd(ind, yn) == {"x":77, "y":99}

def test_deleteYXByInd():
    dataXY.setDataXY(cant=100)
    assert dataXY.deleteYXByInd(99) == {"x":99, "y":99}
