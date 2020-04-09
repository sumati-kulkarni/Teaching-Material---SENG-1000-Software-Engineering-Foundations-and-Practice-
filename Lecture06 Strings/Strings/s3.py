s1 = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"

print('\n...............')
for ch in s1:
	print(ch)

print('\n...............')

i = 0
j = len(s1)
while i < j:
	print(s1[i])
	i += 1

print('\n...............')

i = 0
while i < j:
	print(s1[:i])
	i += 1
	
print('\n...............')

i = 0
while i < j:
	print(s1[i:])
	i += 1

print('\n...............')

i = 0
while i < j:
	print(s1[i:i+10])
	i += 1

print('\n...............')
#print(s1[50]) # Error
print('\n...............')

i = -1
j = -1 * len(s1)
while i >= j:
	print(s1[i])
	i -= 1

print('\n...............')

i = -1
j = -1 * len(s1)
while i >= j:
	print(s1[i:0:-1])
	i -= 1
	
print('\n...............')

i = -1
j = -1 * len(s1)
while i >= j:
	print(s1[i:0:-1] + s1[0])
	i -= 1
	
print('\n...............')

i = -1
j = -1 * len(s1)
while i >= j:
	print(s1[i:0:-2])
	i -= 1