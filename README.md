# magic-timer

[![](https://github.com/sradc/magic-timer/workflows/Python%20package/badge.svg)](https://github.com/sradc/magic-timer/commits/)

`pip install magic-timer`

Conveniently get a rough idea of how long things take. 

This is a light wrapper around the standard library's [time.monotonic](https://docs.python.org/3/library/time.html#time.monotonic). 


## How to use:

## Use via `MagicTimer` object:

```python
from magic_timer import MagicTimer

def do_stuff():
    [i*i for i in range(5_000_000)]

timer = MagicTimer()
do_stuff()
print('Stuff took', timer)
```

```
> Stuff took 455 milliseconds
```

## Use via `ftimer` decorator:

```python
from magic_timer import ftimer

@ftimer
def do_stuff():
    [i*i for i in range(20_000_000)]

do_stuff()
```

```
> `do_stuff` ran in 1.9 seconds.
```

#### The use case for this package: 

You have something you want to time, but you don't want to time it multiple times with [timeit](https://docs.python.org/3/library/timeit.html).

You also don't want to use [Jupyter's `%%timeit`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) because it puts the cell into a different scope.

You can import `magic-timer`, throw it in, and get a rough idea of the time taken.

You could of course use time.monotonic directly, but it's not quite as neat.
