"""Setup for pytest-nice plugin."""

from importlib_metadata import entry_points
from setuptools import setup

setup(
    name='pytest-nice',
    version='0.1.0',
    description='A pytest plugin to turn FAILURE into OPPORTUNITY',
    url='https://github.com/santosh',
    author='Santosh Kumar',
    author_email='sntshkmr60@gmail.com',
    license='proprietary',
    py_modules=['pytest_nice'],
    install_requires=['pytest'],
    entry_points={'pytest11': ['nice = pytest_nice',],},
)
