# implement a class called Jar

class Jar:
    def __init__(self, capacity=12):
        # Ensure capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity  # Maximum number of cookies the jar can hold
        self._size = 0             # Current number of cookies in the jar

    def __str__(self):
        # Return a string of cookie emojis representing the current jar contents
        return "🍪" * self._size

    def deposit(self, n):
        # Add n cookies to the jar, unless it exceeds capacity
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies for the jar!")
        self._size += n

    def withdraw(self, n):
        # Remove n cookies from the jar, unless there aren't enough
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw!")
        self._size -= n

    @property
    def capacity(self):
        # Return the maximum capacity of the jar
        return self._capacity

    @property
    def size(self):
        # Return the current number of cookies in the jar
        return self._size
