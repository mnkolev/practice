numbers = [10, 20, 300 , 40, 50]
print(numbers[0])

# for num in numbers:
# 	print(num)

for i in range(len(numbers)):
	print(numbers[i])

	#prints all items for index 0 to n-1
	print(numbers[0:-1])

#search for biggest number
#linear search has O(N) runtime
maximum = numbers[0]
for num in numbers:
	if num > maximum:
		maximum = num

print(maximum)