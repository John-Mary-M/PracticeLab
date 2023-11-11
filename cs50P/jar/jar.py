"""cs50p 11/11/2023 jar.py"""


class Jar:
    """cookie jar"""

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0  # Track the balance
        self.balance = 0

        if self.balance > 0 or self.balance > 12:
            raise ValueError

    def __str__(self):
        """should return a str with n, where n
        is the number of cookies in the cookie jar. For instance,
        if there are 3 cookies in the cookie jar, then str should
        return '🍪🍪🍪'"""
        return f"{self._size * '🍪'}"

    def deposit(self, n):
        """should add n cookies to the cookie jar. If adding that
        many would exceed the cookie jar’s capacity, though
        , deposit should instead raise a ValueError"""
        if n > self._capacity:
            raise ValueError

        if (self._size + n) > self._capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        """should remove n cookies from the cookie jar.
        Nom nom nom. If there aren’t that many cookies in the cookie jar
        , though, withdraw should instead raise a ValueError."""
        if self.size < n:
            raise ValueError
        self._size = self._size - n


    # @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size
