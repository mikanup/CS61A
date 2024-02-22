def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    if k == 0:
        return 1
    answer = 1
    while k > 0:
        answer = answer * n
        n = n - 1
        k = k - 1
    return answer


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    sum = 0
    while y > 0:
        digit = y % 10
        sum = sum + digit            
        y = y // 10
    return sum



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    # while n > 0:
    #     digit = n % 10
    #     if digit == 8:
    #         n = n // 10
    #         digit = n % 10
    #         if digit == 8:
    #             return True
    #         else:
    #             n = n // 10
    #             continue
    #     else:
    #         n = n // 10
    # return False
    # 在做lab04的时候，找出之前做的，总觉得不精简，找chatgpt改了一下
    pre_digit = 0
    while n > 0:
        digit = n % 10
        if digit == 8 and pre_digit == 8:
            return True
        pre_digit = digit
        n = n // 10
    return False   
        
