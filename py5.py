#20-10-2025

# Using Global Keyword

a = 10

def hey():
    global a
    a = 1000
    print(a)
print(a)

hey()
print(a)
