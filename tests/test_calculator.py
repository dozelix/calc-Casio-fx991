import pytest
from calculator import Calculator


def test_push_pop_get_stack():
    c = Calculator()
    c.push(3.5)
    assert c.get_stack() == [3.5]
    assert c.pop() == 3.5
    assert c.get_stack() == []


def test_binary_add():
    c = Calculator()
    c.push(3)
    c.push(4)
    res = c.binary('+')
    assert res == 7
    # binary consume operands and no re-push
    assert c.get_stack() == []


def test_binary_insufficient_operands():
    c = Calculator()
    c.push(1)
    with pytest.raises(IndexError):
        c.binary('+')


def test_binary_division_by_zero_restores_stack():
    c = Calculator()
    c.push(3)
    c.push(0)
    with pytest.raises(ZeroDivisionError):
        c.binary('/')
    # operandos deben restaurarse después del error
    assert c.get_stack() == [3.0, 0.0]


def test_nary_sum_and_stack():
    c = Calculator()
    c.push(1)
    c.push(2)
    c.push(3)
    res = c.nary('suma_todos')
    assert res == 6
    assert c.get_stack() == [6.0]


def test_nary_product():
    c = Calculator()
    c.push(2)
    c.push(3)
    c.push(4)
    res = c.nary('multiplicacion_todos')
    assert res == 24
    assert c.get_stack() == [24.0]


def test_nary_subtract_order():
    c = Calculator()
    c.push(10)
    c.push(2)
    c.push(1)
    res = c.nary('resta_todos')
    assert res == 7  # 10 - 2 - 1
    assert c.get_stack() == [7.0]


def test_nary_division_by_zero_does_not_modify_stack():
    c = Calculator()
    c.push(4)
    c.push(0)
    with pytest.raises(ZeroDivisionError):
        c.nary('division_todos')
    # pila no modificada
    assert c.get_stack() == [4.0, 0.0]


def test_clear_and_get_stack_copy():
    c = Calculator()
    c.push(1)
    s = c.get_stack()
    s.append(999)
    # get_stack debe devolver copia
    assert c.get_stack() == [1.0]
    c.clear()
    assert c.get_stack() == []
