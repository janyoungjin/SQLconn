from setuptools import setup, find_packages

setup(
    name='SQLconn',
    version='0.0.1',
    description='This package facilitates easy SQL database integration.',
    author='janyoungjin',
    install_requires=['mysqlclient', 'pandas', 'cx_oracle', 'psycopg2', 'pymssql'],
    packages=find_packages(exclude=[]),
    keywords=['mysql', 'postgresql', 'sqlite', 'mssql', 'oracle', 'sql']
)