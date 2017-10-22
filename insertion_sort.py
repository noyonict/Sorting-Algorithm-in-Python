def insertion_sort(a):
    """Insertion Sort in python 3"""
    for i in range(1, len(a)):
        j = i-1
        while a[j] > a[j+1] and j >= 0:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1


def insertion_sort_v2(a):
    """Insertion Sorting v2 algorithm in python 3"""
    for i in range(1, len(a)):
        cur_num = a[i]
        for j in range(i-1, 0, -1):
            if a[j] > cur_num:
                a[j+1] = a[j]
            else:
                a[j+1] = cur_num
                break

array = [12, 3, 43, 43, 9, 3, 2, 2, 43, 23, 53, 3, 3, 23, 23, 12, 53, 91]
print(array)
insertion_sort(array)
print(array)
insertion_sort_v2(array)
print(array)
