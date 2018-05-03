import os, sys
from setuptools import setup, find_packages
import MaybeP2P

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
    name = 'MaybeP2P',
    packages = find_packages(exclude=['__pycache__', '*.txt']),
    version = MaybeP2P.__version__,
    description = 'Simple solution to implement P2P communication into Applications.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    author = 'cl5ode(jackey8616)',
    author_email = 'jackey8616@gmail.com',
    url = 'https://github.com/jackey8616/MaybeP2P',
    download_url = '',
    keywords = ['P2P', 'peer-to-peer'],
    install_requires = [
        'dnspython'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5'
    ],
    python_requires = '>=2.7'
)
