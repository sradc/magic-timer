# magic-timer

[![](https://github.com/sradc/magic-timer/workflows/Python%20package/badge.svg)](https://github.com/sradc/magic-timer/commits/)


`pip install magic-timer`


A simple timer, for conveniently getting a rough idea of how long things take.


This is not for precision / accuracy; for that use something like [timeit](https://docs.python.org/3/library/timeit.html). 


This package basically just makes timing with time.monotic() fractionally more convenient.


This package is not recommended for measuring sub 100 millisecond times.


Output is in an appropriate unit, rounded to two significant figures. 
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
> 95 milliseconds
```


See also this [notebook](https://github.com/sradc/magic-timer/blob/master/magic-timer_nb.ipynb).


The use case: you have a function you want to time, but you don't want to time it multiple times with `timeit`,
and you don't want to use Jupyter `%%timeit` because `%%timeit` puts the cell into a different scope.
You can import `magic-timer`, throw it on, and get a rough idea of the elapsed time.


This is somewhat of a [pico](https://en.wikipedia.org/wiki/Pico-)-package...
