# For loop 
# A for loop is a programming control flow statement that executes a block of code repeatedly, 
# typically when the number of iterations is known in advance. 
# Syntax: for i in Seq/range(start,end,steps)

print("___________________________________________________________________")
#WAP to print 1 to 10 number 
for i in range(1,11):
    print(i)

print("___________________________________________________________________")
#WAP to print 1 to 10 number in reverse
for i in range(10,0,-1):
    print(i)

print("___________________________________________________________________")
#list itereation using for 
l1 = [55,66,99,36,56]
for i in l1:
    print(i)

print("___________________________________________________________________")
#WAP no btn 20 to 50 form given list
l2 = [65,88,63,45,33,22,21,20]
for i in l2:
    if 20<=i<=50:
        print(i)

print("___________________________________________________________________")
#WAP to print all vovel from string
str1 = "my name is Onkar "
v = "AEIOUaeiou"
for i in str1:
    if i in v:
        print(i,end=' ')

#WAP to print all vovel and there count from string
# THis program will repeat the vowel as well as count 
str1 = "my name is Onkar "
for i in str1:
    if i in "AEIOUaeiou":
        print(f"{i}: {str1.count(i)}") 

##WAP to print all vovel and there count from string
str1 = "my name is Onkar".lower()

for v in "aeiou":
    print(f"{v} = {str1.count(v)}") 
    