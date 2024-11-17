# list 清單

a = ['Ford', 'Honda']
print(a)
print(a[0])
print(a[1])
a.append('Skoda')
print(a)
print(len(a))
print('Toyota' in a) #是非題
print('Skoda' in a)

#字串當清單

car = 'Audi'
#['A','U','D','I']
for c in car:
	print(c)

print(len(car))

print('A' in car)