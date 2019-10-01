.. _timer:


..  实现检查函数运行时间的装饰器 该模块 实现了一个获取函数 运行时间的装饰器



timer 模块介绍
===============

该模块 实现了一个获取函数 运行时间的装饰器  *fn_timer*

这个 装饰器 有两个参数  prefix ,interval 默认是 0.0






默认参数
------------
直接装饰在 需要的函数上面 即可,用法 如下:

.. code-block:: python

    import time
    from useful_decoration.timer import fn_timer


    @fn_timer()
    def get_token():
        time.sleep(3)
        return 0

..

结果如下:

.. code-block:: bash

    2019-10-01 18:53:20.022 | INFO    | useful_decoration.timer:function_timer:37 - get_token total running time 3.00232195854187 seconds

..




prefix 参数
------------

1. 可以在装饰器里面传入prefix 参数, 给函数 加一个前缀, 如果你的项目 中有很多同名的函数,这个参数 通常是有用的.



.. code-block:: python

    import time
    from useful_decoration.timer import fn_timer




    @fn_timer(prefix='frank_')
    def pickup():
        time.sleep(2)
..



.. code-block:: bash

    2019-10-01 18:53:22.024 | INFO   | useful_decoration.timer:function_timer:37 - frank_pickup total running time 2.0009548664093018 seconds

..



interval 参数
-------------
这个参数 决定 是否要记录 log ,如果被装饰的函数运行时间 大于等于 `internal` 参数的时间,就会打印日志

.. code-block:: python


    import time
    from useful_decoration.timer import fn_timer



    @fn_timer(prefix='frank_', interval=1.5)
    def pickup():
        time.sleep(1)

        print("pickup is calling.")

..


结果如下:

.. code-block:: bash

    pickup is calling.

..

这个时候 就不会 打印函数的运行时间. 因为函数运行时间小于 1.5 s,所以就不会打印出来.



