#2022-03-04
'''
print('test')
'''
#001
'''
n1 = input("GG1: ")
n2 = input("GG2: ")
print(n1 + n2)
'''

#002
'''
min = 0
max = 10000
n1 = int(input("GG1: "))
n2 = int(input("GG2: "))
if n1 > n2:
    print(n2)
else:
    print(n1)
'''

#003
'''
n1 = int(input("GG1: "))
n2 = int(input("GG2: "))
for x in range(n2):
    for y in range(n1):
        print('*', end = '')
    print()
'''

#004
'''
n1 = input("GG1: ")
n2 = input("GG2: ")
print(n2 + n1 + n2)
'''

#005
'''
x = int(input("GG1: "))
y = int(input("GG2: "))
if y == 0:
    print("다시해라")
else:
    print(x//y)
'''

#006
'''
n1 = input("GG1: ")
n2 = input("GG2: ")
max = 0
min = 0
if len(n1) > len(n2):
    max = len(n1)
    min = len(n2)
    print(len(n1) - len(n2))
else:
    max = len(n2)
    min = len(n1)
    print(len(n2) - len(n1))
'''

#007
'''
n1 = int(input("GG1: "))
n2 = int(input("GG2: "))
for x in range(n1,n2+1):
    print(x)
'''

#008

sum = 0
n1 = int(input("GG1: "))
n2 = input("GG2: ").split(' ')
for x in range(1,len(n2)+1,1):
    sum += x
print(sum)


#009
'''
n1 = input("n: ")
print(n1.count('0'))
'''





























