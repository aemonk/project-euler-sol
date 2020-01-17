# 4-problem
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def reverse(x):
    return x[::-1]


def palindrome():
    lst = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            ret = i*j
            ret = str(ret)
            index_str = len(ret) / 2
            index_str = int(index_str) 
            front = ret[:index_str]
            back = ret[-index_str:]
            r_back = reverse(back)
            if front == r_back:
                lst.append(int(ret))
    print(max(lst))

palindrome()