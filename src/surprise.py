from functools import wraps


def surprise(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("surprise!")

    return wrapper


if __name__ == "__main__":
    @surprise
    def say_hello():
        print("Hello!")

    say_hello()