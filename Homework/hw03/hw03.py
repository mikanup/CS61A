HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    # 一开始写成了当前取到的一位数是否是0
    if pos == 0:
        return 0
    # 人是真的神奇，刚刚在disc03做过类似的，所以一下子就能想到了
    elif pos % 10 == 8:
        return 1 + num_eights(pos//10)
    else:
        return num_eights(pos // 10)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    # 非递归版本
    # result = 0
    # temp = 1
    # for i in range(1,n+1):
    #     result = result + temp
    #     if (num_eights(i) > 0) or ( i % 8 == 0):
    #         temp  = temp * -1
    # return result 
    # 递归版本
    def f(result, i, temp):
        if i >= n:
            return result
        elif (num_eights(i) > 0) or ( i % 8 == 0):
            return f(result-temp, i+1, temp*-1)
        else:
            return f(result+temp, i+1, temp)
    return f(1, 1, 1)

# print(pingpong(10))
# print(pingpong(15))
# print(pingpong(21))
# print(pingpong(22))
# print(pingpong(30))
# print(pingpong(68))
# print(pingpong(80))

def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    # 遗憾，小金没有自己做出来
    def f_count_coins(change, coin):
        # 如果钱最后算出来刚好是0，那就是成功的，算一次
        if change == 0:
            return 1
        # 算出来小于的，说明这条路走不通
        if change < 0:
            return 0
        # 取到比当前币值小一号的
        next_coin = next_smaller_coin(coin)
        # 初始化还钱数量的变量
        way = 0
        # 使用当前面额的硬币，然后继续尝试相同的面额（change减去当前硬币的值）。
        way = way + f_count_coins(change-coin, coin)
        # 跳过当前面额的硬币，尝试下一个较小面额的硬币
        if next_coin is not None:
            way = way + f_count_coins(change, next_coin)
        return way
    return f_count_coins(change, 25)
   
print(count_coins(15))

anonymous = False  # Change to True if you would like to remain anonymous on the final leaderboard.


def beaver(f):
    # 看答案的，老实说，我看不懂。。。
    (lambda g: g(g(g(g(g(g(g(f))))))))(lambda f: lambda: f() or f() or f())() 


def beaver_syntax_check():
    """
    Checks that definition of beaver is only one line.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> source = inspect.getsource(beaver)
    >>> num_comments = source.count('\\n    #')
    >>> contains_default_line = '"*** YOUR CODE HERE ***"' in source
    >>> num_lines = source.count('\\n') - num_comments
    >>> (num_lines == 2) or (num_lines == 3 and contains_default_line)
    True
    """
    # You don't need to edit this function. It's just here to check your work.


def beaver_run_test():
    """
    Checks to make sure f gets called at least 1000 times.

    >>> counter = 0
    >>> def test():
    ...     global counter
    ...     counter += 1
    >>> beaver(test)
    >>> counter >= 1000
    True
    """
    # You don't need to edit this function. It's just here to check your work.
