"""List of prime numbers generator."""

def primes(number_of_primes):
    
    if(number_of_primes<1):
        raise ValueError("Value must be more than zero")

    list = []

    i = 0
    number = 2

    while i < number_of_primes:
        for n in range(2, number):
            if(number % n == 0):
                break
        else:   
            list.append(number)
            i += 1                   
        number += 1

    return list