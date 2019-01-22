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


15. $$\begin{aligned}\tilde{\tilde{\kern{-0.3ex}d}}(x,y)&=\max(d_1(x_1,y_1),d_2(x_2,y_2))\\
    &=\max(xy1, xy2)\\
    &=\max(xz1+zy1,xz2+zy2)=\triangle
    \end{aligned}$$

    ($xy1$ represents $d_1(x_1,y_1)$ for convenience)

    We want to prove $\triangle\le \max(xz1, xz2)+\max(zy1,zy2)$. This is equivalent to show $\max(a+b,c+d)\le \max(a,c)+\max(b,d)$.

    $$\begin{aligned}
    \max(a+b,c+d)&\le\max(\max(a,c)+b,\max(a,c)+d)\\
    &\le\max(\max(a,c)+\max(b,d),\cdots)\\
    &\le\max(a,c)+\max(b,d)
    \end{aligned}$$

## 1.3. Open Set, Closed Set, Neighborhood
1. (a) For any $x\in B(x_0,r)$, define $B'=\{y|d(x,y)<r-d(x,x_0)>\}$. Since $d(x_0,y)\le d(x,y)+d(x,x_0)<r$, $B'\sub B$. $\therefore B$ is an open set.
    (b) Let a closed ball $\tilde B(x_0,r)$. Then $\tilde B^c = {p|d(p,x_0)>r}. For any point $x\in\tilde B^c$, let $B_x=B(x, d(x,x_0)-r)$. A point $y\in B_x$ is not in $B$ because $r<d(x,x_0)-d(x,y)\le d(x,y)+d(y,x_0)-d(x,y)=d(x_0,y)$. $\therefore B_x \in \tilde B^c$, so $x$ is an internal point of $\tilde B^c$, hence $B^c$ is open, and $B$ is closed.

2. An open ball in $\R$ is an open interval. An open ball in $\mathbb C$ is a filled circle without boundary in the complex plane. An open ball $B(x_0,r) $in $C[a,b]$ is a set of functions $x$ whose the value at $t\in[a,b]$ satisfies $|x(t)-x_0(t)|\le r$. In other words, $x_0(t)-r\le x(t)\le x_0(t)+r$.

3. We need to find the smallest $r$ such that $\forall t |\cos t-\sin t|\le r$. Equivalently, find the maximum $\cos t + \sin t$ where $t\in [0,\pi/4]$, or, $\max f(x)$ where $f(x)=x+\sqrt{1-x^2}, x\in[0,1]$. $f'(x)=1+\frac{-2x}{2\sqrt{1-x^2}}=0\Longrightarrow x=\frac{1}{\sqrt 2}$. Therefore $t$ is $0\degree, 45\degree, 90\degree$. Trying these values, we have $\max(\cos t + \sin t)=\sqrt 2$.

4. If a non-empty set $A$ is open, each point $a\in A$ has a ball $B_a\sub A$. Let $B=\cup_a B_a$, then $B\sub A$. Also $A\sub B$ because every $a\in A$, $a\in B_a\sub B$. Hence $A=B$, and $A$ is an union of open balls. Conversely if $A$ is an union of open balls, it is open (by what we learned).

5. (a) $\varnothing$ is open because it has no member and we can say all members are internal points. $X$ is open because any neighborhood is in $X$. $\varnothing, X$ are closed because their complements are open.
    (b) For a subset $Y\sub X$, $Y$ is open because for $y\in Y, B(y,0.5)=\{y\}\sub Y$. Since every subset is open, $Y^c$ is open, hence $Y$ is closed.

6. Suppose a neighborhood $N$ of $x_0$ contains finitely many points of $A$. Let $d_0=\min_{a\in N\cap A} d(x_0, a)$. Then it contradicts that $B(x_0, d_0/2)$ should contain at least one point of $A$.

7. (a) $\N=\overline \N$ on $\R$
    (b) $\overline\mathbb Q=\R$ on $\R$
    (c) $\overline{\mathbb Q \times \mathbb Q}=\R\times\R$
    (d) $\overline{\{z\mid \lvert z\rvert<1\}}=\{z\mid\lvert z\rvert \le 1\}$ on $C$

8. Let $X=\{0,1\}$. Then $B(0;1)=\{0\}, \overline{B(0;1)}=\{0\}$, but $\tilde B(0;1)=\{0,1\}$.

