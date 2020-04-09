L1 = [0,1,2,3,4,5,6,7,8,9,10]

i = 0
j = len(L1)
while i < j:
	print(L1[i],end=',')
	i += 1

print('\n...............')

i = 0
while i < j:
	print(i,' ',L1[i])
	i += 1

print('\n...............')

i = 0
while i < j:
	r = '{0:2}:{1:2}'.format(i,L1[i])
	print(r)
	i += 1
	
print('\nLeft aligned...............')

i = 0
while i < j:
	r = '{0:<2}:{1:<2}'.format(i,L1[i])
	print(r)
	i += 1

print('\nRight aligned...............')

i = 0
while i < j:
	r = '{0:>2}:{1:>2}'.format(i,L1[i])
	print(r)
	i += 1	

	
print('\nRight aligned With fill...............')

i = 0
while i < j:
	r = '{0:>2}:{1:>2}'.format(str(i).zfill(2),L1[i])
	print(r)
	i += 1	
print('\n')
print('Good Luck :-)')



