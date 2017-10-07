Question:

Input: a list
Output: a copy of the list where the duplicates are removed

Questions:
1) What is inside this list, integers, strings, etc?
2) Do you want to remove everything that has more than 1 copy or just remove the duplicate.
3) does the order need to be preserved?

Assumptions:
1) This list will contains only integers
2) We will remove everything from the list until we are left with unique items in the list.
3) We want to preserve order of the items in the list base on the first occurrence of each item.

Idea:
We can use a hashset (or set in python) to store the value of items we seen as we iterate through the list. This will give us a hashset of unique items but we won't know the order of the items.
We can again use a hashset and we can initialize a list and as we iterate through the original list we can keep track of whether we seen this element so far, if we have not seen this so far, we will be the element at the end of the list using append().

# this function returns a copy of the arr that has all of the duplicates removed
def deleteDuplicates(arr):
	seenSoFar = set()
	result = list()
	for element in arr:
		if (element not in seenSoFar):
			seenSoFar.add(element)
			result.append(element)
	return result

The runtime of this algorithm is O(n) as we iterate through the list and the space complexity of this solution is also O(n) as we an addition hashset to store the elements we have seen so far, can we do better?
