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
