print('a1', 'b2') # a1 b2
print('a1', 'b2', sep=', ') # a1, b2

print('aa', end=' ')
print('bb') # aa bb

a = ['A', 'B']
print(' '.join(a)) # A B

idx = 1
fruit = 'Apple'
print('{0}: {1}'.format(idx + 1, fruit)) # 2: Apple
print(f'{idx + 1}: {fruit}') # 2: Apple