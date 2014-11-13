# Functions for Solving Project Euler Problems

function is_divisible(dividend, divisor)
    # returns true if dividend is divisible by divisor
    # if remainder == 0 then divisible
    return dividend % divisor == 0
end

function is_prime(n::Int64)
    # Prime Number: natural number > 1 whose only divisors are 1 & itself
    # check to see if n is divisible by any number <= sqrt(n)

    if n == 2 || n == 3
        return true
    end

    # even numbers are not prime
    if is_divisible(n, 2)
        return false
    end
    
    # Check to see whether it is divisible by any other odd number
    # initialize a counter variable
    i = 3
    while i <= sqrt(n)
        if is_divisible(n, i)
            return false
        end
        i += 2
    end

    return true
end
