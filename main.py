
def my_decorator(func: callable) -> callable:
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
