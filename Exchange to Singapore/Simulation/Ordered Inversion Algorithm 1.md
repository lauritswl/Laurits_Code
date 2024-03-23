1. Generate U from $Unif[0, 1]$.
2. Order $y_{k}$ in a way that $p_0 ≥ p_1 ≥ p_2 ≥ p_3 ≥ ...$ 
3. Set $X = 0$, $P = p_{0}$.
4. While $U > P$:
	- X = X + 1
	- P = P + $p_{X}$
5. Return $y_{x}$

***Expected number of iterations***:
$\le E[Y]+1$
