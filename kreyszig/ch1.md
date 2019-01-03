# 1. Metric Spaces

## 1.1. Metric Space

1. $d(x,y)=|x-y|$ for $x,y\in \R$
    (M1) trivial
    (M2) $|x-y|=0 \iff x=y$
    (M3) $|x-y|=|y-x|$
    (M4) $|x-y|\le|x-z|+|z-y|$

2. $d(x,y)=(x-y)^2$, (M1)~(M3) are trivial. (M4) is false for $x=0, y=2, z=1, (x-y)^2\nleq (x-z)^2+(z-y)^2$.

3. $d(x,y)=\sqrt{|x-y|}$, (M1)~(M3) are trivial. For (M4), $\sqrt{|x-y|}\le\sqrt{|x-z|}+\sqrt{|z-y|} \iff |x-y| \le |x-z|+|z-y|+2\sqrt{...}$, which is true from $|x-y|\le |x-z|+|z-y|$.

4. For two points, $X=\{a,b\}, d(a,a)=d(b,b)=0, d(a,b)=d(b,a)=c>0$. For one point, $X={a}, d(a,a)=0$.

5. $(X,d)$
    (i) if $|X|>1$, $k>0$. If $|X|=1$, $k\ge 0$. If $|X|=0$, $k$ is any real number. $k\in \R$ in all cases.

    (ii) $(d+k)(a,a)=0=d(a,a)+k$. If $|X|\ge 1, k=0$. Otherwise $k$ is any real number.

6. $d(x,y)=\sup_{j\in \N}|x_j-y_j|$
    We have $\forall j\in\N, |x_j-y_j|\le|x_j-z_j|+|z_j-y_j|$.

7. $d(x,y)=1$ if $x\ne y$, 0 if $x=y$.

8. $\tilde d(x,y)=\int_a^b |x(t)-y(t)|dt$
    (M1) $\forall f\in X$, $f$ is bounded because its domain is a closed interval. Hence $\tilde d$ is real, finite, and non-negative.
    (M2) $\tilde d(x,y)=0 \iff $\forall t\in[a,b], x(t)=y(t)$ \iff x=y$
    (M3) obvious
    (M4) $\int_a^b |x(t)-y(t)|dt\le \int_a^b |x(t)-z(t)|+|z(t)-y(t)|dt = \int_a^b |x(t)-z(t)|+\int_a^b |z(t)-y(t)|dt$

9. (M1)~(M3) are obvious.
    (M4) $d(x,y)\le d(x,z)+d(z,y)$
    since each term is $0$ or $1$, the only case (M4) is false is $d(x,y)=1, d(x,z)=d(z,y)=0$. This means $x\ne y, x=z, z=y$, which is impossible. Hence (M4) is true. $d$ is a metric.

10. $X=\{(0,0,0),...(1,1,1)\}, |X|=2^3=8$. $d(x,y)=\sum |x_i-y_i|$.
    (M1)~(M3) are obvious.
    For (M4), $\sum |x_i-y_i|\le\sum(|x_i-z_i|+|z_i-y_i|)=\sum|x_i-z_i|+\sum|z_i-y_i|$

11. $$\begin{aligned}
    d(x_1,x_n)\le &d(x_1,x_2)+d(x_2,x_n)\\
    &d(x_1,x_2)+d(x_2,x_3)+d(x_3,x_n)\\
    &\dots\\
    &d(x_1,x_2)+d(x_2,x_3)+\dots+d(x_{n-1},x_n)
    \end{aligned}$$

12. $|d(x,y)-d(z,w)|\le d(x,z)+d(y,w)$?
    WLOG, $d(x,y)\ge d(z,w)$, then the question becomes
    $d(x,y)\le d(x,z)+d(z,w)+d(w,y)$, which is true by triangle inequality.

13. It is enough to consider $d(x,z)-d(y,z)\ge0$. Then the inequality is $d(x,z)\le d(x,y)+d(y,z)$, which is the triangle inequality.

14. $d(x,y)\le d(z,x)+d(z,y)$ and $d(x,y)=0 \iff x=y$.
    (M3) With $z=y$, we have $d(x,y)\le d(y,x)$. Swapping $x$ and $y$, we have $d(y,x)\le d(x,y)$. Hence $d(x,y)=d(y,x)$.
    (M4) $d(x,y)\le d(z,x)+d(z,y)=d(x,z)+d(z,y)$.

15. Putting $x=y$ into $d(x,y)\le d(x,z)+d(z,y)$, we have $0\le d(x,z)$ for all $x, z$.

## 1.2. Further Examples of Metric Spaces

1. $d(x,y)=\sum_{j=1}^\infty \mu_j \frac{|x_j-y_j|}{1+|x_j-y_j|}, \sum\mu_j<\infty, \mu_j>0$
    (M1) $d(x,y)<\sum \mu_j <\infty$.
    (M2, M3) obvious
    (M4) The same proof from 1.2-1 applies here too. ($f(t)=\frac{t}{1+t}, \cdots$)

2. With $\alpha=\sqrt a, \beta=\sqrt b, p=2, q=2$, we have $\alpha\beta\le \frac{\alpha^p}{p}+\frac{\beta^q}{q}\Longrightarrow \sqrt{ab}\le\frac{a+b}{2}$.

3. Setting $b_i=1$, (11) becomes $(\sum|a_i|)^2\le\sum|a_i|^2$.

4. Let $x_n=1/\log n$. Then $\lim_{n\to\infty} x_n=0$. Given $p$, there exists $m$ such that $\forall n\ge m, \log^pn<n$. Thus

    $$\begin{aligned}
    \sum|x_n|^p
    =\sum_{n=1}^\infty \frac{1}{\log^p n}
    &> \sum_{n=m}^\infty \frac{1}{\log^p n}\\
    &> \sum_{n=m}^\infty \frac{1}{n}=\infty
    \end{aligned}$$

    $\therefore x\notin l^p$.

