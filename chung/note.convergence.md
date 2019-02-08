# Note on convergence

$F_n, F$: cdf
$X_n, X$: random variables

## Relations
For more properties, see [Wikipedia](https://en.wikipedia.org/wiki/Convergence_of_random_variables).
![](https://wikimedia.org/api/rest_v1/media/math/render/svg/6fafe753cbea59eaa36703e0d40921f74cb50827)

## Convergence in dist.
$\forall x, F_n(x)\longrightarrow F(x)$
= converge in law
= converge weakly
= $F_n\xrightarrow d F$
= $F_n\rightsquigarrow F$

## Convergence in pr.
$\lim \Pr(|X_n-X|>\epsilon)=0$
= $\forall \epsilon>0, \delta>0, \exists N, \forall n>N, \lim \Pr(|X_n-X|<\epsilon)<\delta$

= $F_n\xrightarrow p F$
= $\operatorname{plim}_{n\longrightarrow\infty} X_n = X$

## Convergence in mean
$\lim E(|X_n-X|^r)=0 (r\ge 1)$
= $X_n\xrightarrow{L^r} X$

This implies
= $\lim E(|X_n|^r)=E(|X|^r)$


## Almost surely convergence (a.s.)
$\Pr(\lim_n X_n = X)=1$
= almost everywhere (a.e.)
= converge strongly
= with probability 1
= $X_n\xrightarrow{a.s.} X$
= $X_n\xrightarrow{a.e.} X$


## Sure convergence
$\forall \omega, X_n(\omega)\longrightarrow X(\omega)$
= everywhere
= pointwise
