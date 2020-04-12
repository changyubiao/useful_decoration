# -*- coding: utf-8 -*- 
"""
@User     : Frank
@File     : test_funcallable.py
@DateTime : 2019-09-26 21:45 
@Email    : 15769162764@163.com

pytest  -v -s  tests/test_funcallable.py

"""

from useful_decoration.func_callable import checked_arguments

from useful_decoration.func_callable import default_value

import pytest


def check_a(data):
    a = data.get('a')

    if a >= 10:
        return True
    return False


@checked_arguments(callback=check_a, default=default_value)
def calculate(a):
    """
    用户函数
    :return:
    """
    return {"ret": 20}






"""
对于这种 的例子 
"""






def test_calculate():
    assert 20 == calculate(a=10).get('ret')


def test_calculate_02():
    assert 0 == calculate(a=1).get('ret')


if __name__ == '__main__':
    pytest.main(["-s", "test_funcallable.py"])
    pass
