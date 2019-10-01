# -*- coding: utf-8 -*- 

import time
from useful_decoration.timer import fn_timer


@fn_timer()
def get_token():
    time.sleep(3)
    return 0


@fn_timer(prefix='frank_')
def pickup():
    time.sleep(2)


@fn_timer(prefix='frank_', interval=1.5)
def pickup():
    time.sleep(1)

    print("pickup is calling.")
    pass

if __name__ == '__main__':
    # get_token()

    pickup()

    pass
