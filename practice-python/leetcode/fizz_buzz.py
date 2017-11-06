# Write a program that outputs the string representation of numbers from 1 to n.
# But for multiples of three it should output Fizz 
# instead of the number and for the multiples of 
# five output Buzz. For numbers which are multiples 
# of both three and five output FizzBuzz.
def fizz_buzz(n):
	fizz_buzz_list = []
	for i in range(1, n + 1):
		if i % 3 == 0 and i % 5 == 0:
			fizz_buzz_list.append("FizzBuzz")
			print("FizzBuzz")
		elif i % 5 == 0:
			fizz_buzz_list.append("Buzz")
		elif i % 3 == 0:
			fizz_buzz_list.append("Fizz")
		else:
			fizz_buzz_list.append(str(i))

	print fizz_buzz_list

fizz_buzz(15)
