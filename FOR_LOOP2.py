s = input("Enter string: ")
v_list =[]
c_list =[]
n_list =[]
sp_list =[]
space=[]
v_c = 0
n_c = 0
s_c = 0
sa_c= 0
co_c= 0
for i in s.lower():
    if i in "aeiou":
        v_c+=1
        v_list.append(i)
    elif i in "0123456789":
        n_c+=1
        n_list.append(i)
    elif i in "!@#$%^&*()":
        sp_list.append(i)
        s_c+=1
    elif i in space:
        sa_c+=0
        space.append(i)
    else:
        co_c+=1
        c_list.append(i)

print(f"total no of vowel: {v_c}")
print(v_list)

print(f"total no of number: {n_c}")
print(n_list)

print(f"total no of Special char: {s_c}")
print(sp_list)

print(f"total no of Special char: {co_c}")
print(c_list)

print(f"total spaces:{sa_c}")


