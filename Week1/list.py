a = [10, 20, 'Gfg', 60, 9.0]
print(a)

print(a[0])
print(a[4])
print(a[4])
print(a[3])
print(a[2])

b = ['nabeel', 90]
print(a+b)

c = ['billy']
print(b+c)

print(type(a[2]))
print(type(a[4]))
print(type(a[3]))
print(type(b))

a = [10, 'gfg', 3.4, True]
print(type(a[3]))

print(a+b+c+a)

a = [30, 40 , 20, 50]
a.remove(40)
print("after remove(40):",a)

a = ['nabeel',20, 'billy', 3.4, True]
a.remove('billy')
print('after remove(billy)',a)

a.remove(True)
print('after remove(true)', a)
