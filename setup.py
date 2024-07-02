from setuptools import setup, find_packages

setup(
    name='Test',
    version='1.0.0',
    url='https://github.com/argoel21/5100HW9',
    author='Anjali Goel',
    author_email='arg8qqv@virginia.edu',
    description='my booklover package',
    packages=find_packages(),  # Automatically find packages
    install_requires=['pandas'],
)