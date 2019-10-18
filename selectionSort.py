def findsmallest(arr):
    # 定义初始状态
    sml_value = arr[0]
    sml_index = 0
    for i in range(1, len(arr)):
        if arr[i] < sml_value:
            sml_value = arr[i]
            sml_index = i
    return sml_index

def selectionSort(arr):
    # 新建目标数组
    new_arr = []
    n = len(arr)
    while len(new_arr)<n:
        i = findsmallest(arr)
        new_arr.append(arr[i])
        arr.pop(i)
    print(new_arr)

arr = [4,2,5,9,3]
selectionSort(arr)