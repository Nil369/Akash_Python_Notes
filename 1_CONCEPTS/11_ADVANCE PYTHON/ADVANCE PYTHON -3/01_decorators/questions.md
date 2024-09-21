# learn about decorators

- Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of a function or class. 
- Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it. 

```python
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " mili sec")
        return result
    return wrapper


@time_it
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result


@time_it
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
```

<details>
<summary>
Problem 1: Timing Function Execution
</summary>
Problem: Write a decorator that measures the time a function takes to execute.
</details>


<details>
<summary>
Problem 2: Debugging Function Calls
</summary>
Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.
</details>


<details>
<summary>
Problem 3: Cache Return Values
</summary>
Problem: Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function.
</details>


