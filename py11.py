# 23-10-2025

#Identity Operator in Python

a = [10, 20, 30]
b = a
c = [10, 20, 30]
d = [40, 50, 60]

c = a
c = d

print(a is c)
print(b is a)
print(c is d)
print(c is a)

# Memory Address

print(id(a))
print(id(b))
print(id(c))
print(id(d))