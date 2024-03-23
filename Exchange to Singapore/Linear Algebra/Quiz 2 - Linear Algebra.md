# Question 1:
Let $A = (a_{ij})_{2 \times 2}$ and $B = (b_{ij})_{2 \times 2}$ where $a_{ij} = (-1)^{i+j}$ and $b_{ij} = \begin{cases}i \text{ if } i \geq j   \\ j \text{ if } i < j\end{cases}$
Then $B - 2A =$



To find $B - 2A$, we first need to find the matrices $A$ and $B$.

Given that $a_{ij} = (-1)^{i+j}$, we can write out matrix $A$ as: $$A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} = \begin{bmatrix} (-1)^{1+1} & (-1)^{1+2} \\ (-1)^{2+1} & (-1)^{2+2} \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$$

Next, let's determine matrix $B$ using the given conditions for $b_{ij}$: $$B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix}$$

Now, we can calculate $2A$ and $B - 2A$: $$2A = 2 \times \begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix} = \begin{bmatrix} 2 & -2 \\ -2 & 2 \end{bmatrix}$$ $$B - 2A = \begin{bmatrix} 1 & 1 \\ 2 & 2 \end{bmatrix} - \begin{bmatrix} 2 & -2 \\ -2 & 2 \end{bmatrix} = \begin{bmatrix} 1-2 & 1-(-2) \\ 2-(-2) & 2-2 \end{bmatrix} = \begin{bmatrix} -1 & 3 \\ 4 & 0 \end{bmatrix}$$
So, $B - 2A = \begin{bmatrix} -1 & 3 \\ 4 & 0 \end{bmatrix}$.

# Question 2
Let **A** be a matrix:
$$A = \begin{pmatrix} 1 & 1 & 1\\1 & -1 & -1 \\ 0 & 2 & 2 \end{pmatrix}$$


## a)
What is (1,1)-entry of $A^2$ 
To calculate the (1,1)-entry of $A^2$, we first need to find the square of matrix **A**: $$A^2 = A \cdot A$$ $$A^{2} = \begin{pmatrix} 1 & 1 & 1  \\ 1 & -1 & -1  \\  0 & 2 & -2 \end{pmatrix} \cdot \begin{pmatrix} 1 & 1 & 1 \\ 1 & -1 & -1 \\ 0 & 2 & -2 \end{pmatrix}$$ Perform the matrix multiplication to find $A^2$, and then the (1,1)-entry will be the element in the first row and first column of $A^2$.
$$A^{2}_{(1,1)} = a_{(1,j)} a_{(i,1)}= \begin{pmatrix}1 & 1 & 1\end{pmatrix} \cdot \begin{pmatrix}1 \\ 1 \\ 0\end{pmatrix} = 1 + 1 + 0 = 2$$
## b)
What is (3,2)-entry of $A^2$:
Similarly, to find the (3,2)-entry of $A^2$, you need to find the element in the third row and second column of the matrix $A^2$.
$$A^{2}_{(3,2)} = a_{(3,j)} a_{(i,2)}= \begin{pmatrix}0 & 2 & -2\end{pmatrix} \cdot \begin{pmatrix}1 \\ -1 \\ 2\end{pmatrix} = 0 -2 -4 = -6$$
## c)
What is the (1,1)-entry of $AA^{T}$.
As $A_{ij}^{T}$ is just $A_{ji}$. Then $aa^{T}_{ij}$ = $row_{i} \times row_{i}$.
$$AA^{t}_{(1,1)} = a_{(1,j)} a_{(1,j)}= \begin{pmatrix}1 & 1 & 1\end{pmatrix} \cdot \begin{pmatrix}1 \\ 1 \\ 1\end{pmatrix} = 1 + 1 + 1 = 3$$

## d)
The (3,2)-entry of $AA^{T}$
What is the (1,1)-entry of $AA^{T}$.
As $A_{ij}^{T}$ is just $A_{ji}$. Then $aa^{T}_{ij}$ = $row_{i} \times row_{i}$.
$$AA^{t}_{(1,1)} = a_{(1,j)} a_{(1,j)}= \begin{pmatrix}0 & 2 & -2\end{pmatrix} \cdot \begin{pmatrix}0 \\ 2 \\ -2\end{pmatrix} = 0 + 2*2 + (-2)*(-2) = 4 + 4 = 8$$

# Question 3: NEEDS WORK
Which of the following statements is **false** (i.e. not always true)?
1. If A is a nonzero $m \times n$ matrix and B, C are $n \times p$ matrices such that A(B-C) = 0, then B = C.
	- A(B-C) = AB - AC = 0
2. If A, B are square matrices of the same order, then $(A+B)^{2}=A^{2}+AB+BA+B^{2}$
	
3. If A, B are matrices of the same size and c is a real number such $cA = cB$, then $c = 0$ or $A = B$.
4. If A is a square matrix, then $(I-A)^3 = I - 3A + 3A^{2}-A^{3}$.



