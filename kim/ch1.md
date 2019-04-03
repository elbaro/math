# Chapter 1. 확률분포

## Notes
- mgf=$M_X(t) = E(e^{tX})$, $-h<t<h$ for some $h>0$ (if $M_x(t)\in \R$)
- k-th moment = $m_k=E(X^k)$
- mgf exists $\Longrightarrow$ $m_k$ exists $\Longrightarrow$ $m_k=E(X^k)=M^{(k)}(0), M(t)=\sum_0^\infty \frac{E(X^k)}{k!}t^k$

---

- cgf=$C_X(t)=\log M_X(t)$
- r-th cumulant = $c_r=C^{(r)}(0)$
- cgf exists $\Longrightarrow$ $c_r$ exist? $\Longrightarrow$ $C(t)=\sum_{r=1}^\infty \frac{c_r(X)}{r!}t^r$

---


## Problems

1.20
- Scailing:
    $C_X(at)=log E(e^{(at)X})=log E(e^{t(aX)})=C_{aX}(t)$

    Hence $c_r(aX)=C_{aX}^{(r)}(0)=a^r C_X^{(r)}(at)=a^r c_r(X)$.
- Shift:
    $C_{X-a}(t)=log E(e^{t(X-a)})=log E_X(e^{tX}e^{-at})=log E(e^{tX})+ log e^{-at} = C_X(t)-at$
    The last term $-at$ goes away in $c_r(X-a)$ for $r\ge 2$. Hence for $r\ge 2, c_r(X-a)=c_r(X)$.

Combining these two properties, $c_r(\frac{X-\mu}{\sigma})=c_r(X-\mu)/\sigma^r=c_r(X)/\sigma^r$ for $r\ge 2$.

(TODO: The problem requires $r\ge 3$. Is it correct for $r=2$?)
