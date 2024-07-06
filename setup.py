from setuptools import find_packages,setup
from typing import List

def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","")  for req in requirments]

        return requirments

setup(
    name='Diamond Price Prediction',
    version='0.0.1',
    author='mohak',
    author_email='mohakkhandelwal19@gmail.com',
    install_requires=get_requirments('requirments.txt'),
    packages=find_packages()



)