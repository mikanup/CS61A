HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(n)
    else:
        return term(n) + summation(n-1, term)


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    # 开始写成了column == row+1，就是死活想不明白
    if column == 0 or (column == row ):
        return 1
    if column > (row + 1):
        return 0
    return pascal(row - 1, column) + pascal(row - 1, column - 1)

print(pascal(3, 2))


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    if m == 1 or n == 1:
        return 1
    # 递归计算：从右边格子到终点的路径数 + 从下面格子到终点的路径数
    # 这一层确实没想到，总想着有两种可能，其实这两种可能的相加就是最后的总条路
    return paths(m, n - 1) + paths(m - 1, n)


print(paths(2, 2))


def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    cal_couple = [[x ,y] for x, y in zip(s, t)]
    return cal_couple


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return False
    # 我总想着每一位进行判断，chatgpt牛逼
    if n % 100 == 88:
        return True
    return double_eights(n // 10)
        


def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    # 一开始直接写成x和y了
    return [[x ,fn(x)] for x in seq if fn(x) >= lower and fn(x) <= upper]


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    temp = 0
    my_list = []
    for i in deck:
        if temp == 0:
            oddNum = deck[temp]
            my_list.append(oddNum)
        elif temp == 1:
            evenNum = deck[len(deck)//2]
            my_list.append(evenNum)
        elif temp % 2 == 0:
            oddNum = oddNum + 1
            my_list.append(oddNum)
        elif temp % 2 == 1:
            evenNum = evenNum + 1
            my_list.append(evenNum)
        temp = temp + 1
    return my_list
    # 问了chatgpt，它给的更好
    # # 使用列表推导式分别获取偶数索引和奇数索引的元素
    # even_index_elements = [deck[i] for i in range(0, len(deck), 2)]
    # odd_index_elements = [deck[i] for i in range(1, len(deck), 2)]

    # # 交替合并这两个列表
    # result = []
    # for even, odd in zip(even_index_elements, odd_index_elements):
    #     result.extend([even, odd])
    # 还有另外一种做法，确实没想到
    # mid = len(deck) // 2  # 找到中点
    # shuffled_deck = []
    # for i in range(mid):
    #     shuffled_deck.append(deck[i])  # 添加第一半的元素
    #     shuffled_deck.append(deck[i + mid])  # 添加第二半对应位置的元素
    # return shuffled_deck

print(riffle([3, 4, 5, 6]))