# 1. Distribution function

## 1 Monotone functions

1. .

2. The floor function $f(x)=[x]$ is such a function. This function cannot be represented as $\sum_{n=1} b_n\delta_n(x)$ because it does not handle the negative domain. A slight modification would be $\sum_{n=1}^\infty b_n\delta_n(x) - \sum_{n=0}^\infty c_n\delta_n(-x)$ with $b_n=c_n=1$.

3. Since the sum of jump sizes ($f(x+)-f(x-)$) is at most $B-A$, if there are more than $(B-A)/\epsilon$ jumps whose the size exceeds $\epsilon$, then there sum is greater than $B-A$, contradicts. Hence the first statement is proved. Now for a monotone bounded $f$, there are a finite number of jumps by what we just proved, hence (iv) is true. To extend this to a general monotone $f$, consider $f_n$, a function that restricts $f$ on $[-n,n]$. $f_n$ is bounded, and has countable jumps. Let $J_n$ the jumps of $f_n$, and $J$ for $f$. Any discontinuous point of $f$ is a member of $J_k$ for some $k$, hence $\cup J_n = J$. Each $J_n$ is countable, so $J$ is countable. Hence (iv) is true for general monotone functions.

4. .

5. Note: $D$ is dense in $(-\infty,\infty)$. Otherwise define $f(x)=0$ on $[-1,1]$. $f$ is continuous, $\tilde f(x)=\infty$ for $x\ge 1$ and $\tilde f(x)=0$ for $x<1$. $f$ is continuous and uniformly continuous but $\tilde f$ is discontinuous at $x=1$.  
For continuity: let $f$ be the floor function, then $f$ is continuous on $\R\setminus\Z$, and $\tilde f$ is discontinuous at the points of $\Z$.  
For uniformly continuity: suppose $f$ is uniformly continuous on D. For any $\epsilon>0$, there exists $\delta>0$ s.t. $|f(t_0)-f(t_1)|<\epsilon/2$ for all $t_0, t_1\in D$ satisfying $|t_0-t_1|<\delta$. For $x_0, x_1 \in \R$, $x_0<x_1, x_1-x_0<\delta$, there exists $t_0 \in D$ s.t. $t_0>x_0, f(t_0)-\epsilon/2\le\tilde f(x_0)\le\tilde f(x_1)\le f(t_0+\delta)$. The last inequality comes from $x_1< x_0+\delta\le t_0+\delta$. Since the length of interval $[f(t_0)-\epsilon/2, f(t_0+\delta)]$ is less than $\epsilon$, $|\tilde f(x_0)-\tilde f(x_1)|<\epsilon$. $\therefore$ $\tilde f$ is uniformly continuous.

6. .


## 2. Distribution functions

1. $\lim F(x+\epsilon) = F(x+) = F(x)$ and $\lim F(x-\epsilon) = F(x-) = F(x)$, therefore $\lim F(x+\epsilon)-F(x-\epsilon) = F(x+)-F(x-)$. If $x$ is not a point of jump, $F(x+)-F(x-)=0$. If $x$ is a point of jump, $F(x+)-F(x-)$ is the size of the jump.

2. If $x$ is a point of jump, the given sum is at most $F(x-)-F(x-\epsilon)$, which converges to 0. If $x$ is not a point of jump, the given sum is at most $F(x)-F(x-\epsilon)$, which converges to 0 because $F(x)=F(x-)$.

3. .

4. .

5. .

6. If $x$ is a point of jump, for any $\epsilon>0$, $F(x-\epsilon)\le F(x-)<F(x+)\le F(x+\epsilon)$, hence $x$ belongs to the support. Let $S$ the support. If $x$ is an isolated point of $x$, there exists $\epsilon$ s.t. $(x-\epsilon, x+\epsilon)\setminus\{x\} \sub S^C$. This means that $F$ is constant on two intervals $(x-\epsilon, x)$ and $(x, x+\epsilon)$, and the values of two intervals are different. The value for the first interval is $f(x-)$ and one for the latter is $f(x+)$, hence $f(x-)\ne f(x+)$. Therefore $x$ is a point of jump.

7. Note: the definition of *support* in this problem is from Prob 6. Other definitions inherently implies the closedness.  
Let $S$ the support of a d.f. $f$. For $x\in S^C$, there exists $\epsilon$ s.t. $F(x+\epsilon)-F(x-\epsilon)=0$. Since $F$ is monotone, $F$ is constant on a range $(x-\epsilon, x+\epsilon)$, and this range is a subset of $S^C$. Hence $x$ is an interior point of $S^C$ and $S^C$ is open, $S$ is closed.  
By Prob 6, any isolated point of $S$ is a point of jump, hence if $f$ is continuous d.f., $S$ has no point of jump and no isolated point. Therefore $S$ is perfect.




