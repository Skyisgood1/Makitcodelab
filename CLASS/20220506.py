#2022-05-06

#001
'''
N = int(input())
arr = []
for i in range(N):
    [n,m] = map(int,input().split())
    arr.append([n,m])

arr.sort()

for i in range(N):
    print(arr[i][0],arr[i][1])
'''

#002
'''
n1 = int(input())
arr = list(map(int,input().split()))
cnt = 0

for i in range(1,n1):
    for idx in range(1,n1-i+1):
        if arr[idx-1] > arr[idx]:
            arr[idx-1],arr[idx] = arr[idx],arr[idx-1]
            cnt += 1
        print(arr)
print(cnt)
'''

#003
'''
N,K = map(int(input()))
arr= list(map(int,input().split()))
cnt = 0
    
for i in range(1,N):
    for idx in range(1,N-i+1):
        if arr[idx-1] > arr[idx]:
            arr[idx-1],arr[idx] = arr[idx],arr[idx-1]

    cnt += 1
    if cnt == K:
        break

for i in range(N):
    print(arr[i],end = ' ')
'''

#004
'''
N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

for i in range(N-1):
    idx = i
    for j in range(i+1,len(N)):
        if arr[j] < arr[idx]:
            idx = j
    arr[i],arr[idx] = arr[idx],arr[i]

for i in range(N):
    print(arr[i])
'''
#005
'''
N,K = map(int,input().split(' '))
arr = list(map(int,input().split(' ')))

for i in range(1,len(arr)):
    current = arr[i]
    j = i-1
    while j >= 0 and arr[j] > current:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = current
print(arr[K-1])
'''



    
            
            
        






















































































