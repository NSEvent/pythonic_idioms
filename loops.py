# For each loop
# Same thing as
# for i in range(0, 5):
for i in range(5):
	print(i)

# Reverse for each loop 
for i in reversed(range(5)):
	print(i)
###################################################

# Idiomatic examples to traverse lists
numbers = ['zero', 'one', 'two', 'three', 'four']

# Traverse in order
for num in numbers:
	print(num)
	
# Traverse in reverse order
for num in reversed(numbers):
	print(num)
	
# Traverse in order with indices
for i, num in enumerate(numbers):
	print(f'{i}->{num}')
	
# Traverse n lists in order in parallel up to the len of the shortest list
colors = ['red', 'green', 'blue']
for num, color in zip(numbers, colors):
	print(f'{num}->{color}')
	
# Traverse in sorted order
for num in sorted(numbers):
	print(num)

# Traverse in key sorted order
for num in sorted(numbers, key=len):
	print(f'{num} (len={len(num)})')
###################################################

# For else
res = None
for i in range(5):
	if (i == 5):
		res = i
		break
else: # No break
	res = -1
	
print(res)
