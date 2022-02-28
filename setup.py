from setuptools import setup

setup(
    name='fqdn',
    entry_points={
        'console_scripts': [
            'getfqdn = fqdn:main',
        ],
    },
    py_modules=['fqdn'],
)
