import sys
import os
from io import open
from setuptools import setup, find_packages


long_description = 'Please see our GitHub README'
if os.path.exists('README.txt'):
    long_description = open('README.txt', 'r', encoding='utf-8').read()


def getRequires():
    deps = ['python_http_client>=3.0']
    if sys.version_info < (2, 7):
        deps.append('unittest2')
    elif (3, 0) <= sys.version_info < (3, 2):
        deps.append('unittest2py3k')
    return deps


setup(
    name='sendgrid',
    version='5.6.0',
    author='Elmer Thomas, Yamil Asusta',
    author_email='dx@sendgrid.com',
    url='https://github.com/sendgrid/sendgrid-python/',
    packages=find_packages(exclude=["temp*.py", "register.py", "test"]),
    include_package_data=True,
    license='MIT',
    description='SendGrid library for Python',
    long_description=long_description,
    install_requires=getRequires(),
    classifiers=[
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
