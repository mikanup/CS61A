def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m, n-1)


def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return n * skip_mul(n - 2)
    
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # 问chatgpt的
    # 开始确实没想到还可以继续调用函数
    def check_prime(i):
        if i * i > n:
            return True
        if n % i == 0:
            return False
        return check_prime(i + 1)
    if n < 2:
        return False
    # 从2开始检查
    return check_prime(2)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    # 做出来像上个函数的做法，最后问chatgpt的
    # 看了之后豁然开朗
    print(n)
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + hailstone(n // 2)
    else:
        return 1 + hailstone(n * 3 + 1)
        

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    if n1 == 0 and n2 == 0:
        return 0
    elif n1 == 0:
        return n2
    elif n2 == 0:
        return n1

    last_digi1_n1 = n1 % 10
    last_digi1_n2 = n2 % 10

    if last_digi1_n1 < last_digi1_n2:
        return merge(n1 // 10, n2) * 10 + last_digi1_n1
    else:
        return merge(n1, n2 // 10) * 10 + last_digi1_n2

print(merge(31, 42))  # 输出: 4321
#print(merge(21, 0))   # 输出: 21
print(merge(21, 31))  # 输出: 3211