function solve(lim)
{
    var res = 1
    var n = 1
    while(n <= lim)
    {
        if(res%n != 0)
        {
            res *= n / gcd(res, n)
        }
        n += 1
    }
    return res
}

function gcd(a, b)
{
    if(b == 0)
    {
        return a
    }
    else if(a < b)
    {
        return gcd(b, a)
    }
    else
    {
        return gcd(b, a%b)
    }
}

console.log(solve(20))
