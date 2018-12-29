# 1. Distribution function

## 1 Monotone functions

1. .

2. The floor function $f(x)=[x]$ is such a function. This function cannot be represented as $\sum_{n=1} b_n\delta_n(x)$ because it does not handle the negative domain. A slight modification would be $\sum_{n=1}^\infty b_n\delta_n(x) - \sum_{n=0}^\infty c_n\delta_n(-x)$ with $b_n=c_n=1$.

3. Since the sum of jump sizes ($f(x+)-f(x-)$) is at most $B-A$, if there are more than $(B-A)/\epsilon$ jumps whose the size exceeds $\epsilon$, then there sum is greater than $B-A$, contradicts. Hence the first statement is proved. Now for a monotone bounded $f$, there are a finite number of jumps by what we just proved, hence (iv) is true. To extend this to a general monotone $f$, consider $f_n$, a function that restricts $f$ on $[-n,n]$. $f_n$ is bounded, and has countable jumps. Let $J_n$ the jumps of $f_n$, and $J$ for $f$. Any discontinuous point of $f$ is a member of $J_k$ for some $k$, hence $\cup J_n = J$. Each $J_n$ is countable, so $J$ is countable. Hence (iv) is true for general monotone functions.

4. .

5. .

6. .


## 2. Distribution functions




## 3. Absolutely continuous and singular distributions

