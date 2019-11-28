# -*- coding: utf-8 -*- 
"""
test  code_timer  decorations


"""
import time
from useful_decoration.timer import code_timer


def get_token():
    print("begin  code  ... ")
    with code_timer("sleep_code_block"):
        print("hello world")
        time.sleep(5)
        print("aaaaaaa")

    print("end code  ... ")


class Service:
    """ 异步 调用 Service

    """

    def __init__(self, timeout=10):
        self.timeout = timeout

    def query(self, text):
        """
        mock query
        :param text:
        :return:
        """
        with code_timer('query'):
            print(f"begin query .... {text}")
            time.sleep(6)
            print("end query  ... ")
        return 1



def  test_get_token():
    get_token()



def test_service():

    pass




if __name__ == '__main__':

    pass


    # get_token()
