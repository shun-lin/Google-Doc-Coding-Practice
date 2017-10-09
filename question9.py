Technical Question: Given a sequence of N numbers – A[1] , A[2] , …, A[N] . Find the length of the longest non-decreasing sequence.

Questions for interviewer:
1) Are those numbers all integers?
2) Are they all positive, can they be negative?
3) Are we outputting an integer?

Assumptions based on the above questions:
1) Yes all the numbers are all integers.
2) Numbers can be negative, as we want the longest non-decreasing sequence.
3) Yes we are outputting an integer.

Brute force:
Create all possible sequences and find the longest non-decreasing sequence, this will take a lot of time and space. O(2^n) as each element in A can either be in a sequence or not so we can treat each index as a boolean and thus O(2^n)

Example:
Input: [1, 2, 3, 4]
Output: 4

Input: [0, -1, 2, -1, 2, 3]
Output: 4

Input: []
Output: 0

Input: [0, -1, 2, -1, 2, 3, -1, 1, 2]
Output: 4

Input: [1]
Output: 1

Idea:
We can use recursion or dynamic programming to solve this problem.
We need to find two things, base case and recurrence relationship.

Let L[i] be the longest sequence end at index i.
Let arr be the input array
Base case L[0] = 1.
L[i] = max(for j less than i, L[j] if arr[j] > arr[i], or L[j] + 1 if arr[j] <= arr[i])

In words, L[i] is the max of the previous L[j]'s (some + 1 if arr[j] <= arr[i])

Our solution can be dynamic programming or memoization, we will try the memoization approach.

Solution 1 (memoization):

def longestNonDecreasingSeq(arr):
	memo = dict()

	# return L[i] as described above
	def helper(arr, i):
		if (i in memo):
			return memo[i]
		if (i == 0):
			memo[0] = 1
			return 1

		result = 0
		for j in range(0, i):
			L_of_j = helper(arr, j)
			if (arr[j] <= arr[i]):
				L_of_j += 1
			result = max(result, L_of_j)
		memo[i] = result
		return result

	return helper(arr, len(arr) - 1)

The runtime of this solution:
We will calculate L[i] for every i once and the time to calculate L[i] takes O(i) and so the runtime is O(n + n - 1 + n - 2 + ..... + 1) and this is equal to O(n^2)
The space complexity of this solution is O(n) as the recursive calls stack up to n times and our memo hashmap holds n key and value pairs, thus O(n).
