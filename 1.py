import random, wrap
wrap.world

q = 0
s=0
p=0
while q<5:
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    o = input("сколько будет " + str(a) + "*" + str(b))
    o = int(o)
    if o==a*b:
        s=s+1
    else:
        p=p+1

    q = q+1

print("правильных ответов - " + str(s))
print("неправильно - " + str(p))
