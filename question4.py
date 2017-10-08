Technical Question: to rearrange letters according to their frequency

Question to the interviewer:
1) What is the input, is it a string or is it a hashmap?
2) What should we output, should we output a hashmap with the character as key an the frequency as the value or should we output a list or should be output a string that the first character has the highest freq. followed by the 2nd highest, etc.

Assumptions:
1) We are giving a book, which consists of lists of strings and we are using English (a, b, c, ...) and we can ignore white spaces, periods, commas etc.
2) We want to put out a list and the list[0] has the greatest freq followed by list[1] ...

Idea:
Preprocess our input and put the counts into a hashmap where the key is the character and the value is the counts we seen so far.
This preprocessing will take O(n) time where n is the total characters in the input and O(1) space as we assume there is a constant number of English characters (26 characters and 26 integers) so it's constant
We can find the highest value and take it out one by one, and this seems like a job for max heap.
What we can do is to make a max heap and have the priority of each character as the count so far. And then pop it out one by one.

Steps:
1) Preprocess input, have hashmap of letters w/ counts
2) Put each of the key from the hashmap into a max heap with priority equal to the count of each letter
3) Pop the max heap and append the result list with the character we got from popping from this max heap until the max heap is empty.

Complexity of this solution:
Time:
Step 1 will take O(n), step 2 will take O(clog(c)) where c is the number of letters in language we are talking about, and step 3 will take O(c) time as we are popping c times. so overall is O(n + clog(c)).
Space:
hashmap will take O(2c) = O(c)
max heap will also take O(c)
result will take O(c)
Overall space complexity is O(c)
Code:
# return a list of characters of decreasing frequency from the input
# input is formatted as a list of strings
# second input is the alphabet we care about
def frequencyList(book, alphabet):

	# return a hashmap of characters with counts from the book
	def preprocess(book, alphabet):
		result = dict()
		for line in book:
			for char in line:
				if (char in alphabet):
					if (char not in result):
						result[char] = 1;
					else:
						result[char] += 1;
	return result;

	# step 1 of our solution
	counts = preprocess(book, alphabet)

	# step 2 put the keys of counts in a pq

	pq = queue.priorityQueue()
	for key in counts:
		# higher the count for key means higher the priority, thus we take the negative
		priority = -counts[key];
		pq.put((priority, key));

	# step 3 get keys from pq and put them into a list
	result = list();
	while (not pq.empty()):
		priority, key = pq.get()
		result.append(key);

	return result;
