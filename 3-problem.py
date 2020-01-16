# 3-problem
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
def largest_prime(n=600851475143):
    divisor = 2
    highest_divisor = 0
    while divisor != n+1:
        if n % divisor == 0:
            n = n/divisor
            highest_divisor = divisor
            divisor = 2
        elif n % divisor != 0:
            divisor += 1

    return highest_divisor
            

print(largest_prime())