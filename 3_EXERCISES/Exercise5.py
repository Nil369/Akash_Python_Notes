# Calculate the factorial of a given number & also find the number of trailing zeros

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return((num)*factorial(num-1))
    

def factorialTrailingZeros(number):
	count = 0
	i = 5
	while (number//i !=0):
		count+= int(number/i)
		i = i*5
	return count

     
if __name__ == '__main__':
	number = int(input("Enter a number: \n"))
	fac = factorial(number)
	print(f'The factorial is {fac}')
	# print(factorialTrailingZeroes(number))