function no_of_sum(n)
    """ return the number of ways of
    creating a sum of n using atleast two
    positive integers
    """
    r = 0
    for i in 1:n-1
        r += no_of_sums(n-i, i)
    end
    return r
end

function no_of_sums(n, i)
    """ returns the number of ways
    of creating a sum of n using
    one or more positive integers <= i
    """
    if i > n
        return no_of_sums(n, n)
    end
    if i == 1 || n == 0
        # there is only 1 way of creating a sum of
        # 0 or using only 1's
        return 1
    elseif n >= i
        # (n, i) = no of ways of (n-i, i) plus no of ways of (n, i-1)
        return no_of_sums(n-i, i) + no_of_sums(n, i-1)
    end
end

n = 5
println("No of sums of $n: $(no_of_sum(n))")
n = 100
println("No of sums of $n: $(no_of_sum(n))")
