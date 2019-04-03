# 3장. 여러 가지 확률분포
3.2
Consider $n$ numbered balls. Each ball is colored with prob. $p$.

- Event X represents a specific coloring.
- r.v. Y represents a number of permutations of $r$ colored balls.

Then $E[Y|C]=X(X-1)..(X-r+1)$. Hence $E[X(X-1)..(X-r+1)]=E_C[E[Y|C]]=E[Y]=n(n-1)...(n-r+1)p^r$.

3.4
;

3.6
$f(x)\ge f(x-1)$ gives $x\le (r-1)/p+1$.
For $x$ to be the maximum, $f(x+1)\le f(x)\Longrightarrow x+1\ge (r-1)/p+1$.
From $\frac{r-1}{p}\le x \le \frac{r-1}{p}+1$, we have $x=\operatorname{floor}((r-1)/p)+1$.

3.8
$Cov(W_1,W_r)=Cov(W_1,W_r-W_{r-1})+Cov(W_1,W_{r-1})=Cov(W_1,W_{r-1})=\cdots=Cov(W_1,W_1)=Var(W_1)=(1-p)/p^2$


3.10
;

3.12
;

3.14
;

3.16
mgf = $\sum_{k=0}^\infty \frac{E(X^k)}{k!}t^k=\sum \frac{t^{2k}}{2^k k!}$
pdf =

3.18
;q b