5. $x_n=1/n$, then $\sum 1/n=\infty\Longrightarrow x\notin l^1, \sum1/n^p<\infty\Longrightarrow x\in l^2$. These can be easily shown by integrals and lower, upper bounds.

6. If $\delta(A)=\infty$, for any $\delta_0>0, \exists x,y\in A, d(x,y)>\delta_0$, this means $\delta(B)\ge\delta_0$, hence $\delta(B)=\infty$. Now assume $\delta(A)<\infty$. Also assume $A\sub B, \delta(A)>\delta(B)$. For any $\epsilon>0$, there must be $x,y\in A$ such that $d(x,y)>\delta(A)-\epsilon$. Since $x,y\in B$, $\delta(B)\ge d(x,y)>\delta(A)-\epsilon$. Hence $\delta(B)\ge \delta(A)$.

7. $\delta(A)=0\Longrightarrow d(x,y)\le 0\Longrightarrow x=y\Longrightarrow |A|\le 1$. If $|A|=0, \delta(A)=-\infty$, hence $|A|=1$. Conversely, $|A|=1\Longrightarrow \delta(A)=0$.

8. For distinct $x,y\in X$, $D(\{x\},\{x,y\})=0$ but $\{x\}\ne\{x,y\}, \therefore$ D is not a metric. $D$ can be a metric if $A=\varnothing$ or $B=\varnothing$.

9. $A\cap B\ne \varnothing\Longrightarrow\exists x\in A\cap B\Longrightarrow D(A,B)=D(\{x,\dots\},\{x,\dots\})=0$. The converse is not true. Let $A=[0,3], B=(3,6]$, then $D(A,B)=0$ but $A\cap B=\varnothing$.

10. It is enough to prove $D(x,B)-D(y,B)\le d(x,y)$. For $\forall b\in B$,

    $$\begin{aligned}&D(x,B)\le d(x,b)\le d(x,y)+d(y,b)\\
    \Longrightarrow &D(x,B)-d(x,y)\le d(y,b) \\
    \Longrightarrow &D(x,B)-d(x,y) \text{ is a lower bound of d(y,b)} \\
    \Longrightarrow &D(x,B)-d(x,y)\le D(y,B) \\
    \Longrightarrow &D(x,B)-D(y,B)\le d(x,y)
    \end{aligned}$$

11. (M1)~(M3) are obvious.
    (M4) Let $f(t)=t/(1+t)$. It is shown in 1.2-1 that $f$ is increasing.
    From $d(x,y)\le d(x,z)+d(z,y)$,

    $$\begin{aligned}
    f(d(x,y))&\le f(d(x,z)+d(z,y)) \\
    \frac{d(x,y)}{1+d(x,y)}&\le \frac{d(x,z)+d(z,y)}{1+d(x,z)+d(z,y)}\\
    &=\frac{d(x,z)}{1+d(x,z)+d(z,y)}+\frac{d(z,y)}{1+d(x,z)+d(z,y)}\\
    &\le\frac{d(x,z)}{1+d(x,z)}+\frac{d(z,y)}{1+d(z,y)}
    \end{aligned}$$

    Also $0\le f(t)\le 1$, so $X$ is bounded.

12. Let $a_0\in A, b_0\in B$. For any $a\in A, b\in B$,

    $$\begin{aligned}
    d(a,b)&\le d(a,a_0)+d(a_0,b_0)+d(b_0,b)\\
    &\le\delta(A)+d(a_0,b_0)+\delta(B)\\
    &<\infty
    \end{aligned}$$

    $\therefore A\cup B$ is bounded.

13. (M1)~(M3) are obvious.
    (M4)

    $$\begin{aligned}
    d(x,y)&=d_1(x_1,y_1)+d_2(x_2,y_2)\\
    &\le d_1(x_1,z_1)+d_1(z_1,y_1)+d_2(x_2,z_2)+d_2(z_2,y_2)\\
    &=d(x,z)+d(z,y)
    \end{aligned}$$


14. (M1)~(M3) are clear.
    (M4) $\tilde d(x,y)\le \tilde d(x,z)+\tilde d(z,y)$ can be written as $|a+bi|\le|c+di|+|e+fi|$ with $a\le c+e, b\le d+f$.

    $$\begin{aligned}
    |a+bi|\le|(c+e)+(d+f)i|&=|c+di+e+fi|\\
    &\le|c+di|+|e+fi|
    \end{aligned}$$

    the last inequality holds because $\mathbb C$ is a metric space.


15. $$\begin{aligned}\tilde{\tilde d}(x,y)&=max(d_1(x_1,y_1),d_2(x_2,y_2))\\
    &=max(xy1, xy2)\\
    &=max(xz1+zy1,xz2+zy2)=\triangle
    \end{aligned}$$

    ($xy1$ represents $d_1(x_1,y_1)$ for convenience)

    We want to prove $\triangle\le max(xz1, xz2)+max(zy1,zy2)$. This is equivalent to show $\max(a+b,c+d)\le \max(a,c)+\max(b,d)$.

    $$\begin{aligned}
    \max(a+b,c+d)&\le\max(\max(a,c)+b,\max(a,c)+d)\\
    &\le\max(\max(a,c)+\max(b,d),\cdots)\\
    &\le\max(a,c)+\max(b,d)
    \end{aligned}$$

## 1.3. Open Set, Closed Set, Neighborhood
## 1.4. Convergence, Cauchy Sequence, Completeness
## 1.5. Examples, Completeness Proofs
## 1.6. Completion of Metric Spaces
