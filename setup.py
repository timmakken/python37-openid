import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
# README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='python37-openid',
    version='0.1',
    packages=[''],
    description='A line of description',
    # long_description=README,
    author='tim',
    author_email='yourname@example.com',
    url='https://github.com/timmakken/python37-openid.git',
    license='MIT',
    install_requires=[
        'Django>=3.6',
    ]
)