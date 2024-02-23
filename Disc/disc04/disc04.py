def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
print(count_stair_ways(4))

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if k == 1:
        return 1
    if n == 0:
        return 1
    if n < 0:
        return 0
    else:
        count = 0
        for i in range(1,k+1):
            count = count + count_k(n - i,k)
        return  count
print(count_k(10, 3))

a = [1, 5, 4, [2, 3], 3]
print(a[0],a[-1])
print(len(a))
# False
print(2 in a)
print(a[3][0])

def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    # 忘记列表的用法了
    # 发现总是会被思维定式了，知道一种解法，就一直这么做
    return [ i * s[i] for i in range(len(s))if i % 2 == 0]
x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))

s = []
print(len(s))

def max_product(s):
    """Return the maximum product that can be formed using
    non-consecutive elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        # 不选择当前第一个元素：这意味着你将继续寻找剩余列表（即s[1:]）中非连续元素的最大乘积
        # 选择当前第一个元素：如果选择了当前的第一个元素，那么为了确保元素是非连续的，下一个可选择的元素将是从s[2:]开始的列表中的元素。
        # 这时，你需要计算选择了当前元素后，剩余部分能得到的最大乘积，即s[0]乘以从s[2:]开始的子列表的最大乘积。
        return max(max_product(s[1:]), s[0] * max_product(s[2:]))
    # chatgpt的做法
    # def max_product_helper(s, start, product):
    #     if start >= len(s):
    #         return product
    #     choose_current = max_product_helper(s, start + 2, product * s[start])
    #     skip_current = max_product_helper(s, start + 1, product)
    #     return max(choose_current, skip_current)
    # if len(s) == 0:
    #     return 1
    # return max_product_helper(s, 0, 1)
print(max_product([10,3,1,9,2]))

pokemon = {'pikachu': 25, 'dragonair': 148}
# {'pikachu': 25, 'dragonair': 148}
print(pokemon)
# False
print('mewtwo' in pokemon)
# 2
print(len(pokemon))

pokemon['mew'] = pokemon['pikachu']
pokemon[25] = 'pikachu'
# {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu'}
print(pokemon)

pokemon['mewtwo'] = pokemon['mew'] * 2
# {'pikachu': 25, 'dragonair': 148, 'mew': 25, 25: 'pikachu', 'mewtwo': 50}
print(pokemon)

# 下面是错误的，不能这么添加
# 请注意，最后一个示例演示了字典不能使用其他可变数据结构作为键。但是，字典可以任意深入，这意味着字典的值可以是字典本身。
# pokemon[['firetype', 'flying']] = 146