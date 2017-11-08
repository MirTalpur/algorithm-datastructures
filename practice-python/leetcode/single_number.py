# Given an array of integers, every element appears 
# twice except for one. Find that single one.
# Note:
# Your algorithm should have a linear runtime complexity. 
# Could you implement it without using extra memory?

# using extra memory
# keep a frequency hash of the list and keep a count of it
# return the one with the value that is one
def single_number(numbers):
	frequency_hash = {}
	for value in numbers:
		if value in frequency_hash:
			frequency_hash[value] = frequency_hash[value] + 1
		else:
			frequency_hash[value] = 1
	for (key,value) in frequency_hash.iteritems():
		if value is 1:
			return key

# use XOR
def single_number_no_extra_space(numbers):
	result = 0
	for value in numbers:
		result ^= value
	return result

print(single_number_no_extra_space([1, 2, 2, 3, 3]))
print(single_number_no_extra_space([1, 2, 2, 3, 3, 5, 5, 6, 1]))
