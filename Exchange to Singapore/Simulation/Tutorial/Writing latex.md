$$f(x)= \begin{cases}
\frac{x-2}{2} \text{, if }2\leq x \leq 3. \\
\frac{\frac{x-2}{3}}{2} \text{, if }3\leq x \leq 6.
\end{cases}$$


# Q4
Consider the density :
$$f(x) = \frac{2}{\pi(1+x^{2})^{2}}$$

and the corresponding cumulative distribution function  
$$F (x) = \frac{1}{2}+\frac{1}{\pi}(\arctan x + \frac{x}{1+x^{2}})$$These functions define the $t$ distribution with 3 degrees of freedom. In this question, we  shall generate from it using numerical inversion. In order to do that, we shall have to work a little to identify a good starting interval for the solution to $F (X) − U = 0$

## a)
Prove that when $x \geq 0$,

 
$$ \frac{1}{2}+\frac{1}{\pi}\arctan x \leq F (x) \leq \frac{1}{2}+\frac{2}{\pi}\arctan x$$
When x = 0,
$$F (0) = \frac{1}{2}+\frac{1}{\pi}(\arctan 0 + \frac{0}{1+0^{2}})=\frac{1}{2}$$
When $x = \infty$,
$$F (\infty)-1/2 \rightarrow^{\lim \infty} \frac{1}{\pi}(\arctan \infty + \frac{\infty}{1+\infty^{2}})= \frac{1}{\pi}(\arctan \infty + \frac{\infty}{\infty^{2}})=\frac{1}{\pi}(\arctan \infty + \frac{1}{\infty})=\frac{1}{\pi}(\arctan \infty)=\frac{1}{\pi}(\frac{\pi}{2})=\frac{1}{2}$$
$$F (\infty) = 1$$

$$Bernoulli \sim \text{if U = unif(0,1)}, \begin{cases} U < p = 0 \\ U \geq p = 0\end{cases}$$