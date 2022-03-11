# anecAPI

[![PyPI version](https://badge.fury.io/py/anecapi.svg)](https://pypi.python.org/pypi?:action=display&name=anecapi)
[![Downloads](https://pepy.tech/badge/anecapi)](https://pepy.tech/project/anecapi)
[![License: MIT](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)


## Description
`anecAPI` allows you to display funny (or not) USSR/Russian jokes (also called anecdotes).
> All jokes are in Russian only.

## Installation

```
pip install anecapi
```

## Example

### In Console

```
C:\anecAPI> python anecAPI.py -h
usage: anecAPI.py [-h] [-m] [-s] [-a]

Displays a funny (or not) USSR/Russian joke (also called anecdote).

optional arguments:
  -h, --help    show this help message and exit
  -m, --modern  display a modern Russian joke
  -s, --soviet  display an old USSR joke
  -a, --any     display a USSR/Russian joke (default)

C:\anecAPI> python anecAPI.py -m
Штирлиц с Навальным пили водку и вдруг Навальный отрубился
"Новичок"- подумал Штирлиц
```

### In Code

```python
from anecAPI import anecAPI

print(anecAPI.modern_joke()) # Displays a modern Russian joke
print(anecAPI.soviet_joke()) # Displays an old USSR joke
print(anecAPI.random_joke()) # Displays a random USSR or Russian joke
```
