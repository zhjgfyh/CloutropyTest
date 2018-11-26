# -*-coding:utf-8-*-

# Date: 2018.11.14
# ToDo: 选择排序（还有一些问题）

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
        return smallest_index

# print(findSmallest([5, 3, 6, 2, 10]))


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(smallest)
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))

