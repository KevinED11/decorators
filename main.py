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
        correct_password = "secret"
        password = input("Enter password: ")

        if password != correct_password:
            raise IncorrectPasswordException(f"Wrong password '{password}'")

        return func(*args, **kwargs)

    return wrapper


class ServerService:
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

    server = ServerService()
    server.stop()
    print(server.status)


if __name__ == "__main__":
    main()
