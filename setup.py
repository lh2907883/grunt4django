# coding: utf-8
from setuptools import setup, find_packages
 
setup (
    name = 'grunt4django',
    version = '1.0.4',
    py_modules = ['grunt4django'],
    author = 'lihao',
    author_email = 'lihao12518@163.com',
    description = '包含django的runserver命令，还有针对html的中间件(添加livereload)',
    url = 'https://github.com/lh2907883/grunt4django',
    packages = find_packages(),
)