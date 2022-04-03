# magic-timer

[![](https://github.com/sradc/magic-timer/workflows/Python%20package/badge.svg)](https://github.com/sradc/magic-timer/commits/)

`pip install magic-timer`

Conveniently get a rough idea of how long things take. 

This is a light wrapper around the standard library's [time.monotonic](https://docs.python.org/3/library/time.html#time.monotonic). It aims to provide a clean API, and nice output strings.


## How to use:

```python
from magic_timer import MagicTimer

timer = MagicTimer(history=True)
for i in range(3):
    expensive_computation()
    # Print nicely formatted string:
    print(f"{i} - elapsed time {timer}")

# Get the elapsed times that were printed:
print("timer.str_history =", timer.str_history)
```

```
0 - elapsed time 510 milliseconds
1 - elapsed time 1.1 seconds
2 - elapsed time 1.6 seconds
timer.str_history = [0.5046274580000158, 1.005028416000016, 1.510260250000016]
```

## Use via context manager:

```python
from magic_timer import MagicTimer

with MagicTimer() as timer:
    # do stuff
    x = sum(i*i for i in range(100_000))

# Print a nicely formatted string:
print('Stuff took', timer)

# Or get the elapsed time in seconds:
time_elapsed = timer.time_elapsed()
print(time_elapsed)
```

```
> Stuff took 8.0 milliseconds
> 0.007906290999997623
```

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

To pause the timer, use the `stop` method (restart with the `start` method):

```python
from magic_timer import MagicTimer

def do_stuff():
    [i*i for i in range(5_000_000)]

timer = MagicTimer()
do_stuff()
timer.stop()
print('Stuff took', timer)
time_elapsed = timer.time_elapsed()
other_stuff()
timer.start()  # continue timing
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

### The use case for this package:

You have something you want to time, but you don't want to time it multiple times with [timeit](https://docs.python.org/3/library/timeit.html).

You also don't want to use [Jupyter's `%%timeit`](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) because it puts the cell into a different scope.

You can import `magic-timer`, throw it in, and get a rough idea of the time taken. (It's slightly neater than using time.monotonic directly.)
