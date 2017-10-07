Question:

Input: an array of sorted integers
Output: the index of a particular integer

Question:
1) are the integers unique?
2) If not unique, which index should I return?
3) Are the query going to be valid? If not, how should I handle errors (throw exception or should I return -1)

I will code in python for this question

Assumptions:
1) The integers will be unique.
2) Return the index of the integer, since it is unique.
3) Inputs always be valid

# return the index within x such that arr[index] = x;
def findIndex(arr, x):
	# find the index where arr[index] = x and index is in between low and high
	def helper(arr, low, high, x):
		if (low == high):
			return low;
		mid = (low + high) / 2
		if (arr[mid] == x):
			return x
		elif (arr[mid] > x):
			return helper(arr, low, mid, x)
		else:
			return helper(arr, mid, high, x)

	return helper(arr, 0, len(arr) - 1, x)
