# magic-timer

[![](https://github.com/sradc/magic-timer/workflows/Python%20package/badge.svg)](https://github.com/sradc/magic-timer/commits/)


`pip install magic-timer`


Conveniently get a rough idea of how long things take.

#### Use via decorator:

```python
from magic_timer import MagicTimer, magic_timer, format_output
import time

@magic_timer
def some_slow_function():
    time.sleep(2.75)

some_slow_function()
```

```
> 'some_slow_function' - 2.8 seconds
```


#### Use via MagicTimer object:

```python
def some_slow_function():
    time.sleep(90/1000)
  
timer = MagicTimer()

some_slow_function()

print(timer)
```

```
> 94 milliseconds
```

##### Format time in seconds into an appropriate unit, rounded to two sig figs:

```python
print(format_output(365*24*60*60))
print(format_output(2*24*60*60))
print(format_output(4.2*60*60))
print(format_output(3.11*60))
print(format_output(45.38))
print(format_output(.334))
print(format_output(.00008422))
print(format_output(.0))
```

```
> 370 days
> 2.0 days
> 4.2 hours
> 3.2 minutes
> 46 seconds
> 340 milliseconds
> 85 microseconds
> t < 0.05 microseconds
```

See also this [notebook](https://github.com/sradc/magic-timer/blob/master/magic-timer_nb.ipynb).

This package is tiny. It uses time.time() to measure time. For greater precision & accuracy, you could use something like [timeit](https://docs.python.org/3.8/library/timeit.html).
