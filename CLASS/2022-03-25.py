#2022-03-25

#007
'''
n = int(input("GG: "))
for x in range(n,-n-1,-1):
    print(int(x))
'''

#008
'''
a = []
n1 = int(input("Number: "))
a = input("GG: ").split(' ')
for i in range(n1):
    a[i] = a[i].capitalize()
a.sort()

for x in a:
    print(x)
'''


#009
'''
n = input('GG: ')

def is_palindrome(n):
    for i in range(len(n)//2):
        if n[i] != n[-1-i]:
            return False
    
    return True

print(is_palindrome(n))
'''

#010
'''
n1 = input('Type the number: ')
n2 = int(input('Type number: '))

print(n1[n2+1:] + n1[:n2+1])
'''

#008

















