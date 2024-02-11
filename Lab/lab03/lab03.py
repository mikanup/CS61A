from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.
    从左到右读取的数字为非递减的 True
    否则就是False

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    single_dig = x // 10
    if single_dig == 0:
        return True
    else:
        first_dig = x % 10    
        x = x // 10
    while x > 0:
        second_dig = x % 10
        if first_dig >= second_dig:
            first_dig = second_dig
            x = x // 10
        else:
            return False
    return True


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = 0
    first_dig = n % 10
    n = n // 10
    while n >= 0:
        current_dig = n % 10
        # 需要考虑是第一位的情况
        if(first_dig > current_dig) and (current_dig != 0):
            first_dig = current_dig
        else:
            if k == i:
                final = first_dig
                break
            i = i + 1
            first_dig = current_dig
        n = n // 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    # 一开始调用的函数写成了参数的函数，就一直不知道怎么出错了
    def f(x):
        # 等于0的情况没有考虑
        if n == 0:
            return x
        else:
            result = func(x)
            for i in range(n-1):
                result = func(result)
            return result
    return f


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f



def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    # 笑死，开始题目都没看懂
    return make_repeater(func, 2)
    


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False
    i = 2
    while i <= n:
        if not checker(i):
            # 这一步看答案的
            checker = (lambda f, i: lambda x : (x % i == 0) or f(x))(checker, i)
        i = i + 1
    return checker
    # # 方法2
    # # 自己做的
    # def f(x):
    #     checker = False
    #     for i in range(2,n+1):
    #         if x % i == 0:
    #             checker = True
    #             return checker
    #     return checker
    # return f
div_by_primes_under(10)(12)

def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f, i):
                def inner(x):
                    return x % i == 0 or f(x)
                return inner
            checker = outer(checker, i)
        i = i + 1
    return checker

'''
这些函数是在使用所谓的“Church数”，
这是一种用函数表示自然数的方法，由数学家Alonzo Church提出。
在Church数系统中，
每个自然数都表示为一个接受两个函数作为参数的高阶函数：一个是要应用的函数（记作f），另一个是初始值（记作x）。通过对f应用n次来表示数字n。
'''

# zero函数表示数字0。它返回一个函数，这个函数接受一个函数f和一个值x，然后直接返回x，相当于0次应用f。
def zero(f):
    return lambda x: x

# successor函数用于表示自然数的后继函数，即给定一个数字n，返回n+1。
# 在Church数的表示中，successor(n)将函数f应用于结果n(f)(x)一次。
def successor(n):
    return lambda f: lambda x: f(n(f)(x))

# one是通过对0应用一次successor函数得到的。在Church数中，one相当于一次应用函数f。
def one(f):
    """Church numeral 1: same as successor(zero)"""
    return lambda x :f(x)

# two是通过对0应用两次successor函数得到的，即successor(successor(zero))。它表示为两次应用函数f。
def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    return lambda x : f(f(x))


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    return n(lambda x : x + 1)(0)


def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.
    lambda f: lambda x: 定义了一个新的Church数的函数表示。
    m(f)(...) 表示将函数f应用m次。
    n(f)(x) 表示将函数f应用n次到x上。
    将n(f)(x)的结果作为参数传递给m(f)，这样就相当于总共应用了f m+n次。

    >>> church_to_int(add_church(two, three))
    5
    """
    return lambda f : lambda x : m(f)(n(f)(x))


def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    return lambda f : m(n(f))


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    return n(m)