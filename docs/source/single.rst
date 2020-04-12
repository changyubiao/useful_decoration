.. _single:


.. single模块实现了一个单例的装饰器



single 模块介绍
===============

该模块 提供了两个 装饰器 ,分别是 single,singleton

single 可以用来修饰函数;
singleton 可以用来修饰类






使用方法
------------
直接装饰在 需要的函数上面 即可,用法 如下:

.. code-block:: python

    import time
    from useful_decoration import single


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
