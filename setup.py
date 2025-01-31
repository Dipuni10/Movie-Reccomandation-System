from setuptools import setup

with open("README.md","r",encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'DIPUNI SATHUA'
SRC_REPO = 'src'
LIST_OF_REQUIREMENT = ['streamlit']

setup(
    name= SRC_REPO,
    version='0.0.1',
    author='DIPUNI_SATHUA',
    author_email='dipuni.sathua042@gmail.com',
    description='A small example package for movies reccomedation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package=[SRC_REPO],
    python_requires ='>=3.7',
    install_requires = LIST_OF_REQUIREMENT,
)