9. - $A\sub \overline A = A\cup\{\text{accumulation points}\}$
    - $\overline A=\overline{\overline A}$: We have $\overline A\sub \overline {\overline A}$. For the converse, suppose the contrary, so $\exists a\in \overline{\overline A}, a\notin \overline A$. Since $a$ is not an accumulation point of $A$, but of $\overline A$,
    $\exists \epsilon_0>0, B(a,\epsilon_0)\cap A-\{a\}=\varnothing$
    $\forall \epsilon>0, B(a,\epsilon)\cap \overline A - \{a\}\neq \varnothing$
    Let $a'\in B(a,\epsilon_0/2)\cap \overline A-\{a\}$, then $a'\in \overline A-A$ so $a'$ is an accumulation point of $A$.
    $\forall \epsilon>0, B(a', \epsilon)\cap A-\{a'\}\neq \varnothing$
    with $\epsilon=\epsilon_0/2$,
    $\exists a''\in B(a', \epsilon_0/2)\cap A-\{a'\}$
    $d(a'',a')<\epsilon_0/2, d(a',a)<\epsilon_0/2, d(a'',a)<\epsilon_0/2$
    Also $a''\neq a$ because $a''\in A, a\in \overline A$. This contradicts to $a'' \in B(a,\epsilon_0)\cap A-\{a\}$. Therefore such $a$ does not exist, and $\overline{\overline A}=A$.

    - $\overline{A\cup B}=\overline A\cup \overline B$: suppose $x\in \overline{A\cup B}, x\notin \overline A, x\notin \overline B$. Then $\exists \epsilon>0$, $B(x,\epsilon)\cap A\sub\{x\}$, $B(x,\epsilon)\cap B\sub \{x\}$, but $B(x,\epsilon)\cap(A\cup B)\not\subset \{x\}$, which contradicts. Hence $\overline{A\cup B}\sub (\overline A\cup \overline B)$. Now suppose $x\in \overline A$ but $x\notin \overline{A\cup B}$. $\forall \epsilon>0, B(x,\epsilon)\cap A-\{x\}\neq\varnothing, B(x,\epsilon)\cap(A\cup B)-\{x\}\neq \varnothing$, $x$ is an accumulation point of $(A\cup B)$. Therefore the converse is also true.

    - $\overline{A\cap B}\sub \overline A\cap \overline B$
        if $x\in A\cap B$, then $x\in A\sub \overline A, x\in B\sub \overline B\Longrightarrow x\sub \overline A\cap \overline B$. If $x\in \overline{A\cap B}$, $\forall \epsilon>0, B(x,\epsilon)\cap(A\cap B)-\{x\}\neq\varnothing, B(x,\epsilon)\cap A-\{x\}\neq\varnothing$ and $B(x,\epsilon)\cap B-\{x\}\neq\varnothing$, hence $x$ is in $\overline A$ and $\overline B$, and $x\in \overline A\cap \overline B$.

        Conversely suppose $x\in \overline A\cap \overline B$. If $x\in A\cap B$ then $x\in \overline{A\cap B}$. If $x\notin A, x\in B$, then $B(x,\epsilon)\cap A-\{x\}\neq\varnothing, B(x,\epsilon)\cap B-\{x\}\neq\varnothing, B(x,\epsilon)\cap (A\cap B)-\{x\}\neq\varnothing, (\overline A\cap \overline B)\not\sub\overline{A\cap B}$. Hence $\overline{A\cap B}\not\sub\overline A\cap\overline B$.

10. $x\in A \Longrightarrow d(x,x)=0 \Longrightarrow D(x,A)=0$,
    $x\notin A\Longrightarrow \forall \epsilon>0, B(x,\epsilon)\cap A-\{x\}\neq \varnothing$
    If $D(x,A)=\epsilon_0>0$ let $a\in B(x,\epsilon_0)\cap A-\{x\}$, then $d(x,a)<D(x,A)$ which contradicts. $\therefore x\in \overline A \Longrightarrow D(x,A)=0$.
    For converse, $D(x,A)=0$. Then there exists a sequence in $A$ that converges to $x$, hence $x\in \overline A$.

