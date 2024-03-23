## Pseudo code (Sequential Inversion):
Found in slides for lecture 3 - NUS SIMULATION
1. Generate U from $Unif[0, 1]$.
2. Set $X = 0$, $P = p_{0}$.
3. While $U > P$:
	- X = X + 1
	- P = P + $p_{x}$
4. Return X
![[Probabilities_for _Sequential_Inversion.png]]

*Expected number of iterations*:
$E[Y]+1$


