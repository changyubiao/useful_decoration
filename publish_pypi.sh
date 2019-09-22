#!/usr/bin/env bash


# enter virtual environment

# 检查打包文件
echo "begin  python setup.py check  "
python setup.py  check


echo " begin  python setup.py sdist bdist_wheel "
# 打包
python setup.py sdist bdist_wheel


echo " begin twine upload dist/*  "
# 发布包
twine upload dist/*


