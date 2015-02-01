function sum_of_even_fibs(lim)
{
    var res = 0
    var prev = 1
    var n = 1
    var tmp
    while(n <= lim)
    {
        if (n%2 == 0)
        {
            res += n
        }
        tmp = prev
        prev = n
        n = n + tmp
    }
    return res
}

console.log(sum_of_even_fibs(4000000))
