Technical Question: Implement a method to convert a string into a number.

Questions for interviewer:
1) Will this string consists of only characters?
2) Is there a pattern I need to follow?
3) Does the number have to be unique?
4) Do we want to output an integer, a double, a long, or float?
5) Can we also use negative number?
6) Do we get a dictionary on the possible characters in this string?

Assumptions:
1) String will only be numbers.
2) Just convert a string into a number. i.e. "123" -> 123
3) Yes, technically
4) An integer
5) Yes
6) Technically yes, just 0 - 9 and negative sign

One solution will just to use built-in, but let's assume there is no built-in function.
We can start from the end of the string and then work our way digit by digit until we reach the front.

Solution:

def toNum(string):
	result = 0
	power_of_tens = 0
	for char in string.reverse():
		if (char == '-'):
			result = -1 * result
		else:
			num = char.toNum()
			result += num * 10 ** power_of_tens
			power_of_tens += 1
	return result

The runtime of this solution is O(log(n)) where n is the number represented in string, log(n) is the number of digits for a number n.
The space complexity of this solution is O(1) as we do not use additional space in this solution.
