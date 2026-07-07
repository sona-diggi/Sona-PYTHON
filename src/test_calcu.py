from calc import *

def test1():
    assert add(2,3)==5 ,"correct"
    assert add(1,1)==2
    assert add(-1,2)==1

def test2():
    assert sub(2,1)==1
    assert sub(5,1)==4