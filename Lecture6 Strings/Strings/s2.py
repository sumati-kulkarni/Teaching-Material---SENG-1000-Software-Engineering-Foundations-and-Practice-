s1 = "ABCDEFGHIJKLMNOPKRSTUVWXYZ"

i = 0
j = len(s1)
while i < j:
	print(s1[i],end=',')
	i += 1

print('\n...............')

i = 0
while i < j:
	print(i,' ',s1[i])
	i += 1

print('\n...............')

i = 0
while i < j:
	r = '{0:2}:{1:2}'.format(i,s1[i])
	print(r)
	i += 1
	
print('\nLeft aligned...............')

i = 0
while i < j:
	r = '{0:<2}:{1:<2}'.format(i,s1[i])
	print(r)
	i += 1

print('\nRight aligned...............')

i = 0
while i < j:
	r = '{0:>2}:{1:>2}'.format(i,s1[i])
	print(r)
	i += 1	

	
print('\nRight aligned With fill...............')

i = 0
while i < j:
	r = '{0:>2}:{1:>2}'.format(str(i).zfill(2),s1[i])
	print(r)
	i += 1	
print('\n')
print('Good Luck :-)')



