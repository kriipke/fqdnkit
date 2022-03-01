from setuptools import setup
import os

setup(
    name='fqdn',
    entry_points={
        'console_scripts': [
            'getfqdn = fqdn:main',
        ],
    },
    py_modules=['fqdn'],
    scripts=[os.path.join('bin','genfqdn')],
)
