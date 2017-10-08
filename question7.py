You are given a positive integer number and you have to return the greatest smaller tidy number of this input number. If the input number itself is tidy, then, it become the answer
Example
Input: 1234
output: 1234
input: 100
output: 99
input 143456
output: 139999.
PS.A tidy number is a number whose digits are in non-decreasing order.

Question for the interviewer:
1) Will the input be an integer or will it be a string, same goes for output
2) If a string, do I need padding, i.e. "099" instead of "99"
3) Will input be a negative number?

Assumptions:
1) The input will be an integer and the output should also be an integer.
2) It is an integer so there is no need for padding
3) There will not be a negative number, and assume valid input.

Idea:
Brute force -- build from bottom up, find the smallest tidy number and the next one, and the next one until we find the one that is bigger than our input and return the previous one. This will take a lot of computation
Brute force 2 -- top down approach, we decrement input one by one until we find a tidy number, this also can take a long time.

Observation:
Input: 381
Output: 379
When we have an inversion, the lower digit go all the way up to 9 and the higher digit decrement by 1
Input: 101
Output: 99
Input: 91
Output 89
We can solve this by using recursion: when we see the first inversion (i.e. smaller digit, we make the rest of the smaller digit become 9)
Input: 1082
Output: 999
Input: 2082
Output: 1999
Input: 12073
Output: 11999
Input: 1100
Output: 999

When we find inversion, we decrement the bigger digit by 1
High Level:

let i be the i'th digit of the input

1) We recursively call 0... i - 1 digits when computing i digit
2) Our return value for computing 0 ... i - 1 will be 2 things
	1) it will return what 0 ... i - 1 should be (biggest tidy number)
	2) whether i should decrement by 1
	3) The input for this helper function will be: 0 .... i - 1 and a lower bound, which is i

Code:

# Input: integer
# Output: integer, the highest tidy num
def findHighestTidyNum(num):

	# This is the helper function that takes in two inputs
	# And outputs the tidy number and a boolean of whether we should
	# decrement the digit before
	def helper(num, lower_bound):
if (num < 10):
	if (num >= lower_bound):
		return num, False
	else:
		return 9, True
highest_digit = highestDigit(num)
if (highest_digit < lower_bound):
	return allNines(num), True
rest = restDigits(num)
tidy_rest, should_dec = helper(rest, highest_digit)
if (should_dec):
	highest_digit -= 1;
if (highest_digit < lower_bound):
	return allNines(num), True
return reconstruct(highest_digit, tidy_rest), False


	highest_tidy_number, _ = findHighestTidyNum(num, 0)
	return highest_tidy_number
