# 4장. 표본분포

## Problems
4.1
$\operatorname{pdf}_Y(y)=1/\pi * \cos^2(x)=1 / ({\pi(y^2+1)})$

4.2
$g(y_1,y_2)=f(x_1=y_1,x_2=y_1+y_2)=2e^{-2y_1-y_2} I_{(0<y_1,0<y_2)}$
$g_1(y_1)=2e^{-2y_1}$, $g_2(y_2)=e^{-y_2}$, hence independent.

4.4
$g(y_1,y_2,y_3)=f(x_1=y_1,x_2=y_1+y_2,x_3=y_1+y_2+y_3)=6e^{-3y_1-2y_2-y_3} I_{(0<y_1,0<y_2,0<y_3)}$
$g_1(y_1)=3e^{-3y_1}$, $g_2(y_2)=2e^{-2y_2}$, $g_3(y_3)=e^{-y_3}$, hence independent.

4.6
$g(y_1,y_2)=f(y_1y_2,y_2)=2e^{-y_1y_2-y_2} I_{(0<y_1<1,0<y_2)}$
(a) $g_1(y_1)=2e^{-y_1}/y_1$
(b) $g(y_2|y_1)=g(y_1,y_2)/g(y_1)=e^{y_1-y_1y_2-y_2}y_1$
    $E(Y_2|Y_1)=\int_0^\infty y_2 g(y_2|y_1)dy_2 = ..$
    $Var(Y_2|Y_1)=\int_0^\infty (y_2-E(Y_2|Y_1))^2 dy$=..

4.8
(a) $g(y)=\sum f(x_i) |dy/dx|^{-1}=1/4 |1/2x| * 2 = 1/(4\sqrt y)$
(b) ..



4.10
(a) Let $W_i=X_1+\cdots+X_i$. Then $X_i \sim \operatorname{Gamma}(1,1/\lambda)$ and these $X_i$ are independent. Hence $f(y_1,\cdots,y_k)$ is Dirichlet with $c=k!$. We get $f(y_1,\cdots,y_k)=k!$.
(b) Let $V_1=X, V_2=Y-X$. Then $f_{XY}(X,Y)=f_{XY}(V_1,V_1+V_2)=g_V(V_1,V_2) |J|^{-1}=g_V(V_1,V_2)$ and $V_1=W_2/W_5, V_2=(W_4-W_2)/W_5$. Since $W_2, (W_4-W_2)\sim \operatorname{Gamma}(2,1/\lambda)$ and $(W_5-W_4)\sim \operatorname{Gamma}(1,1/\lambda)$, this is again Dirichlet with $\alpha_1=\alpha_2=2,\alpha_3=1$. $g_V(V_1,V_2)=5! V_1 V_2=5! X(Y-X)$ where $0<X<Y<1$.


4.12
(a) $F(x)=x$. $F_Y(y)=1-(1-y)^n, f_Y(y)=n(1-y)^{n-1}$.
(b) $F_Y(y)=y^n, f_Y(y)=ny^{n-1}$.

4.14

4.16
$f(U_1,U_n)=n!/(n-2)!*(U_n-U_1)^{n-2}$
$f(U_n-U_1=\Delta)=\int_{U_1=0}^{1-\Delta} f(u_1,u_1+\Delta)du_1=\int_{U_1=0}^{1-\Delta} n!/(n-2)! \Delta^{n-2} du_1=n(n-1)(1-\Delta)\Delta^{n-2}$


4.18
(a) $X$ increases as $U$ increases. $U=1-e^{-(X^\alpha)/\beta^\alpha}$. Hence $g(u)=f(x) |du/dx|^{-1}, f(x)=g(u)|du/dx|=e^{-x^\alpha/\beta^\alpha}(\alpha/\beta^\alpha)x^{\alpha-1}$.


(b) $F(x)=P(X\le x)=P(U\le u)=u=1-e^{-(x^\alpha)/\beta^\alpha}$, and $f(x)/(1-F(x))=(\alpha/\beta^\alpha)x^{\alpha-1}$.


4.20

4.22

4.24