11. (a) the boundary of
        $(-1,1)\Longrightarrow\{-1,1\}$
        $[-1,1)\Longrightarrow\{-1,1\}$
        $[-1,1]\Longrightarrow\{-1,1\}$
    (b) $\mathbb Q\sub\R$: the boundary is $\R$ because any neighborhood has a point of $\mathbb Q$ and a point of $\R$.
    (c) For both disks, the boundary is $\{z\mid \lvert z\rvert=1\}$.

12. $B[a,b]$ is not separable: Consider a subset $F$, a set of functions $f(x)$ such that $f(x)=0$ if $a\le x<t$, 1 if $t\le x\le b$, for $a<t<b$. $F$ is uncountable and $B(f,1/2)=\{f\}$ for $f\in F$. If $B[a,b]$ has any dense subset $A$, disjoint and uncountably many neighbors $B(f,1/2)$ should contain a point of $A$, which makes $A$ uncountable.

13. $X$ is separable $\iff$ $X$ has a countable dense subset $\iff$ $X$ has a countable subset $Y$ such that $\forall \epsilon>0, \forall x\in X, \exists y\in Y, d(x,y)<\epsilon$. The interpretation is that for any point $x$, there exists a sequence of $(y_n)$ that converges to $x$.

14. Show ① $T:X\Longrightarrow Y$ is continuous $\iff$ ② $T^{-1}(M)$ is closed in $X$.
    ① to ②: $T^{-1}(M^c)=(T^{-1}(M))^c$. If $M$ is closed, $M^c$ is open, and by ①, $T^{-1}(M^c)$ is open. Since $(T^{-1}(M))^c$ is open, $T^{-1}(M)$ is closed.

    ② to ①: If $M$ is open, $M^c$ is closed, and by ②, $T^{-1}(M^c)=(T^{-1}(M))^c$ is closed, so $T^{-1}(M)$ is open.

15. $cos(x)$ on $(-2\pi,2\pi)$ has an open domain but the range $[-1,1]$ is closed.

## 1.4. Convergence, Cauchy Sequence, Completeness

1. If $(x_n)$ converges to a limit $x$, $\forall \epsilon>0, \exists N>0, \forall n>N, d(x_n,x)<\epsilon$, then for any $(x_{n_k})$, $\forall\epsilon>0, \exists K>0, \forall k>K, d(x_{n_k}, x)<\epsilon$, therefore $x_{n_k}\longrightarrow x$

2. $(x_n)$ is Cauchy and $x_{n_k}\longrightarrow x$, then $\forall \epsilon>0$,
   - $\exists K>0, \forall k>K, d(x_{n_k},x)<\epsilon/2$
   - $\exists N>0, \forall n,m>K, d(x_n,x_m)<\epsilon/2$
   - Then $\forall n>max(N,n_k), \exists i, n_i>n$, and $d(x_n,x)\le d(x_n,x_{n_i})+d(x_{n_i},x)<\epsilon/2+\epsilon/2=\epsilon$.
    Hence $(x_n)$ converges to $x$.

3. $(x_n)\longrightarrow x$ is equivalent to $\forall V=n(x), \exists n_0, \forall n>n_0, x_n\in V$
    ($\Longrightarrow$): for a neighborhood $V$, $\exists r, B_r(x)\sub V$, there exists $N$ such that $\forall n>N, d(x_n,x)<r$, hence $x_n\in B_r(x)\sub V$.

    ($\Longleftarrow$): For any $\epsilon>0$ and $B_\epsilon (x)$, there exists $n_0$ such that $x_n\in B_\epsilon(x) \Longrightarrow d(x_n,x)<\epsilon$ for all $n>n_0$. Hence $(x_n)\longrightarrow x$.

4. $\exists N, \forall n,m\ge N, d(x_n,x_m)<1\Longrightarrow \forall n\ge N, d(x_n,x_N)<1$. Hence $x_N,x_{N+1},..$ are bounded. Also $x_1, x_2, .. x_{N-1}$ are finite, so bounded.

5. No. A counter example is $x_n=\sin n$.

6. We will show that $(a_n)$ is Cauchy, then since $\R$ is complete, $(a_n)$ converges. For any $\epsilon>0, \exists N, \forall n,m>N, d(x_n,x_m)<\epsilon/4$ and $d(y_n,y_m)<\epsilon/4$. Then $|a_n-a_m|=|d(x_n,y_n)-d(x_m,y_m)|\le d(x_n,x_m)+d(y_n,y_m)<\epsilon/2$. Hence $(a_n)$ is Cauchy, thus convergent.

