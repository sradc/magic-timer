# magic-timer

![](https://github.com/sradc/magic-timer/workflows/Python%20package/badge.svg)


`pip install magic-timer`


Conveniently get a rough idea of how long things take.


#### Use via decorator:

```python
from magic_timer import MagicTimer, magic_timer
import time

@magic_timer
def some_slow_function():
    time.sleep(3)

some_slow_function()
```

```
>> magic-timer: 'some_slow_function' - 0:00:00:03:000
```


#### Use via MagicTimer object:

```python
def some_slow_function():
    time.sleep(2)

timer = MagicTimer()

some_slow_function()

print(timer)
```

```
>> 0:00:00:02:000
```

Output is in: days:hours:minutes:seconds:milliseconds

- See [notebook](https://github.com/sradc/magic-timer/blob/master/magic-timer_nb.ipynb).


(Note: this package is tiny, and just uses time.time() to measure time)


If you want precision / accuracy, use something like [timeit](https://docs.python.org/3.8/library/timeit.html).
