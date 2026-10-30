#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5 

n = 5
for i in range(1,n+1):
    print((n-i)*' '+(str(i)+" ")*i)


# A
# BB
# CCC
# DDDD
# EEEEE

num = 64 #Alph "A" to "Z" starts from 65 in ascii and "a" to "z" starts from 96
for i in range(1,6):
    print((chr(num+i))*i)  #ord() for alpha to ascii  and chr() for ascii to alpha


num = 96 #Alph "A" to "Z" starts from 65 in ascii and "a" to "z" starts from 97
for i in range(1,6):
    print((chr(num+i))*i) 

