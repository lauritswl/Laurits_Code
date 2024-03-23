# Monte Carlo methods
The goal is to estimate the expected value of X (**The mean of X:** $\mathbb{E}_{p}[f(x)]$)
 Goal: calculate $\int p(x)f(x) dx$
 - where $p(x)$ is the probability function of x 
 - and $f(x)$ is a scalar function we happened to be interested in
 This is the probability weighted $f(x)$ over the area where X exists. This is often written as:
 $$\int p(x)f(x) dx = \mathbb{E}_{p}[f(x)] \approx \frac{1}{N}\sum\limits^{N}_{1=i}f(x_{i}), x_{i} \sim p(x)$$ 
 ### By the **central limit theorem**:
  $$\frac{1}{N}\sum\limits^{N}_{i=1}f(x_{i}) \xrightarrow{Dist} N(\mu, \sigma^{2})\begin{cases}
\mu =\mathbb{E}_{p}[f(x)]  \\
\sigma^{2} = \frac{1}{N}\mathbb{V}_{p}[f(x)]
\end{cases} ,\mathbb{V} = \text{"varriance of"}$$
The distribution of *s*, $\frac{1}{N}\sum\limits^{N}_{i=1}f(x_{i})$, approaches normal as N gets large where the mean of that normal is the expected value we try to calculate and the variance is the variance of f(x) scaled by N.