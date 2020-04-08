var res = 0
let limit = 1000 - 1
for n in 1 ... limit {
    if ( n%3==0 || n%5==0 ) {
        // print(n)
        res += n
    }
}
print("Euler 1 Ans: \(res)")