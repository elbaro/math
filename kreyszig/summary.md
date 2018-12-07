## Note

**countable** in Kreyszig's means **at most countable**, in other words, **finite** or **countably infinite**.

## Spaces

- B(X,Y): Bounded linear operator from normed X to normed Y
- C(X,Y): A subset of B(X,Y), compact operators
- c(X,Y): ?

## Complete set
In a complete set $X$,
- A closed subset is complete
-

## Compact set

## Finite dimension
- A set of finite dim is closed

## Relatively compact set
- Relatively compact $\Longrightarrow$ totally bounded
- Totally bounded $\Longrightarrow$ bounded

## Compact operator
- Compact $T$ is linear, bounded, hence continuous
- If $\dim X=\infty$, $I$ is not compact
- A composition (bounded)$\circ$(compact) is compact
- A composition (compact)$\circ$(bounded) is compact
- A linear $T:X\longrightarrow Y$ is compact $\iff$ for any bounded seq $(x_n)$, $(Tx_n)$ has a convergent subseq

#### finite cases
For a linear $T:X\longrightarrow Y$,
- (**domain**) If $\dim X<\infty$, $T$ is compact
- (**range**) If $\|T\|<\infty$ and $\dim T(X)<\infty$, $T$ is compact


\page

# Hilbert & Inner-product space

We use the following notations.

X: Inner-product space (=pre-Hilbert space)

H: Hilbert space

## Definitions

- the **Fourier coefficients** of $x$ w.r.t orthonormal seq $(e_k)$ are $\langle x,e_k \rangle$
- **Orthogonal complement** $Y^\bot$ in $X$
- **Orthogonal projection** of $x$ on $Y$
- **Projection** of $H$ onto $Y$
- A projection is **idempotent**

Orthonormal
- An **orthonormal set** $M\sub X
- A **total** set
- **Hilbert dimension** (=**Orthogonal dimension**) of $H$


## Properties

Orthogonal
- 3.3-6: When Y is a closed subspace of $H$, $Y=Y^{\bot\bot}$
- 3.3-7: For a subset $M\neq \varnothing$, $spam M$ is dense in $H \iff M^\bot = \{0\}$
- 3.5-2 (a): In Hilbert, $\sum^\infty |\alpha_k|^2<\infty \Longrightarrow \sum^\infty \alpha_k e_k$ converges
- 3.5-2 (b): In Hilbert, if $x=\sum^\infty \alpha_k e_k$ converges, $x=\sum^\infty \langle x,e_k\rangle e_k$
- 3.5-2 (c): In Hilbert, for $x\in H$, $x=\sum^\infty \langle x,e_k\rangle e_k$


Orthonormal set
- For an orthonormal set, the **Pythagorean relation** holds, $\|x+y\|^2=\|x\|^2+\|y\|^2$ and $\|x_1+..+x_n\|^2=\|x_1\|^2+..+\|x_n\|^2$
- An orthonormal set is linearly independent in X
- For an orthonormal seq $(e_1,..)$ and $x\in span\{e_1,..e_n\}$, $x=\sum^n\langle x,e_k\rangle e_k$ in X
- **Bessel inequality**: For an orthonormal seq $(e_k)$ and $x\in X$, $\sum^\infty|\langle x, e_k\rangle |^2\le \|x\|^2$
- An orthonormal seq is obtained from a linearly independent seq by **Gram-Schmidt process** in X
- 3.5-3: $x\in X$ has at most countable nonzero $\langle x,e_k \rangle$ w.r.t an orthonormal family in $X$


total
- All total orthonormal sets in $H\neq\{0\}$ have the same cardinality (=Hilbert dimension)
- For a total $M\sub X$, $M^\bot=\{0\}$
- For a subset $M\sub H$, M is total $\iff M^\bot=\{0\}$
- An orthonormal set $M$ in $H$ is total $\iff$ $\forall x\in H$ the Parseval relation holds
- 3.6-1: every Hilbert $H\neq\{0\}$ has a total orthonormal set
- 3.6-4(a): If $H$ is separable, any orthonormal set is countable (finite or infinite)
- 3.6-4(b): If $H$ has a total orthonormal sequence, $H$ is separable
- All in one: $H$ is separable $\iff$ $H$ has a countable orthonormal basis $\iff$ every total orthonormal set is countable
- 3.6-5: H and H' are isomorphic $\iff$ their Hilbert dims are the same.

\page

# Functionals