7. 1.4-2 (b) has a stronger condition than Prob 6, hence 1.4-2 (b) is true.

8. If $(x_n)$ is Cauchy in $(X,d_1)$, for $\epsilon>0$ and large enough $n,m$, we have $d_1(x_n,x_m)<b\epsilon$, or, $d_2(x_n,x_m)<\epsilon$. Hence $(x_n)$ is Cauchy in $(X,d_2)$. In the same way, a cauchy seq in $(X,d_2)$ is Cauchy in $(X,d_1)$.


9. It can be easily shown that $\tilde{\tilde{\kern{-0.3ex}d}}\le \tilde d\le d\le 2*\tilde{\tilde{\kern{-0.3ex}d}}$.

10. Consider a Cauchy sequence $c_n=(a_n+i b_n)$ in $\mathbb C$, where $a_n,b_n\in \R$. Then for any $\epsilon>0$ and large enough $n$ and $m$, $d(a_n,a_m)\le d(c_n,c_m)<\epsilon, d(b_n,b_m)\le d(c_n,c_m)<\epsilon$, hence $(a_n)$ and $(b_n)$ are Cauchy. Since $\R$ is complete, $(a_n)\longrightarrow a, (b_n)\longrightarrow b$. Again, for any $\epsilon>0$ and large enough $n$, $d(a_n,a)<\epsilon/2, d(b_n,b)=d(i b_n, i b)<\epsilon/2$, hence $d(c_n,a+bi)<\epsilon$, $(c_n)\longrightarrow a+bi$, $\mathbb C$ is complete.

## 1.5. Examples, Completeness Proofs

1. Since $\R$ is complete, a subset is complete iff it is complete. Hence $(a,b)$ is incomplete and $[a,b]$ is complete.

2. Consider a Cauchy $(x^(1),x^(2),\dots)$. For any $\epsilon$ and large enough $n,m$, $d(x^{(n)},x^{(m)})<\epsilon\Longrightarrow \forall j, |x_j^{(n)}-x_j^{(m)}|<\epsilon$. For a fixed $j$, (x^{(n)}_j) is Cauchy. Since $\R$ is complete, $x^{(n)}_j$ converges, and let the limit point $x_j$, and let $x=(x_n)$. Note that $x\in X$. For any $\epsilon>0$ and large enough $n,m$, $\forall j |x_j^n-x_j|\le \epsilon\Longrightarrow d(x^n,x)\le \epsilon$, and $x^n$ converges to $x$. Since any Cauchy converges, $X$ is compelte.

3. Let $x_1=(1,0,0,\dots), x_2=(1,1/2,0,0,\dots), x_3=(1,1/2,1/4,0,0,\dots), \dots$. The sequence $(x_1,x_2,\dots)$ converges to $(1,1/2,1/4,1/8,\dots)$ but this has infinitely many zeros, therefore this is not in $M$. Hence $M$ is not complete.

4. The previous example converges to a point not in $M$, hence $M$ is not closed, Since $l^\infty$ is complete, $M$ is not complete.

5. Consider a Cauchy $(x_n)$. For $\epsilon=0.5$ and large enough $n,m$, $|x_n-x_m|<1$, which means $x_n=x_m$ and the sequence is eventually constant and convergent. Hence $X$ is complete.

6. $(x_n=n)$ is Cauchy. Suppose this sequence converges to $x$. For large enough $n$, $x_n>x\Longrightarrow \arctan(x_n)>\arctan(x)$, so it cannot converge. Hence the space is incomplete.

7. Similar to 6, $(x_n=n)$ is Cauchy but it does not converge.

8. $C[a,b]$ is complete. We will show $Y$ is closed. Consider $(y_n)\longrightarrow y$ and suppose $y\notin Y$. Then $y(a)\neq y(b)$ and for any $\epsilon>0$ and large enough $n$, $|y_n(a)-y(a)|<\epsilon/2, |y_n(b)-y(b)|<\epsilon/2, |y(a)-y(b)|<\epsilon$, which implies $y(a)=y(b)$, a contradiction. Hence $Y$ is closed and complete.

