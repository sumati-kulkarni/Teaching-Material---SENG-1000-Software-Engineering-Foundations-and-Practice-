t = ()
print(t)
print(type(t))
print(len(t))

print('......................')

t = 10,20,30, 10, 50
print(t)
print(type(t))
print(len(t))

print('......................')

for i in t:
	print(i)

print('......................')

s = {1,2,3,4,5,6}
print(s)
print(type(s))
print(len(s))

print('......................')

s = set(t)
print(s)
print(type(s))
print(len(s))

print('......................')

L = [1,2,3,4,5, 1,2,3,4, t, s]
print(L)
print(type(L))
print(len(L))

print('......................')

#s = set(L) # TypeError: unhashable type: 'set'
L.pop()
s = set(L) # # tuples are hashable, so it is OK
print(s)
print(type(s))
print(len(s))

print('......................')

total = 0
product = 1

for i in range(1, 10 + 1):
    num = float(input("Please enter number " + str(i) + " : "))
    total += num
    product *= num

average = total/10

print("Sum: ", total, "\nProduct: ", product, "\nAverage: ", average)

