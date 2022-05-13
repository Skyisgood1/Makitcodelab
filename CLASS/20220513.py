#2022-05-13

'''
arr = set(1,2,3,1,1,2,4,5)
print(arr)
# set => 중복을 없애준다
'''

#   Intro
'''
N,M = map(int,input().split())
A = set()
B = set()

for i in range(N):
    A.add(input())
for i in range(M):
    B.add(input())

result = list(A & B)
result.sort()
print(len(result))
for i in result:
    print(j)
'''


# list의 개수 = n

import random
arr = []
for i in range(1000000):
    arr.append(random.randint(1,1000000))
print(arr)
start = time.time()
print(merge_sort(arr))
end = time.time()
print("Merge Sort: ", str(end-start))

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    #len(arr)=5
    #mid=2
    #left=0,1
    #right=2,3,4
    mid = len(arr)//2
    arr_left = merge_sort(arr[:mid])
    arr_right = merge_sort(arr[mid:])

    arr_result = []
    l = r = 0
    while left < len(arr_left) and right < len(arr_right):
        if arr_left[left] < arr_right[right]:
            arr_result.append(arr_left[left])
            left += 1
        else:
            arr_result.append(arr_right[right])
            right += 1

    arr_result += arr_left[left:]
    arr_result += arr_right[right:]

    return arr_result
    






























































































