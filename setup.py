import setuptools
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='anecapi',
    version='0.0.3',
    description='Russian anecdotes and jokes',
    license='MIT',
    author="suborofu",
    author_email='alexfromsuvorov@gmail.com',
    packages=["anecAPI"],
    url='https://github.com/suborofu/anecAPI',
    keywords= ['anecdotes', 'jokes', 'funny', 'russian', 'ussr'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    includepackagedata=True
)