#Assignment Operators

x = 10
x+=1  #increment
print(x)

x = 10
x-=1  #decrement
print(x)

x = 10
x*=5  #multiple
print(x)

x = 10
x%=1 #moduler
print(x)

x = 10
x//=1 # floar division
print(x)

x = 10
x/=1 # division
print(x)

# Bitwise Operators


a = 12 # binary: 1100
b = 10 # binary: 1010

print("a :", format(a, '04b'), f"({a})")   # format (variable/value ,'specification') It prints the value of a in binary format, along with its original decimal value. 
print("b :", format(b, '04b'), f"({b})")   # Not necessary you can use it if you want # '04b' used for binary value 
print()                                    # 0:add necessary 0 at starting , 4 for for digit output(Eg.0001.0010) b: represents binary conversion

print("a and b :", format(a & b, '04b'), f"({a & b})") # AND
print("a or b :", format(a | b, '04b'), f"({a | b})") # OR
print("a xor b :", format(a ^ b, '04b'), f"({a ^ b})") # XOR
print("not a :", ~a) # NOT
print("left shift a by 2 :", format(a << 2, 'b'), f"({a << 2})") # Left shift
print("right shift a by 2 :", format(a >> 2, '04b'), f"({a >> 2})") # Right shift
