from abc import ABC, abstractmethod
import os


def my_decorator(func: callable) -> callable:
    """
    A function that acts as a wrapper around another function.
    """

    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")

    return wrapper


@my_decorator
def say_hello():
    print("hello")


class MyDecorator:
    def __init__(self, func: callable):
        self.func = func

    def __call__(self, *args, **kwargs):
        """
        Call the function and print "before" before executing the
        function and "after" after executing the function.
        """
        print("before")
        self.func(*args, **kwargs)
        print("after")


@MyDecorator
def say_hello2():
    print("hello2")


def my_decorator_name(name: str) -> callable:
    def my_custom_decorator(func: callable) -> callable:
        def wrapper(*args, **kwargs):
            print("before")
            print("Hello, " + name)
            result = func(*args, **kwargs)
            print("after")
            return result

        return wrapper

    return my_custom_decorator


@my_decorator_name("John")
def suma(a: int, b: int) -> int:
    return a + b


class IncorrectPasswordException(Exception):
    pass


def ask_for_password(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> None:
        password_by_default = "secret"
        correct_password = os.environ.get("PASSWORD", default=password_by_default)
        password = input("Enter password: ")

        if password != correct_password:
            raise IncorrectPasswordException(f"Wrong password '{password}'")

        return func(*args, **kwargs)

    return wrapper


class IServerService(ABC):
    @ask_for_password
    @abstractmethod
    def start(self) -> None:
        pass

    @ask_for_password
    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def status(self) -> str:
        pass


class SyncServerService(IServerService):
    def __init__(self):
        self.__running = False

    @ask_for_password
    def start(self) -> None:
        self.__running = True
        print("Starting server, please wait")

    @ask_for_password
    def stop(self) -> None:
        if not self.__running:
            print("Server is not running")
            return

        print("Stopping server")
        self.__running = False

    @property
    def status(self) -> str:
        print("Server status")
        return f"running: {str(self.__running)}"


def main():
    say_hello()
    say_hello2()
    print(suma(1, 2))

    server_instance = SyncServerService()
    try:
        server_instance.start()
        server_instance.stop()
        print(server_instance.status)
    except IncorrectPasswordException as err:
        print(f"{type(err).__name__}:", err)


if __name__ == "__main__":
    main()
