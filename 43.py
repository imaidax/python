def main():
	num = int(input('Please enter a non negative number: '))
	fact = sum(num)
	print(fact)


def factorial(num):
	if num == 0:
	    return 1
	else:
	    return num * factorial(num - 1)
def range_sum(num_list, start, end):
        if start > end:
            return 0
        else:
            return num_list[start] + range_sum(num_list, start + 1 , end)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
def sum(num):
    #BASE CASE
    if num == 0:
        return 0

    #RECUSIVE CASE
    else:
        return num + sum(num - 1)

main()
