# -*- coding: utf-8 -*- 
"""
@User     : Frank
@File     : setup.py
@DateTime : 2019-09-16 11:24 
@Email    : frank.chang@lexisnexis.com
"""
from setuptools import find_packages


if __name__ == '__main__':
    # packages = find_packages(exclude=('test',))
    packages = find_packages()


    print(packages)