AB -AC = 0

# Question 4:
Let $A$ ban an $m \times n$ matrix and $b$ an $m \times 1$ column matrix such that the linear system $Ax = b$ has no solution.

Which of the following statements are always **true**?
- [x] If B is an $n \times p$ matrix, then $ABx = b$ has no solution
	- Only by having n x p where n (rows) > p (columns), we can be sure to have no solutions. This means that b would always be longer than the rows, and no soultions would occur.
	- Alternatively no solutions could occur because the first column was only 0's, if this is the case, no matrix premultiplier could change this. 
- [ ] $Ax = 0$ has no solution
- [x] If $A$ is a square matrix (i.e. m = n), then $A^2x=b$ has no solution
	- No elementary row operation could make an identity matrix singular, as the row operations are undoable.
- [x] If $B$ is an $m \times m$ matrix, then $BAx = b$ has no solution
- [ ] If $B$ is an $m \times n$ matrix, then $(A + B)x = b$ has no solution

# Question 5:
Let $A,B$ be $2 \times 2$ matrices such that $A^{-1}=\begin{pmatrix}1 & -1 \\ 1 & 1\end{pmatrix}$ and $B^{-1}=\begin{pmatrix}0 & 2  \\ 1 & 0\end{pmatrix}$.
Then find $(AB)^{-1}$:
$$(AB)^{-1}=B^{-1}A^{-1}=\begin{pmatrix}0 & 2  \\ 1 & 0\end{pmatrix}\begin{pmatrix}1 & -1 \\ 1 & 1\end{pmatrix}=\begin{pmatrix}2 & 2  \\ 1 & -1\end{pmatrix}
$$

# Question 6
Which of the following statements are always **true**?
- [x] If $A,B$ are square matrices of the same order and $B$ is invertible, then $(B^{-1}AB)^{2}=B^{1}A^{2}B$
- [x] If $A$ is an invertible matrix and $c$ a nonzero real number, then $cA^{T}$ and $(cA^{T})^{-1} = \frac{1}{c}(A^{-1})^{T}$
- [ ] If $A,B$ are square matrices of the same order and $B$ is invertible, then $(B^{-1}AB)^{2}=(B^{2})^{-1}A^{2}B^{2}$
- [ ] If $A$ is an invertible matrix and $c$ a nonzero real number, then $cA^{T}$ is invertible and $(cA^{T})^{-1} = c(A^{-1})^{T}$.

# Question 7
Match the following elementary matrices with the corresponding elementary row operations.

Only completed online, checked with http://matrixmultiplication.xyz/



