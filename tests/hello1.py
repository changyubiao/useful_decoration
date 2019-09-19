# -*- coding: utf-8 -*- 
"""
@User     : Frank
@File     : setup.py
@DateTime : 2019-09-16 11:24 
@Email    : frank.chang@lexisnexis.com
"""
import io
import re

with io.open("src/useful_decoration/__init__.py", "rt", encoding="utf8") as f:
    content = f.read()
    print(content)
    # version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

    version = re.search(r'__version__ = "(.*?)"', content).group()

    print(version)




if __name__ == '__main__':
    pass
