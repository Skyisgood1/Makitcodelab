#2022-03-11

#000 - 변외 
'''
sum = 0
n1 = int(input("GG1: "))
n2 = input("GG2: ").split(' ')
for i in range(n1-2):
    print(int(n2[i])+int(n2[i+1])+int(n2[i+2]))
'''

#001
'''
n1 = float(input("Ty1: "))
n2 = float(input("Ty2: "))
print(n1+n2)
'''

#002
'''
n1 = input("Type: ")
upn1 = n1.upper()
n2 = input("Type: ")
upn2 = n2.upper()

if upn1 == upn2:
    print("TRUE")
else:
    print("FALSE")
'''

#003 - UNKNOWN
'''
n1 = int(input("Type number: "))
n2 = int(input("Type an another number: "))
for i in range(n1):
    if i==0 or i==n1-1:
        print('*'*n2)
    else:
        print("*" + ' '*(n2-2) + "*")
'''

#004

n1 = input("Type a word: ")
n2 = int(input("Type number:... "))
for x in range(1,len(n1)+1):
    print(int(x))









