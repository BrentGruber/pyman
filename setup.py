from setuptools import setup

setup(
    name = 'pyman',
    version = '0.1.0',
    packages = ['pyman'],
    entry_points = {
        'console_scripts': [
            'pyman = pyman.cli:main'
        ]
    }
)