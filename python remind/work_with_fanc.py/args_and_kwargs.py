#def my_function(*args):
   # for arg in args:
   #     print(arg)

#my_function(1, 2, 3, "hello")  # Вывод: 1 2 3 hello


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("До вызова функции")
        result = func(*args, **kwargs)
        print("После вызова функции")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print("Hello, " + name)

say_hello("Alice")