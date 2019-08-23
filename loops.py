# For each loop
# Same thing as
# for i in range(0, 5):
for i in range(5):
	print(i)

# Reverse for each loop 
for i in reversed(range(5)):
	print(i)


# Idiomatic examples to traverse numbers
 numbers = ['zero', 'one', 'two', 'three', 'four']

for num in numbers:
	print(num)

for num in reversed(numbers):
	print(num)

for i, num in enumerate(numbers):
	print(f'{i}->{num}')
