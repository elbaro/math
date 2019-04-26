# 5장. 표본분포의 근사


5.2

$Z=(X-25)/5=X/5-5\sim N(0,1)$
(a) $P(19<X\le 33)=P(-6/5<Z\le 8/5)$
(b) $P(19.5<X\le 33.5)=P(-5.5/<Z\le 8.5/5)$

5.4
$P(Y_n\le x)=P(X_1\le x)^n=I_x(1,\alpha)^n=(1-(1-x)^\alpha)^n$
$P(n^{1/\alpha}(1-Y_n)\le x)=P(1-xn^{-1/\alpha}\le Y_n)=1-P(Y_n\le 1-xn^{-1/\alpha})=1-(1-(1-(1-xn^{-1/\alpha}))^\alpha)^n=1-(1-(xn^{-1/\alpha})^\alpha)^n=1-(1-(xn^{-1/\alpha})^\alpha)^n=1-(1-x^\alpha n^{-1})^n$

Using $(1-x^\alpha n^{-1})^n=(1-x^\alpha/n)^{n/x^\alpha*x^\alpha}\Longrightarrow (1/e)^{x^\alpha}$, The last term is $1-e^{-x^\alpha}$.

If $Z\sim \exp(1)$, then $P(Z\le x^\alpha)=1-e^{-x^\alpha}=P(Z^{1/\alpha}\le x)$. Therefore the given quantity has the same distribution as $Z^{1/\alpha}$ where $Z\sim \exp(1)$.

5.6
$P(Y_n\le x)=P(X_1\le x)^n=(1-e^{-x})^n$
$P(Y_n-\log n\le x)=P(Y_n\le x+\log n)=(1-e^{-x}/n)^{n/e^{-x}*e^{-x}}\Longrightarrow e^{-x-1}$

5.8
(a) $\operatorname{plim} (X_n,Y_n)^t=(\operatorname{plim} X_n, \operatorname{plim} Y_n)^t=(0,1)^t$
(b) $\operatorname{pdf}(X_n\ge x, Y_n\le y)=(y-x)^n$
$\operatorname{pdf}(X_n=x,Y_n=y)=\frac{\partial}{\partial x}\frac{\partial}{\partial y} (y-x)^n = \frac{\partial}{\partial x}n(y-x)^{n-1}=n(n-1)(y-x)^{n-2}$
$\operatorname{pdf}(R_n=r)=\int_{x=0}^{1-r} P(x_n=x,y_n=r+x) dx=n(n-1)r^{n-2}(1-r)$
$\operatorname{pdf}(n(1-R_n)=x)=\operatorname{pdf}(R_n=1-x/n)=n(n-1)(1-x/n)^{n-2}(x/n)=(n-1)(1-x/n)^{n-2}x$





5.10
(a) $\limsup P(|X_n+Y_n|>k) = \limsup P(|X_n+Y_n|>2k) \le \limsup P(|X_n|>k)+\limsup P(|Y_n|>k)=0$
(b) $\limsup P(|X_nY_n|>k)\le\limsup P(|X_n|>\sqrt k)+\limsup P(|Y_n|>\sqrt k)=0$
(c) We want to show $\forall \epsilon>0, \lim_{n\longrightarrow \infty} P(|Z_nX_n|>\epsilon)=0$. For any $\epsilon>0, \delta>0$, there exists $K>0$ such that $\forall k>K, \sup P(|X_n|>k)<\delta/2$. Also there exists $N>0$ such that $\forall n>N, P(|Z_n|>\epsilon/K)<\delta/2$. Since $\{ |Z_nX_n|>\epsilon \}\sub \{ |Z_n|>\epsilon/k \}\cup \{ |X_n|>k \}$, we have for $n>N$, $P(|Z_nX_n|>\epsilon)\le P(|Z_n|>\epsilon/K)+P(|X_n|>K)\le P(|Z_n|>\epsilon/K)+\sup_i P(|X_i|>K)<\delta$, which proves the statement.

(d) $\sup P(|Z_n|>k)$ is a non-increasing function of $k$ and bounded below by $0$, hence $\lim \sup P(|Z_n|>k)$ exists and is non-negative. Suppose this value is not $0$, i.e. $\lim_{k\longrightarrow \infty} \sup_n P(|Z_n|>k) = c>0$. This implies $\forall k>0, \sup_n P(|Z_n|>k)\ge c$. Since a supremum is at least $c$, all $P$ values are at least $c/2$. Hence $\forall k>0, \forall n>0, P(|Z_n|>k)\ge c/2>0$. This contradicts to the assumption $Z_n=o_P(1)$, i.e. $\forall k>0, \lim_n P(|Z_n|>k)=0$.

5.12
By the CLT, $\sqrt n (\overline X - \lambda)\sim N(0,\lambda)$. With $g(X_i)=X_i/\sqrt \lambda$, $\sqrt n (g(\overline {X_n})-g(\lambda))\sim N(0,1)$. We can estimate a confidence interval, for example, $P(-3\le \sqrt n (g(\overline{X_n})-\sqrt \lambda)\le 3)\approx 0.9973$.


5.14

(a) By the CLT, $\sqrt n \overline X \sim N(0,1)$. For every $\epsilon>0$ we have $\lim_{n\longrightarrow \infty} P(\sqrt n \overline X \overline Y>\epsilon)\le \lim P(n^{1/4} \overline X>\sqrt \epsilon)+\lim P(n^{1/4} \overline Y>\sqrt \epsilon)=\lim P(\sqrt n \overline X>n^{1/4} \sqrt \epsilon)+\lim P(\sqrt n \overline Y>n^{1/4} \sqrt \epsilon)=0+0=0$. Hence $\operatorname{plim} \sqrt n \overline X \overline Y = 0$. We get the 'therefore' part from canceling $\overline{XY}$ and multiplying both sides by $\sqrt n$.

(b) With $m_1=\overline X, m_2=\overline{X^2}$, the statement is $\sqrt{m_2-m_1^2}-\sqrt{m_2}=-m_1^2/(\sqrt{m_2-m_1^2}+\sqrt{m_2})$, which can be easily proven by manipulation.

[TODO: Prove 'therefore' part]


(c)

By the CLT, $\sqrt n (\overline{X^2}-1)/\sigma_{\overline{X^2}}\sim N(0,1)$. With $g(x)=(\sqrt x-1)^2$, we have $\sqrt n (g(\overline{X^2})-g(1))/\sigma_{\overline{X^2}}\sim g'(1) N(0,1)$, which simplifies to $\sqrt n (\sqrt{\overline{X^2}}-1)^2/\sigma_{\overline{X^2}}\sim 0$. The condition required for this is $\sigma_{\overline{X^2}}<\infty$.

From the given assumption $E[X^4]<\infty$, we have $E[\overline{X^2}^2]<\infty, \operatorname{Var}[\overline{X^2}]=E[\overline{X^2}^2]-E[\overline{X^2}]^2<\infty - 1, \sigma_{\overline{X^2}}<\infty$.

$\sqrt n r_{3n} = -\frac{1}{2}\sqrt n (\overline{X^2}-2\sqrt{\overline{X^2}}+1)=-\frac{1}{2}\sqrt n (\sqrt{\overline{X^2}}-1)^2\sim 0$.


(d)


(e)

5.16
[TODO]
