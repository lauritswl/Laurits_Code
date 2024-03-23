Importance sampling is used in relation to Monte Carlo methods to sample with less variability. 
For Monte Carlo methods it is necessary to understand:
![[Monte Carlo methods]]

# Importance sampling
Say we have another distribution $q(x)$, then: 
$$\mathbb{E}_{p}[f(x)] =\int p(x)f(x) dx = \int \frac{q(x)}{q(x)}\cdotp(x)f(x) dx = \int q(x)\cdot\left[ \frac{p(x)}{q(x)}f(x) \right] dx =\mathbb{E}_{q}\left[ \frac{p(x)}{q(x)}f(x) \right]$$
Recalling from Monte Carlo, we can now estimate the expected value of X with samples from q:
$$\mathbb{E}_{q}\left[ \frac{p(x)}{q(x)}f(x) \right] \approx
\underset{\text{r}}{\underbrace{
\frac{1}{N}\sum\limits^{N}_{i=1} \frac{p(x_{i})}{q(x_{i})}f(x_{i})
}}
, \ x_{i} \sim q(x)$$
**This has a new variance**:
$$\mathbb{V}_{q}[r] = \frac{1}{N}\mathbb{V}_{q}[\frac{p(x)}{q(x)}f(x)]$$
**We hope to pick an q, so that:**
$$\mathbb{V}_{q}\left[\frac{p(x)}{q(x)}f(x)\right] \leq \mathbb{V}_{p}[f(x)]$$
To do this, $q(x)$ should be dense where $|p(x)f(x)|$ is dense.
There is no easy way to pick q. We should pick q from our biases.

