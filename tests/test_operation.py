from src.math_operations import add,sub

def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,3)==2
    assert sub(4,3)==1
    assert sub(3,3)==0
    assert sub(2,3)==-1
    
def test_mul():
    assert mul(2,3)==6
    assert mul(-1,1)==-1
    assert mul(0,5)==0  
    
def test_div():
    assert div(6,3)==2
    assert div(5,2)==2.5
    try:
        div(5,0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"    
        
def test_mod():
    assert mod(5,3)==2
    assert mod(5,5)==0
    try:
        mod(5,0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"                    