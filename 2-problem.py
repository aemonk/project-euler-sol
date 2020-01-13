# 2-problem
'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
'''
def fib(n):
    i = 0
    lst = []
    while i <= n:
    	if i == 0:
    		lst.append(0)
    	elif i == 1 or i == 2:
    		lst.append(1)
    	elif i > 2:
    		f1 = lst[i - 1]
    		f2 = lst[i - 2]
    		nice = f1 + f2
    		lst.append(nice)
    	i += 1
    return lst[n]


def iterate(N):
	lst = []
	for i in range(N):
		lst.append(fib(i))
	return lst

def even_valued(lst):
	sum = 0
	ret = []
	for i in lst:
		if i <= 4000000 and i % 2 == 0 and i > 0:
			ret.append(i)
			sum += i
	return sum

if __name__ == '__main__':
	print(fib(10))
	print(iterate(50))
	print(even_valued(iterate(50)))