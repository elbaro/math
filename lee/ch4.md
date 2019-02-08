# 4. Connectedness and Compactness

## Connectedness

Ex 4.3. If $X$ is empty, the statement is true. Otherwise choose any $x\in X$ and let $c$ the equivalence class of $x$. Then $c$ is open and the union of all other equivalence classes is open, and these two subsets are the partition of $X$. If $c\neq X$, then $X$ is disconnected, which contradicts the assumption. Therefore $c=X$.

Ex 4.4. Suppose $X$ is disconnected, $X=A\cup B$ for two disjoint open sets $A, B$. Define a map $f$ that $f(A)=0, f(B)=1$. Then $f$ is continuous and non-constant. Conversely, if there is $f$ that is nonconstant and continuous from $X$ to the discrete space, then by Proposition 4.2, $X$ is empty or disconnected. If $X$ is empty, $f$ is constant. Hence $X$ is disconnected.

Ex 4.5. (Disjoint union of spaces here refers to one in Chapter 3.) Suppose $X$ is disconnected by two open subsets. Let the subspaces for these open subsets $A$ and $B$. We will prove $X$ is homeomorphic to a disjoint union topology $A^*\cup B^*$ by a mapping $f, \forall a\in A,f(a)=(a,A),\forall b\in B,f(b)=(b,B)$. $f$ is continuous because for any open subset $E\sub A^*\cup B^*, E=(E\cap A^*)\cup (E\cap B^*), f^{-1}(E)=f^{-1}(E\cap A^*)\cup f^{-1}(E\cap B^*)$, and $f^{-1}(E\cap A^*), f^{-1}(E\cap B^*)$ are open by definition of disjoint union topology, hence $f^{-1}(E)$ is open. $f^{-1}$ is continuous because for any open subset $E\sub X, f(E)=f(E\cap A)\cup f(E\y cap B)$, and $f(E\cap A)$ is open in $A^*$, $f(E\cap B)$ is open in $B^*$, $f(E)$ is open.

Conversely, if $X$ is homeomorphic to a disjoint union $\cup X_k$ with at least two spaces, then by Proposition 4.2, $X$ is not a nonempty connected space. $X$ is not empty, hence $X$ is disconnected.

Ex 4.10.

Ex 4.14.
(a) Let $f:X\longrightarrow f(X)$ is continuous, and $X$ is path-connected. Then for any two points $a,b\in f(X)$, there is a path $g$ from $f^{-1}(a)$ to $f^{-1}(b)$ in $X$. Then $f\circ g:I\longrightarrow f(X)$ is continuous and from $a$ to $b$. hence a path. Therefore $f(X)$ is path-connected.
(b) Let $p$ a point in common. Then for any two points $a,b\in \cup B_\alpha$, there exists $B_a$ that contains $a$ and $B_b$ that contains $b$. $B_a$ has a path $f$ from $a$ to $p$, and $B_b$ has a path $g$ from $p$ to $b$. Define $f':[0,0.5]\longrightarrow \R,f'(x)=f(x*2), g':[0.5,1]\longrightarrow \R, g'(x)=f(x*2-1)$. Both $f', g'$ are continous. We can use the gluing lemma (pasting lemma) to define $h:[0,1]\longrightarrow \R$ from $f'$ and $g'$. Then $h$ is a path from $a$ to $b$. Hence cup B_\alpha$ is path-connected.
(c) Let $S_1,\dots,S_n$ path-connected spaces and $S=\prod S_n$. For any two points $a,b\in S$, $a=(a_1,\dots,a_n),b=(b_1,\dots,b_n)$. For each index $k\in[1,n]$, there exists a path $f_k$ from $a_k$ to $b_k$ in $S_k$. Define $f:I\rightarrow S, f(x)=(f_1(x),\dots,f_n(x))$. Then by characteristic property of the product topology, $f$ is continous from that each $f_k$ is continous. Hence $f$ is a path from $a$ to $b$ in $S$, and $S$ is path-connected.
(d) A quotient map is continuous, hence by (a) every quotient space of a path-connected space is path-connected.

Ex 4.22.
(a) Suppose two path components of $X$ are not disjoint. They have a common point, so the union of two is also path-connected, which contradicts that path components were maximal. Therefore path components are all disjoint, and form a partition of $X$.
(b) A path component is connected, so by Proposition 4.20 (a), the path component is in a single component. Path components are disjoint and each element belongs to one path component, hence each component is a disjoint union of path components.
(c) For an nonempty path-connected subset $E$ of $X$, $E$, there exists a path component $P$ that shares a point with $E$. Then $E\cup P$ is also path-connected. Since $P$ is a maximal path-connected subset, $E\cup P\sub P\Longrightarrow E\sub P$.

Ex 4.24. Let $M$ a manifold and consider $p\in M$. Since $M$ is locally Euclidean, $p$ has a neighborhood $U$ that is homeomorphic to an open ball in $R^n$ by a homeomorphism $\phi$. An open ball in $R^n$ is path-connected. For any neighborhood $V$ of $p$, $\phi(U\cap V)$ is open and contains $\phi(p)$. Since $\phi(U)$ is locally path-connected, $\phi(U\cap V)$ has a path-connected subset $W$. $\phi^{-1}(W)$ is path-connected and a subset of $U\cap V$. We showed any neighborhood of $p$ has a path-connected subset, hence $M$ is locally path-connected. Since a path-connected subset is connected subset, $M$ is also locally connected.

## Compactness

Ex 4.28. Suppose $A$ is compact. For any open cover $\cup_\alpha E_\alpha$ of $A$ by open sets of $X$, $\cup_\alpha (E_\alpha \cap A)$ is an open cover of $A$ by open sets in $A$. Since $A$ is compact, it has a finite subcover $\cup_1^N (E_{\alpha_n}\cap A)$. For every open set $E$ in $A$, there exists an open set $F$ in $X$ such that $F\cap A=E$. Define $\phi(E)=F$. Then $A=\cup_1^n (E_{\alpha_n}\cap A)\Longrightarrow A\sub\cup_1^n \phi(E_{\alpha_n}\cap A)$, where the last union is a finite subcover by open sets in $X$. This proves the forward direction of the lemma.
Conversely suppose every open cover of $A$ by open sets in $X$ has a finite subcover by open sets in $X$. Then for any open cover $\cup E_\alpha$ of $A$ by open sets in $A$, $\cup_\alpha \phi(E_\alpha)$ is an open cover of $A$ by open sets in $X$, hence it has a finite subcover $\cup_1^N \phi(E_{\alpha_n})$. Then $\cup_1^N (\phi(E_{\alpha_n})\cap A)$ is a finite cover of $A$ by open sets in $A$. Hence $A$ is compact.

Ex 4.29. For compact subsets $A_1,\dots,A_n$, consider an open cover $\cup E_i$ of $\cup A_k$ by open sets of $X$. For each $k$, $A_k\cap (\cup E_i)=\cup (A_k\cap E_i)=A_k$, and $\cup(A_k\cap E_i)$ is an open cover of $A_k$ because $A_k\cap E_i$ is open in $A_k$. Since $A_k$ is compact, there is a finite subcover $\cup_n B_{kn}$ of $A_k$. Collecting all finite subcovers for each $k$, $\cup_k \cup_n B_{kn}=\cup A_k$, and $\cup B_{kn}$ is a finite subcover of $\cup A_k$.

Ex 4.37.

Ex 4.38.

Ex 4.49.
- Theorem 4.46: $\R^n$ is compact, and by Heine-Borel,

## Local Compactness

## Paracompactness

## Proper Maps

## Problems
