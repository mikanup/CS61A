def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    # 一开始for循环放在最外面了
    # 后来f的函数没有调用参数
    def func(f):
        for i in range(1,n+1):
            if f(i):
                print(i)
    return func

# def is_even(x):
#     return x % 2 == 0
# make_keeper(5)(is_even)

def f1():
    """
    >>> f1()
    3
    """
    # 定义了一个lambda表达式，这个表达式不接受任何参数，并且返回3
    # 通过这对括号，我们立即调用了前面定义的lambda表达式。因此，它返回3，这个值随后作为f1`函数的返回值
    return (lambda: 3)()

def f2():
    """
    >>> f2()()
    3
    """
    # f2()：调用f2，返回一个lambda表达式。
    # ()：这个lambda表达式被调用，返回3`。
    return lambda : 3

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x : x

def f4():
    """
    >>> f4()()(3)()
    3
    f4()返回第一个lambda函数。
    第一个()调用第一个返回的lambda函数，它返回第二个lambda函数lambda x: lambda: x。
    (3)调用第二个返回的lambda函数，传入3作为x，返回第三个lambda函数lambda: 3。
    最后一个()调用第三个lambda函数，返回3。
    """
    return lambda: lambda x: lambda: x