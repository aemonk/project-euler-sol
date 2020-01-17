# 5-problem
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def divisible_by(x, y):
    lst = []
    for i in range(x, y+1):
        lst.append(i)
    return lst

def smallest(n, lst):
    ret = [0]
    for num in range(232792559, n+1):
        count = 0
        for i in lst:
            if num % i == 0:
                count += 1
            else:
                continue
        if count == len(lst):
            ret.append(num)
            break
        else:
            continue
    return ret  
        
#print(len(divisible_by(1,20)))
print(smallest(n=232792570, lst=divisible_by(1,20)))