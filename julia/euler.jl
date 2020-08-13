# Functions for Solving Project Euler Problems

function is_divisible(dividend, divisor)
    # returns true if dividend is divisible by divisor
    # if remainder == 0 then divisible
    return dividend % divisor == 0
end

function is_prime(n::T) where {T<:Union{Int, BigInt}}
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


function derivative(f)
    # returns a function that computes the numerical derivative of f
    # Source: Forio Julia Tutorial
    # Reference: http://en.wikipedia.org/wiki/Numerical_differentiation#Practical_considerations_using_floating_point_arithmetic
    return function(x)
        # pick small value for h
        h = x == 0 ? sqrt(eps(Float64)) : sqrt(eps(Float64))*x

        # floating point arithmetic gymnastics
        xph = x + h
        dx  = xph - x

        # evaluate f at  x + h
        f1 = f(xph)
        # evaluate f at x
        f0 = f(x)

        # divide the difference by h
        return (f1 - f0) / dx
    end
end
