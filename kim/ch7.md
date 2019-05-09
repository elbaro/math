# 7장. 검정

## Notes
7.1: $P(기긱역|H_0)\le\alpha$ 으로 유의수준 결정
- 랜덤화 검정 (randomized test): 특정 조건은 ,확률적으로 기각
- 검정력 함수 test function: $f(observation X_1,X_2..)$=이 관측을 할 시 기각할 확률

7.2 (ML ratio test): $P(기긱역|H_1 \cup H_0)/P(기긱역|H_0)\le$ 로 유의수준 결정
7.3: $P(기긱역(n)|H_0\cup H_1)/P(기긱역(n)|H_0)$ as $n\longrightarrow\infty$ 로 유의수준 결정
- Wald's 검정통계량
- Rao's 검정통계량
- 분할표


## Problems



7.2

7.4
(a) $P(X_1+..X_7\ge c|H_0)\le 10\%$
애 때 $E[sum]=3.5, V[sum]=7*0.5*0.5=1.75, \sigma\sim =1.322$,
$\sqrt 7((X_1+..X_7)/7-3.5)/\sigma=((X_1+..X_7)/7-3.5)/0.5 \sim N(0,1)$
$\Phi(1.28)\sim=0.8997, \Phi(1.29)\sim=0.9015$
$P(X_1+..X_7\le (0.5*1.28+3.5)*7=28.9800)\sim=0.8997$
$P(X_1+..X_7\le (0.5*1.29+3.5)*7=29.0150)\sim=0.9015$
$P(X_1+..X_7\ge 28.9800)\sim=0.1003$
$P(X_1+..X_7\ge 29.0100)\sim=0.0885 \Longrightarrow c\in \{29,30\}$
For $c=29$, $z=(29/7-3.5)/0.5=1.285714285$, $P(..>c)\sim=0.0993$
Hence the answer is 29.

(b)
c=29면 기각, c=30이면 $\gamma$ 확률로 기각

(c)


7.6

7.8

7.10

7.12

7.14

7.16

7.18

7.20

