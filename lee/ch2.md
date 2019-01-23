# 2. Topological Spaces

$\gdef\Int{\operatorname{Int}}$
$\gdef\Ext{\operatorname{Ext}}$

## Note
- $A = \Int A+ \partial A + \Ext A \\
  = (\text{limit point} + \text{isolated point}) + \Ext A$
    where $+$ is a disjoint partition op
- boundary -> limit point, not isolated
- isolated -> int


## Topologies

- Ex 2.2
It can be easily seen that all examples satisfy (i)~(iii) in page 20.

- Ex 2.4
(a) For "only if", any open ball w.r.t $d$ is an open set w.r.t $d'$, and any open set contains an open ball, hence there exists $r_1$. The same for $r_2$. For "if", Suppose a set $A$ is open in $(M,d)$. Any point $x\in A$ is internal point in $(M,d)$ and there exists $r$ such that $B_r^{(d)}(x)\sub A$. Since $B_{r_1}^{(d')}(x)\sub A$, $x$ is an internal point of $A$ in $(M,d')$. Hence $A$ is open in $(M,d')$. Conversely, any open set in $(M,d')$ is open in $(M,d)$. Therefore two topologies are the same.
(b) $B_r^{(d)}=B_{cr}^{(d')}$, so their open sets are the same, and generated topologies are the same.
(c) $d'\le d\le nd'$. It can be proved using (a) that $d$ and $d'$ generate the same topology.
(d) With the discrete metric, $B_{0.5}(x)=\{x\}$. These generate all possible subsets of $X$.
(e) With the Euclidean metric, $B_{0.5}(x)=\{x\}$. These generate all possible subsets of $\Z$.

- Ex 2.5
(1) $\varnothing \sub Y, Y \sub Y$.
(2) The set is closed under finite intersection because they were closed in $X$.
(3) The set is closed under any union of arbitrarily many elements because they were closed in $X$.

- Ex 2.6
(1) All topologies have $\varnothing$ and $X$, hence ${\varnothing,X}\sub \mathscr T$.
(2) $\mathscr T$ is closed under finite intersection, since its elements were the elements of $T_{\alpha_0}$ for some $\alpha_0$, and their intersection existed in $T_{\alpha_0}$.
(3) The same as (2).


- Ex 2.9
TODO:


- Ex 2.10
By Proposition 2.8, a boundary point is a limit point. If a set contains all of its limit points, the set contains all boundary points, hence closed. Now suppose a set is closed. Any limit point of the set $A$ is in $\Int A$, $\Ext A$, or $\partial A$. The limit points in $\Int A$ are obviously in $A$. The limit points which are boundary points are in $A$ because $A$ is closed. $\Ext A$ cannot have a limit point because a point $x$ in $\Ext A$ has a neighborhood in $X\setminus A$, and the neighborhood has no point of $A$ other than $x$, so $x$ is not a limit point. Therefore $A$ contains all of its limit points.

- Ex 2.11
Suppose $A$ is dense in $X$ and there is an non-empty open subset $B$ of $X$ that contains no point of $A$. $B$ has at least one element, say $b$. Then $B$ is a neighborhood of $b$ and $B\sub X\setminus A$. By Proposition 2.8 (b), $b$ is in $\Ext A$. However, $\Ext A$ = $X\setminus \overline A = \varnothing$, contradicts. Hence the statement is true.

Conversely, suppose every non-empty open subset of $X$ contains a point of $A$. Then by definition any point of $X$ is a limit point of $A$. Since $\overline A$ is closed, using Exercise 2.10, $\overline A$ contains all of its limit points, $X$. Hence $\overline A=X$.

## Convergence and Continuity

- Ex 2.12
An open ball is a neighborhood, so the definition in topology space implies that a sequence converges if given $\epsilon>0$ its tail is contained in some open ball of size $\epsilon$. Conversely any non-empty neighborhood of a point $x$ has an open ball centered at $x$, and since the definition in metric space implies the sequence tail is contained in the open ball, it is contained in the neighborhood as well.

- Ex 2.13
If a sequence is eventually constant, the sequence after some point is in a neighborhood of the constant, so it is convergent. If a sequence converges to $x$ in a discrete topological space, $\{x\}\in \mathscr T$, so there exists $N$ such that $\forall n>N, x_n\in \{x\}$. Hence the sequence is eventually constant.

- Ex 2.14
If $x\in A$, then $x\in \overline A$. If not, $x$ is either in $\partial A$ or $\Ext A$. Any sequence in $A$ cannot converge to a point of $\Ext A$ because there is a neighborhood of the point in $\Ext A$ that has no point of $A$. Therefore $x$ is in $\partial A$, hence $x\in \overline A$.

- Ex 2.16
From Exercise A.4 (e), $f^{-1}(E^c)=f^{-1}(Y\setminus E)=f^{-1}(Y)\setminus f^{-1}(E)=f^{-1}(Y)\cap (f^{-1}(E))^c=X\cap (f^{-1}(E))^c$. If $f$ is continuous and $E^c$ is closed in $Y$, $E$ is open, $f^{-1}(E)$ is open, $(f^{-1}(E))^c$ is closed, and $X$ is closed, so their intersection $X\cap (f^{-1}(E))^c=f^{-1}(E^c)$ is closed. With $E^c=F$, we showed that $f^{-1}(F)$ is closed for any closed $F$. Conversely, if the preimage $f^{-1}(E^c)$ of any closed set $E^c$ in $Y$ is closed in $X$, $f^{-1}(E)$ is open, hence $f$ is continuous.

- Ex 2.18
(a) A constant map is continuous because the preimage is either $\varnothing$ or $X$.
(b) The identity map is continuous because the preimage of an open set $E$ in $X$ is $X$.
(c) Let $g$ be a restriction of $f$ to an open subset $Z$ of $X$. The preimage $f^{-1}(E)$ of an open set $E$ is open, and $g^{-1}(E)=f^{-1}\cap Z$ is the intersection of two open sets, hence open. Therefore $g$ is continuous.


- Ex 2.20
The continuity of a composotion of two continuous mapping implies the equivalence relation.

- Ex 2.21
if $f$ is homeomorphism, for any $U\in\mathscr T_2, f^{-1}(U)\in \mathscr T_1$ because $f$ is continuous. The converse is true in the same way. Therefore $f(\mathscr T_1) = \mathscr T_2$.
Now conversely if for any $U\in\mathscr T_1$ it is true that $f(U)\in\mathscr T_2$, then $f^{-1}$ is continuous. Symmetrically we can show $f$ is continuous. Therefore $f$ is homeomorphism.


- Ex 2.22
Since $f^{-1}$ is continuous and $U$ is open, $f(U)$ is open. A restriction of continuous $f$ to $U$ is continuous, and at the same time $f^{-1}$ is restricted to $f(U)$ which is open, hence both $f|_U$ and $f|_U^{-1}$ are continuous, and is homeomorphism $U\longrightarrow f(U)$.

- Ex 2.23
TODO

- Ex 2.27
TODO

- Ex 2.28
TODO

- Ex 2.29
(a)->(b): Since $f^{-1}$ is continuous, $f$ maps any open set in $x$ to an open set in $Y$.
(b)->(c): For a closed set $E\sub X$, $f(E^c)$ is open. Since $f$ is bijective, $f(E^c)=f(E)^c$. Hence $f(E)$ is closed.
(b)->(a): Since (b) imlies that $f^{-1}$ is continuous, and $f$ is continuous by asumption, $f$ is homeomorphic.

- Ex 2.32
(a) Already proved in Exercise 2.22.
(b★) Using Proposition 2.19, local homeomorphism implies the continuity. To show $f$ is open, consider any open set $E$. For each $x\in E$, we have an open set $U_x$ such that $f|_{U_x}$ is homeomorphism, and since $U_x\cap E$ is open, $f|_{U_x}(U_x\cap E)$ is open. Then $f(E)=\cup_{x\in E}f(U_x\cap E)$ is the union of open sets, which is open. Hence $f$ is open. [link](https://math.stackexchange.com/questions/1826878/show-that-every-local-homeomorphism-is-continuous-and-open-therefore-bijective-l)
(c) By Exercise 2.29, if $f$ is bijective, continuous and open (from (b)) then $f$ is homeomorphism.

## Hausdorff Spaces

- Ex 2.33
Any sequence converges to any element $y\in Y$ because the only neighborhood of $y$ is $Y$ in the trivial topology and the sequence is in this neighborhood.

- Ex 2.35 (★)
For two distinct points $p,q\in X$, there exists $f$ such that $f^{-1}(0)=\{p\}$. Let $\epsilon=f(q)/2$. Wlog, assume $\epsilon>0$. Since $\epsilon\neq 0$, two intervals $(-\epsilon,\epsilon)$ and $(\epsilon, 3\epsilon)$ are open and disjoint, and so are their mapping by $f^{-1}$. Since $p\in f^{-1}(-\epsilon,\epsilon), q\in f^{-1}(\epsilon,3\epsilon)$, these two are disjoint neighborhoods of $p$ and $q$. Hence $X$ is Hausdorff.

- Ex 2.38
The discrete topology is obviously Hausdorff topology. A Hausdorff topology on a finite set has $\{p\}$ for all $p$, so these generate all possible subsets, which is the discrete topology.

## Bases and Countability

- Ex 2.40
If $U$ is open, it is the union of some collection of elements of $\mathscr B$. Therefore each element of $U$ belongs to some $B_\alpha\sub U$. Conversely, if such $B$ exists for each $p\in U$, denote $B$ as $B_p$. Then $U=\cup B_p$, hence $U$ is open.

- Ex 2.42
(a) Each point of $C_s(x)$ is internal so $C_s(x)$ is open. For an open ball $B$, it contains an open ball $V_{r_x}(x)$ for each element $x$. Then $V_{r_x}(x)$ contains an open cube $C(x)$ which includes $x$. Then $\cup_{x\in B} C(x) = B$. Since open cubes can generate open balls, open cubes are a basis for $R^n$.

(b) Similar to (a), each point $x$ of an open ball $B$ has an open ball $V_x$ in $B$, and $V_x$ contains a 'rational ball' $R_x$ that includes $x$. Therefore $\cup_{x\in B}R_x=B$. Since rational balls generate open balls, $\mathscr B_2$ is a basis for $R^n$.

- Ex 2.45
A topology should have $X$ itself as an open set. If (i) is false, the basis cannot generate $X$. So (i) is true. For (ii), given $B_1,B_2\in \mathscr B$, their intersection is open, so there should exist a subset of $B_1\cap B_2$ in $\mathscr B$, otherwise it cannot generate $B_1\cap B_2$.

- Ex 2.51
- A second countable space $X$ has a countable basis $(B_n)$. Pick any element $x_n$ from each $B_n$, and denote the set as $D$. $D$ is clearly countable. From Exercise 2.11, $D$ is dense because every non-empty open subset of $X$ is an union of $(B_{i_n})$ and contains a point of $D$, for example, $x_{i_1}$. [link](https://topospaces.subwiki.org/wiki/Second-countable_implies_separable)

## Manifolds

- Ex 2.54
If a topological space is a 0-manifold, for any element $x$, it has a neighborhood homeomorphic to $R^0={0}$. So the neighborhood of $x$ is $\{x\}$. Since the topology has the smallest unit of open sets, they generate the discrete topology. A manifold is second countable, hence countable.

If a set $E$ is countable discrete space, it is a Hausdorff space and it has a basis that consists of single-element sets. This basis is countable, so $E$ is second-countable. For a point $x\in E$, it has a neighborhood $\{x\}$ which is homeomorphic to $R^0$. Hence $E$ is a 0-manifold.


## Problems
2-1.
(a) $\{\varnothing,X\}\sub \mathscr T_1$, $X\setminus(\cup U_k)\sub X\setminus U_1$ is finite, $X\setminus (\cap^n U_k)=\cup_1^n(X\setminus U_k)$ is finite, hence $\mathscr T_1$ is a topology.

(b) $\{\varnothing,X\}\sub \mathscr T_2$, $X\setminus(\cup U_k)\sub X\setminus U_1$ is countable, $X\setminus (\cap^n U_k)=\cup_1^n(X\setminus U_k)$ is countable, hence $\mathscr T_2$ is a topology.

(c) $\{\varnothing,X\}\sub \mathscr T_3$, $p\in\cup U_k$, $p\in\cap U_k$, hence $\mathscr T_3$ is a topology.

(d) $\{\varnothing,X\}\sub \mathscr T_4$, $p\notin\cup U_k$, $p\notin\cap U_k$, hence $\mathscr T_4$ is a topology.

(e) $\{\varnothing,X\}\sub \mathscr T_5$ because $X$ is infinite. $X\setminus(\cap^n U_k)\supset X\setminus U_1$ is infinite, but $X\setminus (\cup U_k)=\cap(X\setminus U_k)$ may be finite. An example is $X=\Z$ and $U_1=\{\text{even integers}\}, U_2=\{\text{odd integers}\}$, then $U_1,U_2\in \mathscr T_5$ but $X\setminus(U_1\cap U_2)=\varnothing$.

2-2.
- $\{ \text{discrete topology} \}$, $\{\text{trivial topology}\}$, $\{ \varnothing, \{1\}, X \}$, $\{ \varnothing, \{1\}, \{2,3\}, X \}$, $\{ \varnothing, \{1\}, \{1,2\}, X \}$, $\{ \varnothing, \{1\}, \{1,2\}, \{1,3\}, X \}$, $\{ \varnothing, \{1\}, \{1,2\}, \{2,3\}, X \}$, $\{ \varnothing, \{1\}, \{1,2\}, \{1,3\}, \{2,3\}, X \}$, $\{ \varnothing, \{1\}, \{2\}, \{1,2\}, X \}$, $\{ \varnothing, \{1\}, \{2\}, \{1,2\}, \{1,3\}, X \}$.

2-3.
(a) Taking the complement on both sides, the equation reduces to $\Ext (X\setminus B)=\Int B$, which is true by definition because LHS represents the points with some neighborhood in $(X\setminus B)^c=X$, and RHS represents the same.
(b) $\Int (X\setminus B) = X\setminus \overline B=\Ext B$, which is the same as (a) with replacing $B$ with $X\setminus B$.

2-4.
(a) LHS is the minimal closed set including $\cap A$. RHS is closed and includes $\cap A$. Hence LHS$\sub$RHS.
(b) Any element $x$ of RHS belongs to some $\overline {A_\alpha}$. Since $x \in \overline {A_\alpha} \sub \overline{\cup A}$, RHS is a subset of LHS.
(c) Any point $x$ of LHS has a neighborhood $V$ in $\cap A_\alpha$. Then $\forall\alpha,  V\sub A_\alpha$, hence $x$ is in $\Int A_\alpha$ for all $\alpha$, and $x$ is an element of RHS.
(d) Any point $x$ of RHS has a neighborhood $V$ in some $A_0$. Since $V\sub \cup A_\alpha$, $x$ has a neighborhood in $\cup A_\alpha$, and $x\in \Int(\cup A_\alpha)$.

equality:

(a) An example with strict inequality is $A_1=\mathbb Q, A_2=\R\setminus\mathbb Q$.

(b) We show a boundary point $p$ of $\cup A$ is in $\cup\overline A$. Since $\mathscr A$ is finite, the smallest neighborhood $V$ of $p$ exists, and is the intersection of all neighborhoods of $p$. $V$ has a point $q$ other than $p$ in $A_i$ for some $i$. Then $p\in \overline A_i$ because any neighborhood of $p$ contains $V$ and $V$ contains $q$, so $p$ is a limit point of $A_i$. We proved $\partial (\cup A)\sub \cup\overline A$, and clearly $\Int (\cup A ) \sub \cup \overline A$, hence $\overline{\cup A}\sub \cup\overline A$.

(c) Any point of $\cap \Int A$ has a neighborhood in each $A_i$. The finite intersection $V$ of them is also a neighborhood. $\forall i, V\sub A_i\Longrightarrow V\sub \cap A$. Hence the point is interior of $\cap A$.

(d) An example with strict inequality is that $A$ is indexed by a real number $\alpha$ and $A_\alpha=\{\alpha\}$, then $\Int(\cup A_\alpha)=\Int \R = \R \supset \cup \varnothing$.

2-5.

2-6.
(a) Suppose $f$ is continuous. $A\sub f^{-1}(f(A))\sub f^{-1}(\overline{f(A)})$ and $f^{-1}(\overline{f(A)})$ is closed. Since $\overline A$ is the smallest closed set containing $A$, we have $\overline A\sub f^{-1}(\overline{f(A)})\Longrightarrow f(\overline A)\sub \overline{f(A)}$. Conversely suppose $f(\overline A)\sub \overline{f(A)}$ for all $A\sub X$.
(b)
(c)
(d)

2-7. Suppose a neighborhood $V$ of $p$ contains finitely many points of $A$. Since $p$ is a limit point of $A$, $V$ has another point $q\in A, q\neq p$. $X$ is Hausdorff so there are two disjoint neighborhoods $V_p, V_q$ such that $p\in V_p, q\in V_q$. Then $V\cap V_p$ is also a neighborhood of $p$ and does not contain $q$. If we repeat the above with $V\cap V_p$ as new $V$, then at each step the size of $V\cap A$ decreases by at least one, and since $V\cap A$ is finite by assumption, the process cannot continue, which contradicts. Therefore $V\cap A$ is infinite.


2-25.
