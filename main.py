
def my_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs):
        print("before")
        func(*args, **kwargs)
        print("after")
    return wrapper


@my_decorator
def say_hello():
    print("hello")


def main():
    say_hello()


if __name__ == '__main__':
    main()
