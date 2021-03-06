# 3. Random Variable. Expectation. Independence

## 3.1. General Definitions



1. f

2. d

3. Define r.v. X as the identity, so $X(B)=B$ for $B\in\mathscr B_1$. Then $\mu(X^{-1}(B))=\mu(B)$. An identity mapping may be not continuous in some spaces, which means there exists an open set $B$ such that $X^{-1}(B)$ is not open, thus $\mu\circ X^{-1}$ is not defined at $B$.

4. We need to show $\mathscr P\{G(\theta)\le x\}=F(x)$ for all $x\in\R$. This is equivalent to $\mathscr P\{\sup\{y;F(y)\le\theta(\omega)\}\le x\}=F(x)$ for all $x$. $\sup\{y;F(y)\le\theta\}\le x \iff F(x)\ge \theta$, and $\mathscr P\{F(x)\ge\theta(\omega)\}=P\{\theta(\omega)\le F(x)\}=D(F(x))=F(x)$ where $D$ is a d.f. of uniform distribution on $[0,1]$. Hence it is proved.

5. Let $G$ the d.f. of of $F(X)$. Then for $k\in[0,1]$, $G(k)=\mathscr P\{F(x)\le k\}=\mathscr P\{x\le F^{-1}(k)\}=F(F^{-1}(k))=k$ where $x\le F^{-1}(k)$ means $x$ is equal to or smaller than any element of $F^{-1}(\{k\})$. Hence $F(X)$ has the uniform distribution on $[0,1]$. The continuity is used for $F^{-1}(k)\neq\varnothing$. If $F$ is not continuous, for example $F$ jumps from $0.2$ to $0.3$ at $x_0$, $G(k)$ is not defined on $(0.2,0.3)$. Clearly this is not uniform distribution.

6..

7..

8..

9..

10..

11. ($X$ is r.v.) Since $X$ is measurable, $X^{-1}(B)\in \mathscr F\{X\}$. Conversely, $\mathscr F\{X\}$ is generated by a collection of $X^{-1}(B)$ for $B\in\mathscr B^1$. Any element of $\mathscr F\{X\}$ is made of complement/union/intersection of basis elements, and the inverse is commutative with complement/union/intersection, hence $\Lambda\in\mathscr F\{X\}\Longrightarrow \Lambda=X^
{-1}(B)$ for some $B$.  $B$ is not unique if $x$ is not surjective.

## 3.2. Properties of mathematical expectation

(46p)

1. From $X\ge 0$ a.e., there exists a null set $N$ such that $X\ge 0$ on \Lambda\setminus N$. Consider a set $E_n=\{X\ge 1/n\}$. Then $\mathscr P(E_n)=0$ because if not, $\mathscr P(E_n)>0, \int_\Lambda Xd\mathscr P=\int_{\Lambda\setminus N} Xd\mathscr P\ge \int_{E_n} Xd\mathscr P\ge \mathscr P(E_n)*1/n>0$, which contradicts. Let $E=\cup_n E_n=\{X>0\}$, then $\mathscr P(E)=0$. Hence $X=0$ on $\Lambda\setminus E\setminus N$ whose the measure is 1. Therefore $X=0$ almost everywhere.

2. (The statement is wrong in a case of direc-delta function?) [WIP] In particular, suppose $\lim_{n\Longrightarrow\infty}\mathscr P(|X|>n)=k>0$. Then it is a contradiction that $\int_X Xd\mathscr P\ge nk$ for all $n$ and thus $\int_X Xd\mathscr P=\infty$. Therefore $\lim_{n\Longrightarrow\infty}\mathscr P(|X|>n)=0$. (Or, more easily, use Theorem 3.2.1) Using the first statement in the problem,  $\lim_{n\longrightarrow\infty}\int_{|X|>n}Xd\mathscr P=0$.

3. We show three conditions on page 21. (iii) $\nu(\Omega)=1d$, (i) $X\ge 0\Longrightarrow \nu(\Lambda)\ge 0$, (ii) the additivity from the additivity of integral. Therefore $\nu$ is a p.m.

4. $\sum_{n=1}^\infty \mathscr P(|X|\ge cn)=\sum_{n=1}^\infty \mathscr P(|X|/c\ge n)<\infty \iff \mathscr E(|X|/c)<infty \iff \mathscr E(|X|)<infty$.

5. ?

6. Let $Z_n=Y-X_n$ and apply Fatou's lemma on $Z_n$. Since $Y-\limsup X_n=\liminf Z_n$, we get the desired inequality. Without the condition on $Y$, it's equivalent to claim Fatou's lemma without non-negativity, which is known false. (TODO: Counterexample)

7. (This problem is equivalent to Folland 2.26) We use the dominated convergence theorem. First let $X=X^+-X^-$. For $X^+$, there exists a sequence of simple rv.s $(\phi^+_n)$ that pointwise converges to $X^+$. $|\phi^+_n-X^+|$ converges to $0$. Also $|\phi^+_n-X^+|\le|\phi^+_n|+|X^+|\le 2|X^+|$ and since $|X^+|$ is integrable, $|\phi^+_n-X^+|$ is bounded by an integral function. Now we apply the dominated convergence theorem on $|\phi^+_n-X^+|$ and get $\int |\phi^+_n-X^+| \longrightarrow \int \lim |\phi^+_n-X^+| = 0$. This means that for any $\epsilon>0$ and large enough $n$, $\int |\phi^+_n-X^+| < \epsilon/2$. We can do the same for $X^-$, and combining them to get the desired result.d

