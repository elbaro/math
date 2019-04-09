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
(b) this margin is too narrow to contain the demonstration.



4.10
(a) Let $W_i=X_1+\cdots+X_i$. Then $X_i \sim \operatorname{Gamma}(1,1/\lambda)$ and these $X_i$ are independent. Hence $f(y_1,\cdots,y_k)$ is Dirichlet with $c=k!$. We get $f(y_1,\cdots,y_k)=k!$.
(b) Let $V_1=X, V_2=Y-X$. Then $f_{XY}(X,Y)=f_{XY}(V_1,V_1+V_2)=g_V(V_1,V_2) |J|^{-1}=g_V(V_1,V_2)$ and $V_1=W_2/W_5, V_2=(W_4-W_2)/W_5$. Since $W_2, (W_4-W_2)\sim \operatorname{Gamma}(2,1/\lambda)$ and $(W_5-W_4)\sim \operatorname{Gamma}(1,1/\lambda)$, this is again Dirichlet with $\alpha_1=\alpha_2=2,\alpha_3=1$. $g_V(V_1,V_2)=5! V_1 V_2=5! X(Y-X)$ where $0<X<Y<1$.


4.12
(a) $F(x)=x$. $F_Y(y)=1-(1-y)^n, f_Y(y)=n(1-y)^{n-1}$.
(b) $F_Y(y)=y^n, f_Y(y)=ny^{n-1}$.

4.14
Let $Y=(U_1,..U_n)$ and $Z=(U_1,U_2/U_1,..U_n/U_{n-1})$. Then $y_1=z_1, y_2=z_1z_2, y_3=z_1z_2z_3, \cdots$. $\operatorname{pdf}_Z(z) = \operatorname{pdf}_U(u) |\frac{\partial y}{\partial z}|=n!*1*z_1*z_1z_2*z_1z_2z_3*\cdots$. Marginalize $z_1$ out: $\int_0^1 \operatorname{pdf}_Z(z)dz_1=n!/(n+1)*z_2^{n-1}z_3^{n-2}\cdots z_n$. Hence $f(U_2/U_1,\cdots,U_n/U_{n-1})=n!/(n+1)*(U_2/U_1)^{n-1}(U_3/U_2)^{n-2}\cdots (U_n/U_{n-1})=n!/(n+1)*\frac{U_2U_3\cdots U_n}{U_1^{n-1}}$.

4.16
$f(U_1,U_n)=n!/(n-2)!*(U_n-U_1)^{n-2}$
$f(U_n-U_1=\Delta)=\int_{U_1=0}^{1-\Delta} f(u_1,u_1+\Delta)du_1=\int_{U_1=0}^{1-\Delta} n!/(n-2)! \Delta^{n-2} du_1=n(n-1)(1-\Delta)\Delta^{n-2}$


4.18
(a) $X$ increases as $U$ increases. $U=1-e^{-(X^\alpha)/\beta^\alpha}$. Hence $g(u)=f(x) |du/dx|^{-1}, f(x)=g(u)|du/dx|=e^{-x^\alpha/\beta^\alpha}(\alpha/\beta^\alpha)x^{\alpha-1}$.


(b) $F(x)=P(X\le x)=P(U\le u)=u=1-e^{-(x^\alpha)/\beta^\alpha}$, and $f(x)/(1-F(x))=(\alpha/\beta^\alpha)x^{\alpha-1}$.


4.20
$X=\tan((U-1/2)\pi)$
The problem asks to prove $\operatorname{pdf}_X(x)=1/(\pi(1+x^2))$ for $-\infty<x<\infty$. Replace $x=tan \theta$. Then $\operatorname{pdf}_X(x)=\operatorname{pdf}_\Theta(\theta)(dx/d\theta)^{-1}=\operatorname{pdf}_U(u)(d\theta/du)^{-1}(dx/d\theta)^{-1}=(1/\pi)(sec^2 \theta)^{-1}=(1/\pi)(1+\tan^2 \theta)^{-1}=1/(\pi(1+x^2))$.

4.22
Using a polar coordinate,
$f(x,y)=(1/2\pi) e^{-0.5r^2}(1+r^2 cos\theta sin\theta e^{-0.5r^2+1})=g(r,\theta) |dr\theta/dxy|^{-1}=g(r,\theta)/r$
$\int_0^\infty \int_0^{2\pi} g(r,\theta) d\theta dr=\int_0^\infty r e^{-0.5r^2}dr=[-e^{-0.5r^2}]_0^\infty=1$. Hence this is a distribution.

$f(x)=\int_{-\infty}^{+\infty} \frac{1}{2\pi}e^{-\frac{1}{2}(x^2+y^2)}+\frac{1}{2\pi}xye^{-x^2-y^2+1} dy$, using $\int_{-\infty}^\infty e^{-y^2}dy=\sqrt \pi$ and $\int_{-\infty}^\infty ye^{-y^2}dy=0$, we have $f(x)=\frac{1}{2\pi}e^{-0.5x^2} \sqrt{2\pi}=\frac{e^{-0.5x^2}}{\sqrt{2\pi}}=N(0,1)$. In the same way, $f_2(y)=N(0,1)$.

4.24
(a) $Y_1=(X_1-X_2+X_3,2X_1+X_2-X_3,0)^T=\begin{bmatrix}
   1 & -1 & 1 \\
   2 & 1 & -1 \\
   0 & 0 & 0
\end{bmatrix}(AZ+\mu)=(\begin{bmatrix}
   1 & -1 & 1 \\
   2 & 1 & -1 \\
   0 & 0 & 0
\end{bmatrix}A) Z + \begin{bmatrix}
   2 \\ 1 \\ 0
\end{bmatrix}$
The new mean is $[2,1,0]^T$ and new variance matrix is $(MA)(MA)^t=MAA^tM^t=M\Sigma M^t=\begin{bmatrix}
   5 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 0
\end{bmatrix}$.
Ditching the last one, the original $Y$ follows $N([2,1]^T,\begin{bmatrix} 5 & 1 \\ 1 & 2 \end{bmatrix})$.
