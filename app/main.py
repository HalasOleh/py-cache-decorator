from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def inner(*args: Callable, **kwargs: Callable) -> Any:

        try:
            key = args
            if kwargs:
                key = args + tuple(sorted(kwargs.items()))
        except TypeError:
            raise TypeError("Arguments must be hashable")

        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            print("Calculating new result")
            result[key] = func(*args, **kwargs)
            return result[key]

    return inner
