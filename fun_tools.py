#! /usr/bin/python # -*- coding: utf-8 -*-

# func_tools

import functools
import re



def curry(function):
    """
    Returns a curried version of the given function `f`.

    Parameters:
        f (function): The function to be curried.

    Returns:
        function: A curried version of the given function `f`.
    """

    curried = lambda *args, **kwargs: function(*args, **kwargs)
    return curried


def currry(xunction, argc=None):
    """
    Generates a curried version of a function.

    Args:
        x: The function to be curried.
        argc: The number of arguments the function takes. Defaults to None.

    Returns:
        A curried version of the function.

    Example:
        >>> def add(x, y):
        ...     return x + y
        >>> curried_add = currry(add)
        >>> curried_add(2)(3)
        5
    """
    if argc is None:
        argc = xunction.__code__.co_argcount

    def punction(*a):
        if len(a) == argc:
            return xunction(*a)

        def qunction(*b):
            return xunction(*(a + b))

        return currry(qunction, argc - len(a))

    return punction


def cury(xunction, argc=None):
    """
    Returns a curried version of the given function.

    Parameters:
    - x: The function to be curried.
    - argc: The number of arguments that the curried function should take. If not provided, it defaults to the number of arguments of the original function.

    Returns:
    - A curried version of the given function.

    Example:
    curried_func = cury(my_func, argc=3)
    result = curried_func(1)(2)(3)
    """
    if argc is None:
        argc = xunction.__code__.co_argcount

    def punction(*a):
        if len(a) == argc:
            return xunction(*a)

        def qunction(*b):
            return xunction(*(a + b))

        return currry(qunction, argc - len(a))

    return punction


def compose(*functions):
    """
    Composes multiple functions into a single function.

    Parameters:
        *functions (Callable): The functions to be composed.

    Returns:
        Callable: The composed function.
    """
    return functools.reduce(lambda f, g: lambda *x: f(g(*x)),
                            functions, lambda x: x)



match = curry(lambda x, y: re.findall(x, y))


class Nothing:
    """Nothing Monad."""
    def __repr__(self) -> str:
        """
        Returns a string representation of the object.
        This method is used by the built-in `repr()` function and by string
        formatting operations when no `__format__()` method is defined.

        :return: A string representation of the object.
        :rtype: str
        """
        return 'nothing'


class Maybe:
    """Maybe monad."""
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        """
        Return a string representation of the container.

        Returns:
            str: The string representation of the container.
        """
        return f'Container({self.value.__repr__()})'

    def is_nothing(self):
        """
        Check if the value of the current object
        is an instance of the `Nothing` class.

        Returns:
            bool: True if the value is an instance
            of `Nothing`, False otherwise.
        """
        return isinstance(self.value, Nothing)

    def map(self, function):
        """
        Apply a given function to the value
        inside the Maybe monad.

        Parameters:
            f (function): The function to apply.

        Returns:
            Maybe: A new Maybe monad with the
            result of applying the function to the value.
        """
        if self.is_nothing():
            return Nothing()
        return Container(function(self.value))


class Container:
    """Identity container."""

    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        """
        Return a string representation of the Container object.
        The returned string is formatted as 'Container(value)'
        where value is the string representation of the
        self.value attribute.

        Returns:
            str: The string representation of the Container object.
        """
        return f'Container({self.value.__repr__()})'

    def is_nothing(self):
        """
        Check if the value of the object is an instance of the Nothing class.

        Returns:
            bool: True if the value is an instance of Nothing, False otherwise.
        """
        return isinstance(self.value, Nothing)

    def map(self, function):
        """
        Apply the function `f` to the value
        contained in the Maybe monad.

        Parameters:
            f (function): The function to be applied
            to the value.

        Returns:
            Maybe: A new Maybe monad containing
            the result of applying `f` to the value.
        """
        if self.is_nothing():
            return Nothing()
        return Maybe(function(self.value))


class IO:
    """INPUT/OUTPUT"""
    def __init__(self, function) -> None:
        self.value = function

    def map(self, function):
        """
        Applies a function to the value inside
        the IO monad and returns a new IO monad
        with the result.

        Parameters:
        - fn: A function that takes the value
        inside the IO monad as input and returns a new value.

        Returns:
        - IO: A new IO monad with the result of
        applying the function to the value inside
        the original IO monad.
        """
        return IO(compose(function, self.value))

    def __repr__(self) -> str:
        """
        Returns a string representation of the `IO` object.

        :return: A string representation of the `IO` object.
        :rtype: str
        """
        return f'IO({self.value.__repr__()})'

    def add(self, other):
        """
        Adds the value inside the IO monad to another value
        of the same type and returns a new IO monad with the result.

        Parameters:
        - other: Another value of the same type as the value
        inside the IO monad.

        Returns:
        - IO: A new IO monad with the result of adding the values.
        """
        current_value = self.value()
        result = current_value + other
        return IO(lambda: result)

    def update_value(self, new_value):
        """
        Updates the value inside the IO monad with
        a new value.

        Parameters:
        - new_value: The new value to be stored inside
        the IO monad.
        """
        self.value = lambda: new_value  # Wrap the new value in a lambda

from cachetools import LRUCache

cache = LRUCache(maxsize=128)
