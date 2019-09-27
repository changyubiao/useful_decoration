.. _func:


.. 介绍了有一些如何检查 实例中的  的data 参数 来决定 是否要进行 执行一些函数.



func 模块介绍
===============
这个里面实现 了一个装饰器 ,该装饰器 用来检测 某个对象 的参数 是否合法,
如果 合法 则可以进行计算某个 方法,如果 参数不合法 ,直接返回默认值

本例子:

检查 例子中 参数 `data` 是否 为空, 如果为空 ,则不会进行 calculate 计算
如果 data 不为空,则进行 计算 正常返回 `calculate` 的结果.






第一个例子
------------

.. code-block:: python

    from useful_decoration.func  import  checked_arguments

    class Model:

        def __init__(self, data):
            self.data = data

        @checked_arguments(score='score', prob='prob')
        def calculate(self):
            return {
                "score": 100.0,
                "prob": 100.0,
            }


    if __name__ == '__main__':
        data = {'0': None, '1': None, '6': None, '7': None, '8': None, '9': None}

        model = Model(data=data)

        r = model.calculate()

        print(f"r :{r}")

..

结果如下:

.. code-block:: bash

    r :{'score': -111.0, 'prob': -222.0}
..


第二个例子
-----------

1. 这个例子正常 传入值

.. code-block:: python



    if __name__ == '__main__':
        data = {'0': 7, '1': 5, '6': 1, '7': 3, '8': 5, '9': 7}

        model = Model(data=data)

        r = model.calculate()

        print(f"r :{r}")  # { 'score':100.0,'prob':'100.0' }


..



说明
>>>>>>

这里通过 这两个例子 来说 这个装饰器的使用,这里 只是判断data 的值 是否为空,
作为 装饰 `calculate` 方法 . 通过 data 是否为空 来决定 是否 执行 `calculate` 方法 .
