from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


# All abstract classes should inherit from ABC (Abstract Base Class)
class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    # All subclass must implement this method
    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading from file stream")


class NetworkStream(Stream):
    def read(self):
        print("reading from network stream")


# stream = Stream() -> wont work as stream class is abstract
stream = NetworkStream()
stream.read()