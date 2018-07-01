/** Akachukwu Obi, 2018

Project Euler #10 - Summation of all primes below 2 million

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below two million.

Retrieved 25 June 2018 from https://projecteuler.net/problem=10

**/

function isFnPrime {
    
}

function find_highest_prime_factor(n) {
    var max, i;
    max = Math.round(Math.sqrt(n));
    for (i = max; i >= 2; i--) {
        if (n % i === 0 && find_highest_prime_factor(i) === 1) {
            return i;
        }
    }
    return 1;
}

var target = 600851475143;
print(find_highest_prime_factor(target));