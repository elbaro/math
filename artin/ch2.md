# Chapter 2. Groups

## Checklist
- Group
- Group's order
- Subgroup
- Relation between left inverse / right inverse
- Cyclic Group
- Coset


## Section 1. Laws of Composition

1.1. $ab=a$, $(ab)c=ac=a$, $a(bc)=ab=a$.

1.2. (Note: these properties are not true with non-associative operations.)
    - $la=ar=1, (lar)=l=r, ra=ar=1, a^{-1}=r$.
    - an inverse is unique, if not ($b\ne c$), $ab=1, ac=1, cab=c(ab)=c=(ca)b=b, b=c$.
    - $(ab)(b^{-1}a^{-1})=aa^{-1}=1, \therefore (ab)^{-1}=b^{-1}a^{-1}$.
    - A counter-example is Exercise 1.3.

1.3. For right inverse, $ss^{-1}(n)=n$, $s^{-1}(n)=n-1$ For left inverse, $s^{-1}s(n) = s^{-1}(n+1)=n$, however $s^{-1}(1)$ is unspecified, hence infinitely many left ivnerses.


## Section 2. Groups and Subgroups

2.1. skip

2.2. The subset is closed under inverse, contains 1 because 1 is invertible, and if the subset has $a, b$, $ab$ has the inverse $b^{-1}a^{-1}$, hence $ab$ is the element of the subset as well. Therefore the subset is a subgroup.

2.3. .
    (a) $y=x^{-1}w^{-1}z$
    (b) $x(yz)=(yz)x=1$. $yxz$ may be be $1$, since it is possible $xy\ne yx$.

2.4. .
    (a) yes
    (b) yes
    (c) no, $H$ is not closed under inverse.
    (d) yes
    (e) no, $I$ is not in $H$.

2.5. If $G$ has an identity $I_1$ and $H$ has an identity $I_2$, $I_1 I_2 = I_1 = I_2$.

2.6. $G^\circle$ is still assosiative, has the same identity, same inverse. Hence $G$ is a group.


## Section 3. Subgroups of the Additive Group of Integers

3.1. skip

3.2. $a+b=p, gcd(a,b)=gcd(a,p-a)=gcd(a,p)=1$ because $a$ and $p$ are coprime.

3.3. .
    (a) $gcd(a_1,a_2,..a_n)=gcd(gcd(a_1,..a_{n-1}, a_n)$, then a linear combination of linear combinations is a linear combination.
    (b) if $gcd(a_1/d, a_2/d, .. a_n/d) = d'$, then $d*d'$ is a linear combination of $a_1, .., a_n$, and $d*d'$ divides $d$, so $d'=1$.


## Section 4. Cyclic Groups

4.1. $a^7=1, a^3b = ba^3, ba^3b^{-1}=a^3$, squaring the both sides, $ba^6b^{-1}=a^6, ba^{-1}b^{-1}=a^{-1}$, then $ab=ba$.

4.2. .
    (a) skip (use $e^{in/(2\pi)}$)
    (b) if $n$ is even, the sum of power is 0 (modular n), thus the product $1$.  if $n$ is odd, all terms except $1$ cancel out, and the product is $1$.

4.3. $(ab)^k=1 \iff a((ba)^k)a^{-1}=1 \iff (ba)^k=1$, hence the order of two are the same.

4.4. Any group with order greater than 1 has a trivial proper subgroup ${1}$ and it is the smallest group. Only ${1}$ has no proper subgroup.

4.5. If a subgroup is a trivial ${1}$, it is cyclic. Otherwise the subgroup of a group $<x>$ consists of $x^k$ and let $m$ be the smallest positive $k$. For any element of the subgroup $x^l$, $l=mq+r$ by the division theorem. Since the subgroup has $x^{mq}$ and $x^{mq+r}$, it also has $x^{-mq}$ (inverse) and $x^r$. If $r$ is not $0$, it contradicts that $m$ is the smallest positive $k$. Hence $r$ is zero, $l$ is a multiple of $m$. This proves the subgroup is a cyclic, $<x^m>$.

4.6. .
    (a) skip
    (b) $x^k$ generates a cyclic group $<x>$ of order $n$ if and only if $gcd(k,n)=1$. The answer is $\phi(n)$, which is the euler phi function.

4.7. $H$ is closed under the composition because $xx=1, yy=1, (xy)(xy)=1$, $xy$ is in $H$, $yx=y^{-1} x^{-1} = (xy)^{-1} = xy$ is in $H$, $xxy=xy$, $yxy=x^{-1}=x, xyx=y^{-1}=y, xyy=x$. $H$ also has $1$ and all inverses (the inverse of an element is itself). Hence $H$ is a subgroup. It is of order $4$ because $x, y, xy$ are all different. If $x=y$, $xy=1$, so the order of $xy$ is $1$, contradicts. If $x=xy$, then $y$ is an identity, $y=1$, the order of $y$ is $2$, contradicts. Therefore they are all different.

4.8. .
    (a) (Type 2) can be represented as (Type 1) and (Type 3). Suppose two rows are $(r1,r2)$. Then $(r1,r2)\Rightarrow (r1+r2,r2)\Rightarrow (r1+r2,-r1)\Rightarrow (r1+r2,r1)\Rightarrow (r2,r1)$. Therefore only (Type1) and (Type3) are enough to generate $GL_n(\R)$.
    (b) Without (Type3) we can make a matrix similar to a row echelon one, except each row's leading non-zero element is not 1. Any product of (Type 1) matrices has the determinant $1$ hence it is in $SL_n(\R)$. Any element in $SL_n(\R)$ has the determinant $1$, and can be reduced to an upper triangle matrix using only (Type 1). The first $n-1$ diagonal elements also can be reduced to 1 using (Type 1). The last diagonal element is automatically $1$ since the product of diagonal elements is the determinant. Hence it is possible to reduce any element of $SL_n(\R)$ to $I$, and taking the inverse of a sequence of (Type 1) operations used, we have a product of (Type 1) which is equal to the element. Therefore (Type 1) operations exactly generates $SL_n(\R)$.

4.9. skip

4.10.

4.11. .
    (a)
    (b)



## Section 5. Homomorphisms

5.5

## Section 6. Isomorphisms

6.1


6.2

## Section 7. Equivalence Relations and Partitions


## Section 8. Cosets

## Section 9. Modular Arithmetic


## Section 10. The Correspondence Theorem

## Section 11. Product Groups

## Section 12. Quotient Groups

## Miscellaneous Problems

M.1.
