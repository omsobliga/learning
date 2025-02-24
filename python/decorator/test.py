

def dec(*args, **kwargs):
    print(args, kwargs)

    pass


@dec("demo")
def f(a, b):
    print(a, b)

