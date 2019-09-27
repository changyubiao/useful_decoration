.. _decrations:


decorations模块说明
===================

  element_mapping 这个装饰器
  用来 修饰 类方法, 成员方法 ,静态方法 的返回结果,
  如果 返回为不是一个字典类型, 转成字典返回  {factor_name:value},
  如果返回 类型 是一个字典类型 , 则直接返回, 不做任何处理.


第一个例子
----------
.. code-block:: python

    from useful_decoration.decorations import element_mapping


    class Person:

        def __init__(self, name):
            self.name = name

        @element_mapping(factor_name="factor")
        def calculate(self):
            return 10


        @classmethod
        @element_mapping(factor_name='pick')
        def pickup(cls):
            return 20

    if __name__ == '__main__':
        p = Person()

        print(p.calcalute())  #{'person': 10}

        print(p.pickup())  # {'pick': 20}

        pass

..


说明
-----

这个装饰器 用来 指定一个本来返回一个值的函数,或者方法  让其 返回 一个字典,
字典的key 就是 自己指定的 factor_name  这个变量 .


