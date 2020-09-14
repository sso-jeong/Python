"""
문제 1 ~ 문제 12
"""
a=80
b=75
c=55
print((a+b+c)/3)

d=13%2
print(d)

hongCode="881120-1068234"
print(hongCode[0:6])
print(hongCode[7:])

pin = "881120-1068234"
print(pin[7])

a = "a:b:c:d"
print(a.replace(":","#"))

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
print(" ".join(a))

a = (1,2,3)
a = a + (4,)
print(a)

a = dict()
{}
a['name'] = 'python'
a[('a',)] = 'python'
# a[[1]] = 'python'
a[250] = 'python'

a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))

a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
a2 = set([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5])
b = list(a2)
print(b)

a = b = [1, 2, 3]
a[1] = 4
print(b)


