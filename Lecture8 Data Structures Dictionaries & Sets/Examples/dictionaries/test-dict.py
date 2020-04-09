#clear()	Removes all the elements from the dictionary
#copy()	    	Returns a copy of the dictionary
#fromkeys() 	Returns a dictionary with the specified keys and values
#get()		Returns the value of the specified key
#items()	Returns a list containing the a tuple for each key value pair
#keys()		Returns a list contianing the dictionary's keys
#pop()		Removes the element with the specified key
#popitem()	Removes the last inserted key-value pair
#setdefault()	Returns the value of the specified key. 
#		If the key does not exist: insert the key, with the specified value
#update()	Updates the dictionary with the specified key-value pairs
#values()	Returns a list of all the values in the dictionary

St = 'abcdefghiABCDEFGHIaabbccddeefffffg'
S = set(St)
L= list(St)
T = tuple(St)

print('\n  1................\n')
print('St=',St)

print('\n  2................\n')
print('L=',L)

print('\n  3................\n')
print('S=',S)

print('\n  4................\n')
print('T=',T)

print('\n  5................\n')
t = (1,2), (3,4), ('a',10), (St, S), (T, L)
print('t=',t)

print('\n  6................\n')
D = dict(t)
print('D=',D)

print('\n  7................\n')
for i in D:
    print('i=',i)

print('\n  8................\n')
for i in D.items():
    print('i=',i)

print('\n  9................\n')
for i in D.keys():
    print('i=',i)

print('\n  10................\n')
for i in D.values():
    print('i=',i)

print('\n  11................\n')
for i,v in D.items():
    print('i=',i,'  ','v=',v)


