#2022-04-29

#001
'''
1. 샆입 정렬
    - 최솟갓 선택

2. 버블 정렬
    -앞에서 뒤로
    -작은 것을 계속해서 앞으로 끈다

3, 선택 정렬
    - 최솟값을 선택해서 앞으로 가져온다
'''

#1. Bubble Sort

import random

def bubble_sort(arr):
    for i in range(1,len(arr)-1):
        for idx in range(1,len(arr)-i+1):
            if arr[idx-1] > arr[idx]:
                arr[idx-1],arr[idx] = arr[idx],arr[idx-1]
            print(arr)
    return arr

# arr = [25,22,19,27,47,35,50]
# print(bubble_sort(arr))

def lotto():
    arr = []
    for i in range(7):
        arr.append(random.randint(1,50))
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        idx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[idx]:
                idx = j
        arr[i],arr[idx] = arr[idx],arr[i]
        print(arr)

    return arr

arr_selection = lotto()
print(selection_sort(arr_selection))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i-1
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = current
        print(arr)
    return arr

arr_insertion = lotto()
print(insertion_sort(arr_insertion))






    
