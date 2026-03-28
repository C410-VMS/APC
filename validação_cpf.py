cpf = [1,4,5,7,8,9,6,5,1,2,0,7]
v = 10
m = 0

for i in cpf[:9]:

    print(f"{i}*{v}")
    m += i * v
    v = v - 1

print(m)