8.

#### Part 2

9..

10. Let $\phi(x)=x^{r'/r}$. Then $\phi$ is convex. By Jensen inequality, $\phi(\int |X|^{r})\le \int \phi(|X|^{r})=\int |X|^{r'}<\infty$. For the second statement, when $p\ge 1$ and $\mathscr E(|X|^r)<\infty$, using Minkowski, $\mathscr E(|X-a|^r)^{1/r} < \mathscr E(|X|^r)^{1/r} + \mathscr E(|a|^r)^{1/r} < \infty$. For the other direction, $\mathscr E(|X|^r)^{1/r}=\mathscr E(|X-a+a|^r)^{1/r}<E(|X-a|^r)^{1/r}+E(|a|^r)^{1/r}<\infty$. For $0<p<1$, $|X-a|^r\le |(|X|+|a|)|^r\le |X|^r+|a|^r$ since $f(x)=x^r$ is concave and the subadditivity holds. Similarily, $|X|^r=|X-a+a|^r\le |X-a|^r+|a|^r$. Applying integrals on both sides, this proves the second statement.d

11..

12..

13..

14..

15..

16. $\int_{-\infty}^{\infty}[F(x+a)-F(x)]dx=\int_{-\infty}^{\infty}\int_{x}^{x+a} f(t) dt dx=\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(t) \chi_E(x,t) dt dx$ where $E=\{x\le t\le x+a\}$. By Fubini, This is equal to $\int\int f(t)\chi_E(x,t)dxdt = \int f(t) \int \chi_E(x,t) dxdt = \int f(t)*a \,dt=a\int_{-\infty}^\infty f(t)dt = a*1 = a$.

17. $\int_0^\infty (1-F(x)) dx=\int_0^\infty \mathscr P(X>x)dx=\int_0^\infty \int_x^\infty \mathscr f(t) \,dt \,dx$. By Tonelli, this is $=\int_0^\infty \int_0^t \mathscr f(t) \,dx \,dt=\int_0^\infty t*f(t)\,dt=\mathscr E(X)$. Since $\mathscr P(X=x)=0$, $\mathscr P(X>x)=\mathscr P(X\ge x)$.

18..
19. ???
20..

## 3.3. Independence

1. [WIP] Let $\mathscr F=\{\varnothing,\{a\},\{b\},\{a,b\}\}, \mathscr P_1(\{a\})=0.5, \mathscr P_1(\{b\})=0.5, \mathscr P_1(\{a,b\})=1, X_1(a)=1, X_1(b)=2, X_2(a)=1, X_2(b)=1$. Then $\mathscr P(X_1=1)=0.5, P(X_2=1)=1$

2. It can be easily checked that they are pairwise independent. They are not totally independent because $P(X_1X_2=1,X_1=1,X_2=1)=1/4\neq P(X_1=1)P(X_1=1)P(X_1X_2=1)=1/8$. $\mathscr F=\{X_1,X_2,\dots,X_{n-1},X_1X_2X_3\dots X_{n-1}\}$ is an example that every $n-1$ of them are independent but not all of them. Let $\Lambda_1=\{b,c\},\Lambda_2=\{a,b\},\Lambda_3=\{c,d\}, P(b)=1/4=P(ab)P(bc)=1/2*1/2$ and $P(c)=1/4=P(bc)P(cd)=1/2*1/2$. Then $\Lambda_1$ and $\Lambda_2\cup\Lambda_3=\{a,b,c,d\}$ are not independent.

3..

4..

5..

6..

7..

8..

9. $\int_{Y\in B}Xd\mathscr P=\int X\Delta_B(Y)d\mathscr P=\mathscr E(X\Delta_B(Y))=\mathscr E(X) \mathscr E(\Delta_B(Y))=\mathscr E(X) \mathscr P(Y\in B)$. $X$ and $\Delta_B(Y)$ are independent because the identity is measurable and an indicator of a borel set is measurable, so by Theorem 3.3.1 they are independent.

10. Let any possible value of $Y$ be $y$. By Fubini, $\mathscr E(|X+y|^p)<\infty$. There exists a constant $c\in(0,\infty)$ such that $|a+b|^p\le c(|a|^p+|b|^p)$ for all $a, b$.  Then $\mathscr E(|X|^p)=E(|X+y-y|^p)\le \mathscr E((|X+y|+|y|)^p)\le\mathscr E(c(|X+y|^p+|y|^p))=\mathscr cE(|X+y|^p)+|y|^p<\infty$. The similar proof for $\mathscr E(Y)$ holds. [link](https://math.stackexchange.com/questions/1589248/if-the-sum-of-two-independent-random-variables-is-lp-does-it-imply-that)

11..

12..

13..

14..

15..

16..

17..

18..

19..

20..