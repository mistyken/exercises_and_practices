def getPermutations(array):
	# Write your code here.
	permutations = []
	permHelper(0, array, permutations)
	return permutations

def permHelper(i, array, perms):
	if i == len(array) - 1:
		perms.append(array.copy())
	else:
		for j in range(i, len(array)):
			array[i], array[j] = array[j], array[i]
			permHelper(i + 1, array, perms)
			array[i], array[j] = array[j], array[i]

print(getPermutations([1,2,3,4]))