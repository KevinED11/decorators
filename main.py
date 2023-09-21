
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


def main():
    say_hello()
    say_hello2()


if __name__ == '__main__':
    main()
