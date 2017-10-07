Question: Write a method to return all permutations of a string.

Input: A string
Output: A list of permutations (strings), hashmap of strings, arraylist

Questions:
1) Will the strings composes of English characters, is there numbers, other language characters
2) Does order matters?

Assumptions:
1) The string is only English characters and that characters are not unique
2) Order doesn't matter as long as every permutation is there
3) No duplicates

Samples:
Input: "abc"
output: ["abc", "acb", "bac", "bca", "cab", "cba"]

Input: "aab"
output: ["aab", "aba", "baa"]

Input: ""
Output: [""] or None or exception

Input: "aba"
Ouput: ["aab", "aba", "baa"] order may be different

Main Idea:
Like what we do when we construct the output for sample input 1, we iterate through the input string and place each character in front and we build the permutation with the rest of the string.

Code: (in python)
# return a list of permutations of the input string
def permutations(string):
	if (len(string) == 0):
		return [""];
	elif (len(string) == 1):
		return [string];
	letters_seen_so_far = set();

	result = list();
	for i in range(0, len(string)):
	head = string[i]
	if (head not in letters_seen_so_far):
		rest_permutations = permutations(string[0:i] + string[i+1:])
	for rest_permutation in rest_permutations:
		result.append(head + rest_permutation)

return result;
