try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'IEX Cloud Python Bot',
    'author': 'Gahfy',
    'url': 'https://github.com/gahfy/iexcloud',
    'download_url': 'https://github.com/gahfy/iexcloud',
    'author_email': 'gahfydev@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['iexcloud'],
    'scripts': [],
    'name': 'IEX Cloud'
]

setup(**config)