## 3. Absolutely continuous and singular distributions

### Part 1

1. If $F$ is singular, then $F'(x)=0$ a.e. and $F_{ac}=0$, hence $F=F_s$. If $F=F_s$, then $F_{ac}=F-F_s=0$, and $F_{ac}'=0=F'$ a.e., $F$ is not zero because $F(+\infty)=1$, hence $F$ is singular. If $F$ is absolutely continuous, then $F(x)=\int_{-\infty}^x F'(t)dt=F_{ac}(x)$, hence $F=F_ac$. If $F=F_ac$, then $F(x')-F(x)=F_{ac}(x')=F_{ac}(x)=\int_x^{x'} f(t)dt$, so by definition $F$ is absolutely continuous.

2. .

3. $F(x+\epsilon)-F(x-\epsilon)=0$ for all $\epsilon>0$ a.e $x$. This means $F'(x)=0$ a.e. Hence $F_{ac}(x)=0$ for all $x$. $F=F_s$ and from Prob 1, $F$ is singular. Conversely if $F$ is singular, $F_{ac}=0$. However $F$ does not need to be zero a.e. An example is $F=F_s=F_d$ where $F_d$ is any discrete d.f.

4. Since $f\le 0$ a.e and $f$ is continuous, $f\le 0$ everywhere. By the first fundamental theorem of calculus, $F'(x)=f(x)$ everywhere.

5. Let $S$ the support of $F$ and $S_0=\{t|f(t)=0\}$. We show the second statement and derive the first from it. If $x\in S^C$, $f(x+\epsilon)-f(x-\epsilon)=0$ for some $\epsilon$. $F$ is constant on $(x-\epsilon, x+\epsilon)$, $f$ is zero on $(x-\epsilon, x+\epsilon)$, $x$ is an interior point of $S_0$. Conversely, if $x$ is an interior point of $S_0$, $f$ is zero on $(x-\epsilon, x+\epsilon)$ for some $\epsilon$, and $F$ is constant on this interval, hence $x\in S^C$. Therefore $S^C$ is equal to the interior of $S_0$ and the second statement is proved. Since $S^C$ is the interior of $S_0$, $S$ is automatically the closure of $S_0^C$, which proves the first statement.


6. .

7. .


### Part 2

8. A point $x$ in $C$ is an end-point of one of removed intervals, hence the left points of $x$ and right points of $x$ belong to different intervals. Since the belonged interval determines the value of $F$, $F(x-)\ne F(x+)$ and $x$ is in the support of $F$. Note that the value of $f(x)$ does not matter. A point $x$ not in $C$ belongs to an open interval $J_{n,k}$, thus it has a neighborhood that has a constant value of $F$. Hence $F(x-)=F(x+)$ and $x$ is not in the support of $F$.

9. .

10. .

11. .

    (a) Let A=$\int_0^1 x dF(x), B=\int_0^{1/3} x dF(x), C=\int_{2/3}^1 x dF(x)$. $\int_{1/3}^{2/3} x dF(x) = 0$ because $F(x)$ is constant on this interval. For $B$, we have $A = \int_0^1 x dF(x) = 2\int_0^1 x dF(x/3) = 6\int_0^1 x/3 dF(x/3) = 6B$. For $C$, we have $A = \int_0^1 x dF(x) = 2\int_0^1 x dF(2/3+x/3) = 6\int_0^1 x/3 dF(2/3+x/3) = 6(\int_0^1 (2/3+x/3) dF(2/3+x/3)-2/3)=6C-4$. Now putting these into $A=B+C$, $A=A/6+(A/6+2/3)$, we get $A=1/2$.

    (b) Same as in (a). Let D=$\int_0^1 x^2 dF(x), E=\int_0^{1/3} x^2 dF(x), F=\int_{2/3}^1 x^2 dF(x)$. $\int_{1/3}^{2/3} x^2 dF(x) = 0$ because $F(x)$ is constant on this interval. For $E$, we have $D = \int_0^1 x^2 dF(x) = 2\int_0^1 x^2 dF(x/3) = 18\int_0^1 (x/3)^2 dF(x/3) = 18E$. For $F$, we have $D = \int_0^1 x^2 dF(x) = 2\int_0^1 x^2 dF(2/3+x/3) = 6\int_0^1 (3(2/3+x/3)^2-(2/3+2/3x)) dF(2/3+x/3) = 18F - 6C$. Now putting these into $D=D/18+D/18+C/3$, $D=3/8 * C= 3/8 * 3/4 = 9/32$, we get $D=9/32$.

    (c) ..

12. .

13. [incomplete] Define a new $F_0^{-1}(x)$ as $\inf F^{-1}(x)$. Then $F_0^{-1}$ is single-valued

14. .

15. .

