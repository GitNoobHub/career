# 复制分为深复制和浅复制
# 浅复制只复制了序列或字典中的直接子元素的内存位置。对于一般数据类型如字符串，数字等，复制的就是该值的内存地址。
# 对于序列如列表，只复制了这个列表的内存地址而不是这个列表里的元素的内存地址。而深复制则不同，它复制了原来序列的
# 所有元素（直接子元素，子孙元素）的内存地址。

# 字典浅拷贝实例
# >>>a = {1: [1,2,3]}
# >>> b = a.copy()
# >>> a, b
# ({1: [1, 2, 3]}, {1: [1, 2, 3]})
# >>> a[1].append(4)
# >>> a, b
# ({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})



# 深度拷贝需要引入 copy 模块
# >>>import copy
# >>> c = copy.deepcopy(a)
# >>> a, c
# ({1: [1, 2, 3, 4]}, {1: [1, 2, 3, 4]})
# >>> a[1].append(5)
# >>> a, c
# ({1: [1, 2, 3, 4, 5]}, {1: [1, 2, 3, 4]})