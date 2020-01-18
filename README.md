# magic-timer

[![](https://github.com/sradc/magic-timer/workflows/Python%20package/badge.svg)](https://github.com/sradc/magic-timer/commits/)


`pip install magic-timer`


A simple timer. Conveniently get a rough idea of how long things take.


Output is in appropriate unit, rounded to two significant figures. 
Note that 3 digit numbers are also rounded to 2 sig figs, e.g. 231 -> 240.


#### Use via decorator:

```python
from magic_timer import MagicTimer, magic_timer
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


See also this [notebook](https://github.com/sradc/magic-timer/blob/master/magic-timer_nb.ipynb).

This package is tiny. It uses time.time() to measure time. For greater precision & accuracy, you could use something like [timeit](https://docs.python.org/3.8/library/timeit.html).
