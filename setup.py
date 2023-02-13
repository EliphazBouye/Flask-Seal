"""
Flogin
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flogin',
    version='1.0',
    url='http://github.com/EliphazBouye/flogin/',
    license='MIT',
    author='Eliphaz BOUYE',
    author_email='eliphazbouye@gmail.com',
    description='Flogin provides user session management for flask',
    long_description=__doc__,
    py_modules=['flogin'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)