L1 = [0,1,2,3,4,5,6,7,8,9,10]

print('\n...............')
for ch in L1:
	print(ch)

print('\n...............')

i = 0
j = len(L1)
while i < j:
	print(L1[i])
	i += 1

print('\n...............')

i = 0
while i < j:
	print(L1[:i])
	i += 1
	
print('\n...............')

i = 0
while i < j:
	print(L1[i:])
	i += 1

print('\n...............')

i = 0
while i < j:
	print(L1[i:i+10])
	i += 1

print('\n...............')
#print(L1[50]) # Error
print('\n...............')

i = -1
j = -1 * len(L1)
while i >= j:
	print(L1[i])
	i -= 1

print('\n...............')

i = -1
j = -1 * len(L1)
while i >= j:
	print(L1[i:0:-1])
	i -= 1
	
print('\n...............')

i = -1
j = -1 * len(L1)
while i >= j:
	print(L1[i:0:-1],L1[0])
	i -= 1
	
print('\n...............')

i = -1
j = -1 * len(L1)
while i >= j:
	print(L1[i:0:-2])
	i -= 1