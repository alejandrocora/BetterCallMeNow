import sys
from setuptools import setup, find_packages

requires = [
    'bs4'
]

setup(
    name='callme',
    description=("Automated program to request phone calls from (most) of websites that allow this option, usually related to insurance or TSP companies."),
    version='1.0',
    install_requires=requires,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['callme=callme.app:main'],
    },
    long_description=open('README.md').read(),
    keywords=['phone', 'call', 'requester']
)