## In Hilbert
- (3.8-1 **Riesz's**) A bounded linear functional $f$ has a representation $f(x)=\langle x,z\rangle$, $\|z\|=\|f\|$
- If $\langle x_0,x\rangle=0$ for all $x$, then $x_0$=0

#### Sesquilinear form
For $h: X\times Y\longrightarrow R$ or $C$
- $h(x_1+x_2,y) = h(x_1,y)+h(x_2,y)$
- $h(x,y_1+y_2) = h(x,y_1)+h(x,y_2)$
- $h(\alpha x, y)=\alpha h(x,y)$ (linear in the first arg)
- $h(x,\beta y)=\bar\beta h(x,y)$ (conjugate linear in the second)
- $\|h\| = \sup \frac{|h(x,y)|}{\|x\|\|y\|}$
- $|h(x,y)|\le \|h\|\|x\|\|y\|$

#### Bilinear

# Operators

## Convergence

#### Definitions

- **strongly convergent**: $\lim x_n = x$
- **weakly convergent**: $x_n\xrightarrow{w} x \iff \forall f\in X', \lim f(x_n)=f(x)$
- **weak\* convergence** of $(f_n)$: $f_n(x)\longrightarrow f(x) \forall x\in X$
- **uniformly operator convergent**: $T_n\longrightarrow T$ in $B(X,Y)$
- **strongly operator convergence**: $\forall x\in X, (T_nx)$ converges strongly in Y
- **weakly operator convergence**: $\forall x\in X, (T_nx)$ converges weakly in Y


#### Properties (normed space X)

- strongly convergence $\longrightarrow$ weakly convergence
- weak convergence $\longrightarrow$ strong convergence when $dim X<\infty$
- weak convergence $\iff (1) (\|x_n\|)$ is bounded and (2) $\forall f\in \text{total } M\sub X', f(x_n)\longrightarrow f(x)$
- the weak limit $x$ is unique
- weak convergence $\longrightarrow$ every subseq of $(x_n)$ weakly converges to $x$

#### Properties (normed X, Y)

- if $(T_n)$ strongly operator convergent with limit $T$, $T\in B(X,Y)$
- $\|T_n\|$ is bounded && $(T_n x)$ is Cauchy in $Y$ for all $x$ in a total subset $M\sub X$

## Self-adjoint operator

bounded, self-adjoint, linear $T, S:H\longrightarrow H$

spectrals

- $\sigma(T)$ is real
- $\sigma(T)$ lies on $[m,M]$ on a complex $H$
- eigenvectors for different eigenvalues are orthogonal
- $\lambda \in\rho(T) \iff \exists c>0, \forall x\in H, \|T_\lambda x\|\ge c\|x\|$
- $m=\inf_{\|x\|=1}\langle Tx,x\rangle$, $M=\sup_{\|x\|=1}\langle Tx,x\rangle$
- For $H\neq \{0\}$, $\{m,M\}\sub \sigma(T)$
- $\|T\|=max(|m|,|M|)=\sup_{\|x\|=1}|\langle Tx,x\rangle|$
- For a complex $H$, $\sigma_r(T)=\varnothing$




not in the book

- If $T_n \longrightarrow T$ and $(T_n)$ are self-adjoint, then $T$ is self-adjoint


## Positive operator

bounded, self-adjoint, linear $T, T_n, K:H\longrightarrow H$

- Positive operator != Positive element (see wikipedia)
- $T\ge 0 \iff \langle Tx,x\rangle\ge 0$
- On a complex $H$, If $T_1\le T_2\le .. \le K$ and $T_kK=KT_k$, $(T_n)$ is strongly operator convergent with limit $T$, $T$ is linear, bounded, self-adjoint, $T\le K$

bounded, self-adjoint, linear, positive $T, S:H\longrightarrow H$

- If $ST=TS$, $ST$ is positive

from problems
- $T:H\longrightarrow H$ is bounded, linear, $H$ is complex. $TT^*$ and $T^*T$ are self-adjoint and positive.

## Square Roots

- $T:H\longrightarrow H$ is bounded, self-adjoint, linear, positive on a complex $H$. A bounded self-adjoint linear $A$ is a square root of $T$ if $A^2=T$. The unique positive square root $A=T^{1/2}\ge 0$ exists.
- $T^{1/2}$ commutes with any bounded linear opeartor which commutes with $T$

\page

## Projection operator

$P_1, P_2$ are projections on $H$.

- A bounded linear $P:H\longrightarrow H$ is a **projection** $\iff$ $P^2=2$ and $P=P^*$
- For a projection $P$,
    - $\langle Px,x\rangle=\|Px\|^2$
    - $P\ge 0$
    - $\|P\|\le 1$, $\|P\|=1 if P(H)\neq\{0\}$
- (**product**) $P_1P_2$ is a projection $\iff P_1P_2=P_2P_1$ . $P_1P_2$ projects onto $P_1(H)\cap P_2(H)$
- (**sum**) $P_1+P_2$ is a projection $\iff $P_1(H)\bot P_2(H)$. $P_1+P_2$ projects onto $P_1(H) \bigoplus P_2(H)$
- (**difference**) $P_2-P_1$ is a projection $\iff $P_1(H)\in P_2(H)$. $P_2-P_1$ projects onto the orthogonal complement of $P_1(H)$ in $P_2(H)$
- Closed subspaces $A, B\sub H$ are orthogonal $\iff P_A P_B=0$
- if $(P_n)$ is a monotone increasing,
    - $P_nx\longrightarrow Px, \forall x$ and the limit $P$ is a projection
    - $P(H)=\overline{\cup^\infty P_n(H)}$
    - $N(P)=\cap^\infty N(P_n)$


#### partial order
These are equivalent.

- $P_2P_1=P_1P_2=P_1$
- $Y_1\sub Y_2$
- $N(P_1)\supset N(P_2)$
- $\|P_1x\|\le\|P_2x\|,\forall x\in H$
- $P_1\le P_2$

\page

