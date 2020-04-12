# -*- coding: utf-8 -*- 

"""
@Time   : 2020/4/12 19:55
@File   : test_single.py
@Author : 15769162764@163.com

"""
from useful_decoration.single import singleton


@singleton
class Person:
    """
    This is  Person
    """
    name = "Frank"


def test_person():
    p = Person()
    p2 = Person()
    p3 = Person()

    print(p, p2, p3)

    assert p == p2 == p3

    assert id(p) == id(p2) == id(p3)


if __name__ == '__main__':
    test_person()
