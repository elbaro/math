# 2장. 다차원 확률변수의 확률분포

## Notes
- joint moment = $M(t_1,t_2)=E(e^{t_1X+t_2Y})$
- joint cumulant = $C(t_1,t_2)=\log M(t_1,t_2)$
- independence =>
  - cdf = cdf*cdf
  - pdf = pdf*pdf
  - mgf = mgf*mgf
  - g_1(X) and g_2(Y) are independent
  - E[g_1(X)g_2(Y)] = E[g_1(X)]E[g_2(Y)]
- - Cov(X,Y)=0
- pdf=g1(x)g2(y) => independent
- same for cdf, mgf.

- Var(X+Y)=Var(X)+Var(Y)=2Cov(X,Y)
---

- Var(matrix X)=E[(X-mean)(X-mean)^T]
- Cov(matrix X, matrix Y)=E[(X-Xmean)(Y-Ymean)^T]
- Var(AX+b)=AVar(X)A^T
- Cov(AX+b,CY+d)=ACov(X,Y)C^T
- Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)
- Cov(X,Y+Z)=Cov(X,Y)+Cov(X,Z)
- Var(X+Y)=Var(X)+Var(Y)+Cov(X,Y)+Cov(Y,X)

- For multi-dim cgf, see page. 95

- multi-dim independence =>
  - Cov(X,Y)=0
  - Var(X1+..+Xn) = Var(X_1)+..Var(Xn)
  - mgf_{X_1+..}(t)=mgf_{X_1}(t)mgf_{X_2}(t)..
  -

## Problems

2.1
(a) $P(Y\le 1/2)=\int_0^1\int_x^1 10xy^2 dy dx$
(b) $P(X+Y\le 1)=\int_0^1\int_x^{1-x} 10xy^2 dy dx$

2.2
(a) $\int_0^1\int_x^1 cx^2y dydx=1$
(b) similar to 2.1 (a)
(c) $\int_0^1\int_x^{\min(1,2x)} cx^2y dydx=1$

2.4
(a) $f_1(x)=\int_x^1 2 dy=2(1-x)$
(b) $f_1(x)=\int_x^\infty e^{-y} dy=e^{-x}$

2.6
$E[X] = \int_0^\infty x \int_x^\infty xe^{-y} dy dx$
$E[Y] = \int_0^\infty y \int_0^y  xe^-y  dx dy$

$\operatorname{Cov}(X,Y) = E[(X-E[X])(Y-E[Y])]$

2.8
(a) $f_2(y)=\int_0^y 10xy^2 dx=5y^4$
(b) $f_{1,2}(x,y)/f_2(y)=2x/y^2$
(c) $E(X|Y)=2y/3, Var(X|Y)=E((X-E(X|Y))^2|Y)=\int_0^y (X-E(X|Y))P(X|Y)dx=\int_0^y (x-2y/3)(2x/y^2)dx$
(d) $\operatorname{Var[E(X|Y)]}=$, E[\operatorname{Var}(X|Y)]$
(e) $f_1(x)=\int_x^1 10xy^2 dy$, $E[X]=..$, $\operatorname{Var(X)}=E[(X-E[X])^2]=..$

2.10
(a) Var[E(X|Y)]=
, E[Var(X|Y)]
(b) d

..

2.12

2.14

2.16
