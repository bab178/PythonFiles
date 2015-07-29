try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Skeletor',
    'author': 'Blake Bordovsky',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'blakebordovsky@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Skeletor'],
    'scripts': [],
    'name': 'Skeletor'
}

setup(**config)