# Question 8
Let $A$ be a square matrix of order $3$ and $I$ the identity matrix of order 3.
Suppose
$$
 \left(
\begin{array}{(c|c}
A & B
\end{array}
\right)
\

\begin{array}{(c}
\text{a series of } \\
\rightarrow \\
\text{row operations}
\end{array}
\
\left(
\begin{array}{(ccc|ccc}
1 & 0 & 1 & 1 & 1 & 1\\
0 & -1 & 0 & -1 & 2 & -3\\
0 & 0 & 1 & -1 & 1 & 2\\
\end{array}
\right)
$$


$$\text{Then } A^{-1} =
\left(
\begin{array}{(ccc|ccc}
1 & 0 & 1 & 1 & 1 & 1\\
0 & -1 & 0 & -1 & 2 & -3\\
0 & 0 & 1 & -1 & 1 & 2\\
\end{array}
\right) 
$$
$$\begin{array}{(c}
(-1)R_{2} \\
\leftrightarrow
\end{array}
\left(
\begin{array}{(ccc|ccc}
1 & 0 & 1 & 1 & 1 & 1\\
0 & 1 & 0 & 1 & -2 & 3\\
0 & 0 & 1 & -1 & 1 & 2\\
\end{array}
\right) $$
$$\begin{array}{(c}
R_{1}-R_{3} \\
\leftrightarrow
\end{array}
\left(
\begin{array}{(ccc|ccc}
1 & 0 & 0 & 2 & 0 & -1\\
0 & 1 & 0 & 1 & -2 & 3\\
0 & 0 & 1 & -1 & 1 & 2\\
\end{array}
\right)$$
# Question 9
Determine the value(s) of $a$ such that the square matrix below is singular:

$$\begin{pmatrix}a & 1 & 0 \\ 1 & 0 & a \\ 0 & a & 1\end{pmatrix}$$
$Det = a(0-a^{2})-1*(0-1*1) = a(a^{2)}-1 = a^3-1$

This is solved for $Det = 0$ as the matrix is singular here:
$a^{3}-1 = 0 \leftrightarrow a^{3} = 1 \leftrightarrow a = 1^{-2} \leftrightarrow a = 1$

# Question 10
Let $A$ be a square matrix such that $A^{4}-3A^{3}+3A^{2}-A+2I = 0$
Determine which one of the following is $A^{-1}$.


To solve this problem, we need to find the inverse of matrix $A$, denoted as $A^{-1}$.

Given that $A^4 - 3A^3 + 3A^2 - A + 2I = 0$, where $I$ is the identity matrix, we can rewrite the equation as: $A(A^3 - 3A^2 + 3A - I) = -2I$

To find $A^{-1}$, we can multiply both sides of the equation by $A^{-1}$: $A^{-1}A(A^3 - 3A^2 + 3A - I) = -2A^{-1}I$ $A^3 - 3A^2 + 3A - I = -2A^{-1}$

Since we are looking for $A^{-1}$, we can rearrange the equation as: $A^{-1} = \frac{A^3 - 3A^2 + 3A - I}{-2}$

Therefore, the inverse of matrix $A$ is given by $\frac{A^3 - 3A^2 + 3A - I}{-2}$.
# Question 11
Which of the following statements are always **true**?
- [ ] If $A$ is a singular (square) matrix, then a row-echelon form of $A$ has at least one non-pivot columns.
- [ ] If $A$ is an invertible matrix, then a row-echelon form of $A$ has no non-pivot columns

# Question 12
Let $A = \begin{pmatrix}2 & 0 & -1 \\ 1 & 1 & 0  \\ 0 & 2 & 2\end{pmatrix}$
Then determine the cofactor for the following:

1) The (1,1)-cofactor of A:
The cofactor is determined by $A_{ij} = 1(-1)^{i+j}det(M_{ij})$
$M_{ij}$ is the $(n-1) \times (n-1)$ matrix obtained by deleting the $i_{th}$ row and $j_{th}$ column from A.

$(-1)^{1+1} \cdot det(\begin{pmatrix}1 & 0 \\ 2 & 2\end{pmatrix})= 1\cdot(1*2-0*2) = 1(2) = 2$

2) The (1,2)-cofactor of A:
$$(-1)^{1+2} \cdot \begin{pmatrix}1 & 0 \\ 0 & 2\end{pmatrix}=-1 \cdot(1*2-0)=-2$$
3) The (1,3)-cofactor of A:
$$(-1)^{2+2} \cdot \begin{pmatrix}1 & 1 \\ 0 & 2\end{pmatrix}=1 \cdot(1*2-1*0)=2$$


Determinant of A
$$2 \cdot 2 + 0 \cdot (-2) + (-1) \cdot 2 = 4+0 -2 = 2$$



# Question 3

Consider $X ∼ \frac{1}{5}q^{(1)} + \frac{2}{5}q^{(2)} + \frac{2}{5}q^{(3)}$, where:

$$\begin{cases}
q^{(1)}:q_{1}^{(1)} = 0.3, q_{2}^{(1)}=0.2, q_{3}^{(1)} = 0.5; \\
q^{(2)}:q_{1}^{(2)} = 0.3, q_{5}^{(2)}=0.7 \\
q^{(3)}:q_{1}^{(3)} = 0.25, q_{2}^{(3)}=0.25, q_{4}^{(3)} = 0.25, q_{5}^{(3)} = 0.25;
\end{cases}$$

## a) Find P(X = 5)
$$P(X = 5) = \frac{1}{5}*0 + \frac{2}{5}*0.7 + \frac{2}{5}*0.25 = 0.38$$

## b) Find the probability mass function of X
$$1 = \frac{1}{5}*0.3 + \frac{2}{5}*0.3 + \frac{2}{5}*0.25 = 0.28$$
$$2 = \frac{1}{5}*0.2 + \frac{2}{5}*0 + \frac{2}{5}*0.25 = 0.14$$

$$3 = \frac{1}{5}*0.5 + \frac{2}{5}*0 + \frac{2}{5}*0 = 0.1$$
$$4 = \frac{1}{5}*0 + \frac{2}{5}*0 + \frac{2}{5}*0.25 = 0.1$$
$$5 = \frac{1}{5}*0 + \frac{2}{5}*0.7 + \frac{2}{5}*0.25 = 0.38$$
## c) Find the probability mass function of X
Create table with 100 entrances:
{0:27 = 1
28:41 = 2
42:51 = 3
52:61 = 4
62:99 = 5}
Simulate U = $\lfloor 100*unif(0,1) \rfloor$ 
Find corresponding value to U in table


## d) Give the pseudo-code to generate X by the alias method
* Generate U ~ Unif(0,1) and V ~ Unif(0,1)
* If U < 0.2
	* If V < 0.3, X = 1
	* elseif < 0.5, X =2
	* else X = 3
* elseif U < 0.6
	* V < 0.3, X = 1
	* else X = 5
* else:
	* if V < 0.5, X =$\lceil 4*V\rceil$
	* else X = $\lceil 4*V\rceil+1$