9. $(x_m)\in C[a,b], (x_m)\Longrightarrow x$. For any $\epsilon>0$ and large enough $n$, $d(x_n,x)<\epsilon\Longrightarrow |x_n(t)-x(t)|<\epsilon$. Since $x_n$ is continuous, for any $\epsilon_2>0$ there exists $\delta>0$, $|t_1-t_2|<\delta\Longrightarrow |x_n(t_1)-x_n(t_2)|<\epsilon_2$. Then for $t_1,t_2\in [a,b]$ such that $|t_1-t_2|<\delta, |x(t_1)-x(t_2)|\le|x(t_1)-x_n(t_1)|+|x_n(t_1)-x_n(t_2)|+|x_n(t_2)-x(t_2)|<\epsilon+\epsilon_2+\epsilon$. Since $\epsilon$ and $\epsilon_2$ were chosen arbitrarily, $x$ is continuous.

10. Any Cauchy sequence in a discrete metric space is eventually constant (use $\epsilon=0.5$), and converges to the constant. Hence discrete metric spaces are complete.

11. Suppose $x_n\longrightarrow x$. Then for any $\epsilon>0$ and large enough $n$, $d(x_n,x)=\sum_j \frac{1}{2^j} \frac{|x_j^{(n)}-x_j|}{|x_j^{(n)}-x_j|+1}<\epsilon$. Since all terms are positive, $\frac{|x_j^{(n)}-x_j|}{|x_j^{(n)}-x_j|+1}<2^j \epsilon$. Let $f(t)=\frac{t}{1+t}$. $f$ is continuous and increasing. $f(|x_j^{(n)}-x_j|)<2^j\epsilon$ implies $x_j^{(n)}\longrightarrow x_j$. (why?)

12. Consider a Cauchy $(x^{(m)})$. For any $\epsilon>0$ and large enough $n,m$, $d(x^{(n)},x^{(m)})<\epsilon\Longrightarrow f(|x_j^{(n)}-x_j^{(m)}|)<2^j \epsilon\Longrightarrow |x_j^{(n)}-x_j^{(m)}|<f^{-1}(2^j\epsilon)$. For a fixed $j$ and any $\epsilon_2>0$, there exists $\epsilon_0$ such that $f^{-1}(2^j\epsilon_0)<\epsilon_2$. With $\epsilon=\epsilon_0$ in the previous inequality, $|x_j^{(n)}-x_j^{(m)}|<f^{-1}(2^j\epsilon_0)<\epsilon_2$, hence $x_j^{(n)}$ is Cauchy. This sequence converges to $x_j$ because $\R$ is complete. By Problem 11, $x^{(n)}\Longrightarrow x$. Therefore $s$ is complete.

13. With $n<m$, $d(x_n,x_m)=\int_{m^{-2}}^{n^{-2}}(t^{-1/2}-t)dt=[2t^{1/2}-1/2 t^2]_{m^{-2}}^{n^{-2}}=2(n^{-1}-m^{-1})-1/2(n^{-4}-m^{-4})<2(n^{-1}-m^{-1})<2n^{-1}$. Thus for any $epsilon>0$, choose $n$ such that $2n^{-1}<\epsilon$, then $d(x_n,x_m)<\epsilon)$. Hence $(x_n)$ is Cauchy.


14. $(x_n)$ converges to $x(t)=t^{-1/2}$ for $t>0$, but $x(0)=0$. Hence $x$ is not continuous at $t=0$ and $x$ is not in the space.

15. $d(x_n,x_m)=\frac{1}{(n+1)^2}+\frac{1}{(n+2)^2}+\dots+\frac{1}{m^2}\le \int_{n+1}^{m+1} \frac{1}{t^2} dt = [-1/t]^{m+1}_{n+1}=\frac{1}{n+1}-\frac{1}{m+1}<\frac{1}{n+1}$. Therefore for $n,m>1/\epsilon, d(x_n,x_m)<\frac{1}{n+1}<\frac{1}{n}<\epsilon$, Hence this is Cauchy.
Suppose this converges to $x$. Let $k$ the index ofo the last nonzero element of $x$. Then for $n>k, d(x,x_n)>\frac{1}{(k+1)^2}+\frac{1}{(k+2)^2}+\dots+\frac{1}{n^2}$. Hence $d(x,x_n)>\frac{1}{(k+1)^2}$ and $(x_n)$ does not converge to $x$.


## 1.6. Completion of Metric Spaces
