# 4.1:sum函数代码
def sum1(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum1(arr[1:])

# 4.2:递归函数计算列表包含的元素数
def len_ele(arr):
    if arr == []:
        return 0
    else:
        return 1 + len_ele(arr[1:])

# 4.3:找出列表中最大的数字：
def max_num(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return [arr[0]] if arr[0]>= arr[1] else [arr[1]]
    else:
        return max_num([arr[0]]+ max_num(arr[1:]))

# 4.3书上答案:
# 试了一下python的max,空列表的max会报错。然而书上的答案没有考虑只有一个元素的情况？？？
# def max_num(arr):
#     if len(arr) == 2:
#         return arr[0] if arr[0]>= arr[1] else arr[1]
#     else:
#         sub_max = max(arr[1:])
#         return arr[0] if arr[0] >= sub_max else sub_max

# 修改：
def max_num1(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[0]>= arr[1] else arr[1]
    else:
        sub_max = max_num1(arr[1:])
        return arr[0] if arr[0]>= sub_max else sub_max

# 快速排序：
def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]
        return quicksort(quicksort(less) + [pivot] + quicksort(greater))
