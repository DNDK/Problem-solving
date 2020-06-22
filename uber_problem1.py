"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""
# Without NumPy(with numpy there not neccessary to write Prod function)
def prod(arr:list):
	result = 1
	for i in arr:
		result *= i
	return result

arr = [int(a) for a in input().split()]
new_arr = []

for i in arr:
	buff_arr = arr
	ind = buff_arr.index(i)
	buff_arr.remove(i)
	new_arr.append(prod(buff_arr))
	buff_arr.insert(ind, i)

print(new_arr)
