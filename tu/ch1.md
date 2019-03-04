# Chapter 1. Euclidean Spaces
## 1 Smooth Functions on a Euclidean Space

summary.
$C^k, C^\infty$, smooth, real-analytic, star-shaped, taylor theoerem, diffeomorphism

1.1. (???) negative^fraction is not defined in R->R

 <!-- $g(x)=\frac{3}{4}x^\frac{4}{3}, $ -->


1.2.
(a) Suppose $f^{(k)}(x)$ is continuous and of the form $p_{2k}(1/x)e^{-1/x}$ for some $k\le 0, x>0$. Then $\frac{dp_{2k}(1/x)}{dx}=p_{2k-1}(1/x)*(-1/x^2)$ which is a $2k+1$ degree polynomial of $1/x$, and $\frac{de^{-1/x}}{dx}=e^{-1/x}*(1/x^2)$, hence $f^{(k)}(x)$ is of degree $2(k+1)$. Since it can be easily shown that the statement is true for $k=0$, it is true by induction.
(b) Suppose $f^{(k)}(0)=0$ and $f^{(k)}$ is continus for some $k$. Then $f^{(k+1)}(0)=\lim_{x\longrightarrow 0} \frac{f^{(k)}(x)-f^{(k)}(0)}{x}=\lim_{x\longrightarrow 0} \frac{f^{(k)}(x)}{x}$. The limit from left is $0$ since it is obvious that $f^{(k)}(x)=0$ for $x<0$. The limit from right is, by L'Hopital's rule, $\lim_{x\longrightarrow 0+} \frac{f^{(k+1)}(x)}{1}$ if this limit exists. This limit is zero because $\lim_{x\longrightarrow 0+} f^{(k+1)}(x)=\lim_{x\longrightarrow 0+} p_{2k+1}(1/x) e^{-1/x}=\lim_{y\longrightarrow \infty} p_{2k+1}(y)/e^y=0$, from that $e^y$ grows much faster than the polynomial $p_{2k+1}(y)$. Both left limit and right limit are zero, therefore $f^{(k+1)}(0)$ exists and is zero. Also $f^{(k+1)}$ is continuous since its limit from right at $x=0$ is zero. For $k=0$, $f^{(0)}(0)=0$ and $f^{(0)}$ is continus. By induction, the statement is true.

-

1.3.

(a)
- $\tan x$ is smooth because $\tan^{(k)}$ is a polynomial of $\tan$ and $\sec$ which is continuous.
- $\arctan x$ is smooth because $\arctan^{(k)} x = \frac{P(x)}{(1+x^2)^k}$ where $P(x)$ is a polynomial of $x$ and this is continuous for all $k\ge 0$.
- $\tan x$ is strictly increasing, and it is easy to show that $\tan$ is bijective from $(-\pi/2,\pi/2)$ to $(-\infty,\infty)$.
Hence $\tan$ is diffeomorphism.

(b) Given $a,b$, we can scale and shift $\arctan$ to get $h$. Precisely, $\arctan$ maps an interval $(a,b)$ to $(\arctan a, \arctan b)$, therefore let $h(x)=\arctan(x-(a+b)/2)/\arctan ((b-a)/2)$, then $h$ maps from $(a,b)$ to $(-1,1)$. This proves $(a,b)$ and $(-1,1)$ are diffeomorphic, and it it clear that the inverse is also a diffeomorphism from $(-1,1)$ to $(a,b)$. Hence arbitrary two intervals $(a,b)$ and $(c,d)$ are diffeomorphic by transitivity.

(c) ??
$-e^x$ is a diffeomorphism from $\R$ to $()$

1.4.
**1.5.
1.6.
1.7.
1.8.

## 2 Tangent Vectors in $\R^n$ as Derivations

summary. $T_p(\R^n), D_v f$, relation, germ of $f$ at $p$, $C_p^\infty(\R^n)=C_p^\infty$, $\R$-linear, Leibniz rule, a point derivation of $C_p^\infty$, $D_p(\R^n)$, kronecker delta,

## 3 The Exterior Algebra of Multicovectors
## 4 Differential Forms on $\R^n$
