
from practices.practice1.practice1 import Practice1

practice2 = Practice1()

def test_setDataXY():
    practice2.setDataXY()
    assert practice2.getDataXY() == []
    practice2.setDataXY(cant=10)
    assert len(practice2.getDataXY()) == 10

def test_getDataXY():
    practice2.setDataXY(cant=10)
    assert len(practice2.getDataXY()) == 10

def test_insertDataXY():
    practice2.insertDataXY(1,2)
    assert len(practice2.getDataXY()) == 11

def test_updateDataXYByInd(ind=3, x=2, y=3)->None:
    practice2.updateDataXYByInd(ind, x, y)
    res = practice2.getDataXYByInd(ind)
    assert res == {"x":2,"y":3}

def test_getXByInd(ind=3)->int:
    res = practice2.getXByInd(ind)
    assert res == 2

def test_getYByInd(ind=3)->int:
    res = practice2.getYByInd(ind)
    assert res == 3

def test_setX(x=111)->int:
    practice2.setX(x)
    res = practice2.getX()
    assert res == 111

def test_setY(y=222)->int:
    practice2.setY(y)
    res = practice2.getY()
    assert res == 222

def test_deleteYXByInd(ind=0)->None:
    res = practice2.deleteYXByInd(ind)
    assert res == {'x': 0, 'y': 0}