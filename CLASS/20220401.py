#2022-04-01
'''
sum = 0
n = int(input("Enter the number: "))
for x in range(1,n+1):
    sum += x
print(sum)

'''

#재귀 코드
'''
def solution(n):
    print(n)
    if n<100:
        solution(n+1)
solution(1)

def print_to_n(n):
    if n>1:
        print_to_n(n-1)
    print(n)
print_to_n(20)
'''

'''
def solution(n):
    if n < 20:
        solution(n+1)
    print(n)
solution(1)

def print_to_n(n):
    print(n)
    if n > 1:
        print_to_n(n-1)
print_to_n(20)
'''

'''
n = int(input("Number: "))
for x in range(1,n+1):
    if x % 3 == 0 and x % 5 == 0:
        print(x, '은 3과 5의 베수입니다.')
'''

'''
n = list(input())
for i in range(len(n)-1,-1,-1):
    print(n[i],end=' ')
'''

'''
def solution(n,arr):
    if n < len(arr)-1:
        solution(n+1,arr)
    print(arr[n],end = ' ')
arr = list(input())
solution(0,arr)
'''

'''
def solution(n,arr):
    print(arr[n],end = ' ')
    if n > 0:
        solution(n-1,arr)
arr = list(input())
solution(len(arr)-1,arr)
'''

'''
def solve(n):
    if n == 0:
        return 0
    print(n%10,end = ' ')
    solve(n//10)
print('입력을 정수를 거꾸로 출력하는 프로그램이다. ')
n = int(input("정수를 입력하세요."))
solve(n)
'''

'''
n = int(input("Enter number: "))
result = 1
if n == 0:
    print('1')
else:
    for x in range(1,n+1):
        result *= x
    print(result)
'''

''' #팩토리얼
def solution(n):
    if n == 0 or n == 1:
        return 1

    return n * solution(n-1) 

n = int(input())
print(solution(n))
'''

''' #피보나치 수열
def solution(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return solution(n-1) + solution(n-2)
n = int(input())
print(solution(n))
'''

''' #dynamic programming
n = int(input())
arr = [0] * (n+1)
arr[0] = 0
arr[1] = 1

for i in range(2,n+1):
    arr[i] = arr[i-1]+arr[i-2]
print(arr[n])
'''

'''
for x in range(1,7):
    for y in range(1,7):
        for z in range(1,7):
            print(x,y,z)
print()
'''

'''
#순열
from itertools import permutations
data = [1,2,3]
cnt = 0
for i in permutations(data,2):      
    print(i)
    cnt += 1
print(cnt)

#조화
from itertools import combinations
data = [1,2,3]
cnt = 0
for i in combinations(data,2):
    print(i)
    cnt += 1
print(cnt)

#중복순열
from intertools import product
data = [1,2,3,4,5,6]
cnt = 0
for i in product(data,repeat=3):
    print(i)
    cnt += 1
print(cnt)

#중복조화
from itertools import combinations_with_replacement
data = [1,2,3,4,5,6]
cnt = 0
for i in combinations_with_replacement(data,3):
    print(i)
    cnt += 1
print(cnt)
'''

'''
from itertools import product
data = [1,2,3,4,5,6]
n = int(input("h: "))
cnt = 0
for x in product(data,repeat=3):
    if x[0] + x[1] + x[2] == n:
        print(x[0],x[1],x[2]) 
'''

from itertools import combinations
n = int(input())
data = [i for i in range(1,n+1)]
cnt = 0 
for x in combinations(data,6):      
    print(x)
    cnt += 1
print(cnt)
























