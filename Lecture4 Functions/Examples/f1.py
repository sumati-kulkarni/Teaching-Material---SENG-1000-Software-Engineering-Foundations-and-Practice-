
print("0.................")

x = 10
i = 0
while i < x:
	print('i=',i)
	i += 1

	
def f1(k):
	i = 0
	while i < k:
		print('i=',i)
		i += 1

print("1.................")

f1(10)

print("2.................")
# Is this possible? Yes why not in Python :-)
def f1(k):
	i = k-1
	while i >= 0:
		print('i=',i)
		i -= 1

print("3.................")
f1(10)