# 1. Measures ($R^d$)

## Definitions

- A **cube**, **rectangle**
- The **exterior measure** of a set E in $R^d$

## Measurable sets

- Open sets
- Closed sets
- $\sigma$-algebra

## Measure approximation

For a measurable set E in $R^d$,

1. $\exists$ an open set $O\supset E$ s.t. $m(O-E)\le \epsilon$
2. $\exists$ an closed set $F\subset E$ s.t. $m(E-F)\le \epsilon$

For a finite $m(E)$,

1. $\exists$ a compact set $K\subset E$ s.t. $m(E-K)\le \epsilon$
2. $\exists$ a finite union $F=\cup^N Q_j$ s.t. $m(E\triangle F)\le \epsilon$

## Measurable functions

- A simple function
- A step function
- A continuous function on $R^d$
- A composition (continuous) $\circ$ (measurable and finite-valued)
- sup, inf, limsup, liminf of a sequence of mesaruable functions

## Mesaurable function approximation

- If $f$ is a non-negative measurable on $R^d$, there is an increasing seq of non-negative simple functions, pointwisely converging to $f$.

- If $f$ is measurable on $R^d$, there is a sequence of simple functions s.t. absolutely increasing and pointwisely converging to $f$.

## Littlewoods

- Egorov: ..
- Lusin: a mesurable $f$ can be restricted so it is continuous

\page

# 2. Integration

## Definition

- A Lebesgue integral of simple functions
- A Lebesgue integral of bounded functions supported on a set of finitei measure
- A Lebesgue integral of non-negative functions
- A Lebesgue integral of integrable functionos
- $f$ is **supported** on a set $E$
- **$L^1$**

## Properties

- **Fatou**
- **Fubini**
- **Tonelli**

\page

# 3. Differentiation

## Definitions

- A **curve**
- A curve is **rectifiable**
- A **length** of a curve
- A function F is of **bounded variation**
- The **total variation** of a function f on [a,b]
- The **positive variation** of a function F on [a,x]
- The **negative variation** of a function F on [a,x]
- **Cantor-Lebesgue function**
- A function F on [a,b] is **absolutely continuous**
- A **Vitali covering** of a set E
- The **arc-length parametrization** of a curve
- A curve is **simple**
- A curve is **closed simple**
- A curve is **quasi-simiple**
- A set K has **Minkowski content**
- The **isoperimetric inequality**
- **Dini numbers**
- **Jump function** for $F$


## Properties
Bounded Variation
- 3.1: A curve $(x(t),y(t))$ is rectifiable $\iff$ $x(t)$ and $y(t)$ are of bounded variation
- 3.2: If $F$ is real, bounded variation on $[a,b]$, then $F(x)-F(a)=P_F(a,x)-N_F(a,x)$
- 3.3: $F$ is of bounded variation $\iff$ $F$ is the diff of two increrasing bounded fuctions
- 3.4: $F$ is of bounded variation on $[a,b]$, F is differentiable almost everywhere in $[a,b]$

F and F'
- 3.5: Rising-sun lemma (by F. Riesz)
- 3.7: $F$ is increasing, continuous $\Longrightarrow$ $F'$ exists a.e.
- 3.7: .. if $F'$ is measurable, non-negative, then integral of $F' \le F(b)-F(a)$
- 3.9: If $E$ is of finite measure and \$B\$ is a Vitali covering, then for any $\delta>0$ there are finitely many balls $B_1, .. B_N$ in $B$ that are (1) disjoint and (2) $\sum m(B_i) \ge m(E)-\delta$
- 3.10: By 3.9, we can arrange so $m(E-\cup^N B_i)\le 2\delta$
- 3.11 (a): If $F$ is absolutely continuous on $[a,b]$, then $F'$ exists a.e. and is integrable. Also $F(x)-F(a)=\int_a^x F'(y)dy$
- 3.11 (b): If $f$ is integrable on $[a,b]$ then $F=\int_a^x f(y)dy$, absolutely continuous and $F'(x)=f(x)$ a.e.

Jump functions and Discontinuities
- 3.12: A bounded increasing $F$ on $[a,b]$ has at most countable many discontinuities
- 3.13: If $F$ is increasing and bounded on $[a,b]$, then (1) J(x) is discontinuous precisely at the points ${x_n}$ and has a jump at $x_n$ equal to that of $F$ (ii) F(x)-J(x) is increasing , continuous
- 3.14: $J'(x)$ exists and vanishes a.e.

\page

# 4. Hilbert Spaces

Many theorems in Ch4 are included in the general properties of Hilbert spaces, and omitted here. Refer to Kreyszig's <Functional Analysis>.

## Definitions

- **Hilbert space**
- Two elements are **orthogonal** or **perpendicular**
- **Bessel's inequality**
- **Parseval's identity**
- A mapping H->H' is **unitary**
- H and H' are **unitarily equivalent** or **unitarily isomorphic**
- **pre-Hilbert space**
- **n-th Fourier coefficient** of $f\in L^1([-\pi,\pi])$

## Properties

- $L^2(R^d)$, a collection of **square integrable functions** on R^d is Hilbert
- $L^2(R^d)$ is **separable**
