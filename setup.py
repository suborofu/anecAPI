import os
import setuptools

NAME = 'anecapi'
DESCRIPTION = 'Russian anecdotes and jokes'
URL = 'https://github.com/suborofu/anecAPI'
EMAIL = 'alexfromsuvorov@gmail.com'
AUTHOR = 'suborofu'
REQUIRES_PYTHON = '>=3.6'

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as file:
    long_description = '\n' + file.read()

with open(os.path.join(here, 'VERSION'), 'r', encoding='utf-8') as file:
    VERSION = '.'.join([d for d in str(int(''.join(file.read().split('.')), 10) + 1).rjust(3, '0')])

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    packages=["anecAPI"],
    url=URL,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Text Processing :: Linguistic',
    ],
)

with open(os.path.join(here, 'VERSION'), 'w', encoding='utf-8') as file:
    file.write(VERSION)