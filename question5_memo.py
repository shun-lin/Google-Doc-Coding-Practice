Technical Practice Question: Assume from (x,y) you can go (x+1,y+1),(x+1,y) or (x+1. y-1). How many ways can you choose to go from (0,0) to (x,0)?

Question:
1) Is there any coordinate (x, y) that we are not allowed to go? i.e is there any blocks?
2) Is there any off bound? i.e. is (1, -1) off bound.

Assumptions:
1) We can go to any square
2) We assume that there is no off bound

Term:
Going up means from (x, y) to (x, y + 1)

We have three options:
Going right -> (x, y) to (x + 1, y)
Going up and right -> (x, y) to (x + 1, y + 1)
Going down and right -> (x, y) to (x + 1, y - 1)


Sample Input/Outputs:
1.
Input: (1, 0)
Output: 1

2.
Input: (2, 0)
Output: 3

3.
Input: (0, 0)
Output: 0

Idea:
There are three ways to from column x - 1 to column x
previous step of arriving at (x, 0) must be either (x - 1, 0) or (x - 1, 1) or (x - 1, - 1)

W((x, y)) -> means that ways to get to (x, y)
Recurrence relationship:
W((x,y)) = W((x-1,y)) + W((x-1,y-1)) + W((x-1,y+1))
The ways to go to x,y is the sums of the ways to the previous step (which is consist of three ways)

One solution: use recursion using the recurrence relationship we found and use memoization to save time.

Runtime for not using memo:

T(x) = 3T(x-1) + O(1)
So the running time complexity without memoization is 3^x

Space: dominated by the recursive stack , O(x)

using memoization:
O(x^2)

Code: (Using memoization)

# return the number of ways, in integer, from (0,0) to (x, 0) using the given guideline
def ways(x):
	# memoization table having tuple (x, y) as key and W((x,y)) as the value
	memo = dict()

	# return the number of ways from 0,0 to x,y
	def helper(x, y):
		key = (x, y)
		if (key in memo):
			return memo[key]
		ways_from_left_down = helper(x-1, y-1)
		ways_from_left_up = helper(x-1, y+1)
		ways_from_left = helper(x-1, y)
		result = ways_from_left_down + ways_from_left_up + ways_from_left
		memo[key] = result
		return result

	return helper(x, 0)
