from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'

def get_packages(file_path:str):
    req = []

    with open(file_path) as obj:
        req =  obj.readlines()
        req = [x[0:len(x) - 1] for x in req ]

        if HYPHEN_E_DOT in req:
            req.remove(HYPHEN_E_DOT)

        print(req)

    return req



setup(
    name='regrssor_project',
    version='0.0.1',
    author='sahil',
    author_email='sahil15shinde@gmail.com',
    install_requires=get_packages('requirments.txt'),
    packages=find_packages()
)