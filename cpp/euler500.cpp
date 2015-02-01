#include <iostream>
#include <set>
#include <vector>
#include <cmath>
#include <cstring>

using namespace std;

typedef pair<long long, long long> pii;
set<pii> pq;

// limit <= 10^8
vector<int> prime_numbers (int limit) {
    const int SQRT_MAXN = 10000;
    const int S = 1000;

    vector<int> primes;
    vector<int> res_primes;
    bool nprime[SQRT_MAXN], bl[S];
    int cnt = 0;

    memset(nprime, 0, sizeof nprime);
    memset(bl, 0, sizeof bl);

    int nsqrt = (int) sqrt (limit + .0);
    for (int i=2; i<=nsqrt; ++i)
        if (!nprime[i]) {
            primes.push_back(i);
            if (i * 1ll * i <= nsqrt)
                for (int j=i*i; j<=nsqrt; j+=i)
                    nprime[j] = true;
        }

    cnt = (int) primes.size();

    int result = 0;
    for (int k=0, maxk=limit/S; k<=maxk; ++k) {
        memset (bl, 0, sizeof bl);
        int start = k * S;
        for (int i=0; i<cnt; ++i) {
            int start_idx = (start + primes[i] - 1) / primes[i];
            int j = max(start_idx,2) * primes[i] - start;
            for (; j<S; j+=primes[i])
                bl[j] = true;
        }
        if (k == 0)
            bl[0] = bl[1] = true;
        for (int i=0; i<S && start+i<=limit; ++i)
            if (!bl[i])
                res_primes.push_back(start+i);
    }

    return res_primes;
}

int main () {
    vector<int> p = prime_numbers(10000000);

    for (int i = 0; i < (int)p.size(); i++)
        pq.insert(make_pair(p[i] * 1LL, p[i] * 1LL));

    long long num = 1;
    const long long MOD = 500500507LL;
    // for every exponent in 2^500500
    for (int two_exp = 1; two_exp <= 500500; two_exp++) {
        // take top of the heap
        pii top = *pq.begin();
        pq.erase(pq.begin());

        // multiply the result
        long long prime_exp = top.first;
        num = (num * prime_exp) % MOD;

        // put the new candidate back to the queue
        long long new_base = top.second;
        long long new_prime_exp = prime_exp * prime_exp;
        pq.insert(pii(new_prime_exp, new_base));
    }

    cout << num << endl;

    return 0;
}
