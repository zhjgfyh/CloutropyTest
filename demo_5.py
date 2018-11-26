# -*-coding:utf-8-*-

# Date: 2018.11.14
# ToDo: 二分查找

def binary_search(testlist, item):
    low = 0
    high = len(testlist) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = testlist[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
