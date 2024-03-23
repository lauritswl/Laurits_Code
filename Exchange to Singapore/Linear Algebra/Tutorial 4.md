# Q1
For each of the following matrices,
$$(a) \begin{pmatrix}0 & 1 & 3  \\  1 & 3 & 1 \\ 1 & 4 & 5\end{pmatrix},\ (b)\begin{pmatrix}1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \\ 2 & 0 & 2 & 1 \\ 2 & 0 & 1 & 0\end{pmatrix}$$
## (i)
compute the determinant by following Definition 2.5.2;
### a)
$$a) \begin{pmatrix}0 & 1 & 3  \\  1 & 3 & 1 \\ 1 & 4 & 5\end{pmatrix} = 0\begin{pmatrix}3 & 1 \\ 4 & 5\end{pmatrix}-1\begin{pmatrix}1 & 1 \\ 1 & 5\end{pmatrix}+3\begin{pmatrix}1 & 3 \\ 1 & 4\end{pmatrix}$$
$$-(1*5-1*1)+3(1*4-3*1)=-(5-1)+(12-9)=-5+1+12-9 = 13-14 = -1$$
**Determinant of a = -1**
### b)
$$(b)\begin{pmatrix}1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \\ 2 & 0 & 2 & 1 \\ 2 & 0 & 1 & 0\end{pmatrix} = 1\begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 1 \\ 0 & 1 & 0\end{pmatrix}-1\begin{pmatrix}1 & 0 & 1 \\ 2 & 2 & 1 \\ 2 & 1 & 0\end{pmatrix}+(-1)\begin{pmatrix}1 & 1 & 1 \\ 2 & 0 & 1 \\ 2 & 0 & 0\end{pmatrix}-0\begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 1 \\ 0 & 1 & 0\end{pmatrix}$$
$$1):\begin{pmatrix}1 & 0 & 1 \\ 0 & 2 & 1 \\ 0 & 1 & 0\end{pmatrix}=1\begin{pmatrix}2 & 1 \\ 1 & 0\end{pmatrix}-0+1*0= 1(0-1)=-1$$
$$2:\begin{pmatrix}1 & 0 & 1 \\ 2 & 2 & 1 \\ 2 & 1 & 0\end{pmatrix} = 1\begin{pmatrix}2 & 1 \\ 1 & 0\end{pmatrix}-0+1\begin{pmatrix}2 & 2 \\ 2 & 1\end{pmatrix}=1(0-1)+1(2-4)=-1-2=-3$$
$$3: \begin{pmatrix}1 & 1 & 1 \\ 2 & 0 & 1 \\ 2 & 0 & 0\end{pmatrix} = 1*0-1\begin{pmatrix}2 & 1 \\ 2 & 0\end{pmatrix}+1*0=-1(0-2)=2$$
$$\begin{pmatrix}1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \\ 2 & 0 & 2 & 1 \\ 2 & 0 & 1 & 0\end{pmatrix} = 1(-1)-1(-3)+(-1)(2)-0=-1+3-2=3-3=0$$
## (ii) 
Compute the determinant using the method of elementary row operations discussed in Remark 2.5.15
$$det(a)=\begin{pmatrix}0 & 1 & 3  \\  1 & 3 & 1 \\ 1 & 4 & 5\end{pmatrix} = -\begin{pmatrix}  1 & 3 & 1 \\ 0 & 1 & 3  \\ 1 & 4 & 5\end{pmatrix} = -\begin{pmatrix}  1 & 3 & 1 \\ 0 & 1 & 3  \\ 0 & 1 & 4\end{pmatrix} = -\begin{pmatrix}  1 & 3 & 1 \\ 0 & 1 & 3  \\ 0 & 0 & 1\end{pmatrix} = -(1*1*1) = -1$$
$$det(b) = 
\begin{pmatrix}1 & 1 & -1 & 0 \\ 1 & 1 & 0 & 1 \\ 2 & 0 & 2 & 1 \\ 2 & 0 & 1 & 0\end{pmatrix}=
\begin{pmatrix}1 & 1 & -1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & -2 & 4 & 1 \\0 & -2 & 3 & 0\end{pmatrix}=
-\begin{pmatrix}1 & 1 & -1 & 0 \\0 & -2 & 4 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & -2 & 3 & 0\end{pmatrix}=
-\begin{pmatrix}1 & 1 & -1 & 0 \\0 & -2 & 4 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & -1 & -1\end{pmatrix}=
-\begin{pmatrix}1 & 1 & -1 & 0 \\0 & -2 & 4 & 1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0\end{pmatrix}=
-(1*-2*1*0)=-0=0
$$ 
## (iii)
if the matrix is invertible compute the inverse using the adjoint of the matrix discussed in Theorem 2.5.25
**Only the 3x3 matrix is invertible:**

**Adjoint method to Determine the Inverse of Matrix**
Let A be an invertible n x n matrix. Then
$$A^{-1}=\frac{1}{det(A)}adj(A)$$
$$adj(A) = [cofactor(A)]^{T}$$

For: $A = \begin{pmatrix}0 & 1 & 3  \\  1 & 3 & 1 \\ 1 & 4 & 5\end{pmatrix}$

Then: $A^{-1} = \frac{1}{det(A)}adj(A) = \frac{1}{-1}adj(\begin{pmatrix}0 & 1 & 3  \\  1 & 3 & 1 \\ 1 & 4 & 5\end{pmatrix})$
I now find the cofactor matrix:

where $cof(A)_{1,1} = (-1)^{1+1}\begin{pmatrix}3 & 1 \\ 4 & 5\end{pmatrix}$ and so on:


$cof(A) = \begin{pmatrix}cof(A)_{1,1} & cof(A)_{1,2} & cof(A)_{1,3} \\ cof(A)_{2,1} & cof(A)_{2,2} & cof(A)_{2,3} \\ cof(A)_{3,1}  & cof(A)_{3,2}  & cof(A)_{3,3} \end{pmatrix} = \begin{pmatrix}11  & -4 & 1 \\ 7  & -3 & 1 \\ -8 & 3 & -1\end{pmatrix}$ 
We have learnt:
if A is invertible: $A \cdot adj(A) = det(A)I$
$$adj(A) = [cof(A)]^{T}=\begin{pmatrix}11  & -4 & 1 \\ 7  & -3 & 1 \\ -8 & 3 & -1\end{pmatrix}^{T} = \begin{pmatrix}11 & 7 & -8 \\ -4 & -3 & 3 \\ 1 & 1 & -1\end{pmatrix}$$




$$A^{-1} = \frac{1}{-1}adj(\begin{pmatrix}0 & 1 & 3  \\  1 & 3 & 1 \\ 1 & 4 & 5\end{pmatrix})=-\begin{pmatrix}11 & 7 & -8 \\ -4 & -3 & 3 \\ 1 & 1 & -1\end{pmatrix} = \begin{pmatrix}-11 & -7 & 8 \\ 4 & 3 & -3 \\ -1 & -1 & 1\end{pmatrix}$$

# Q2
Let $A, B$ and $C$ be $4 \times 4$ matrices such that both $A$ and $B$ can be obtained from $C$ by the following elementary row operations
$C \rightarrow R_{2}-2R_{1} \rightarrow -2R_{1} \rightarrow A$ and $C \\ \rightarrow (R_{1} \leftrightarrow R_{3}) \\ \rightarrow R_{1} + R_{4} \\ \rightarrow B$.

## i)
Find four elementary matrices so that $A = E_1 ... E_4 B$

We need to go from B to C and then to A, so the 
So we just backtrack:
$$C =\begin{pmatrix}0 & 0 & 1 & 0 \\0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}\begin{pmatrix}1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}B$$
$$A=\begin{pmatrix}-2 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}\begin{pmatrix}1 & -2 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}C$$
$$A = \begin{pmatrix}-2 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}\begin{pmatrix}1 & -2 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}\begin{pmatrix}0 & 1 & 0 & 0 \\1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}\begin{pmatrix}1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1\end{pmatrix}B$$
## ii)

If $det(B) = 4$ then $det(A) =-(-2*4) = 8$


# Q3 
Let $A$ be an invertible matrix of order $n$ such that $A^{-1} = A^{T}$
## i)
Prove that $det(A) = \pm 1$
For $A^{-1}$ we have $AA_{-1} = A_{-1}A = I,$
and by the definition we therefore have:
$$A^TA=I=AA^T$$
We have that $det(QQ^{T})= 1 \rightarrow det(Q^{T})det(Q) = 1 \rightarrow det(Q)det(Q) = 1\rightarrow |det(Q)|^{2 = 1}\rightarrow det(Q) = \pm 1$.




$$Det(A^{-1}) = det(A^{T}) \leftrightarrow Det(A^{-1}) = det(A) \leftrightarrow$$


## ii)
If n = 2 and det(A) = 1, show that $$A = \begin{pmatrix}cos(\theta) & -sin(\theta) \\ sin(\theta) & cos(\theta)\end{pmatrix}$$
We have the $sin^{2}x + cos^{2}x = 1$
And $Det(A) = cos^{2}- (-sin^{2})= sin^{2}+cos^{2}=1$ 



# Q4
Are the following true:
## i)
$Det(A + B) = Det(A) + Det(B)$ 
**Not True**
**As**:
$Det(\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}+\begin{pmatrix}0 & 0  \\ 0 & 1\end{pmatrix})=Det(\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}) =1$
**While**:
$Det(\begin{pmatrix}1  &  0 \\ 0 & 0\end{pmatrix})+Det(\begin{pmatrix}0 & 0  \\ 0 & 1\end{pmatrix})=0+0=0$

**And**:
$1 \neq 0$


## ii)
$Det(A + I) = Det(A^{T}+I)$
When flipping A for A^{T} then the elements getting changed by the addition of an Identity matrix (diagonal) isn't changed either. So the added size of an I is the same.

## iii)
if $A, B$ and $C$ are square matrices of the same size such that $det(A) =  det(B)$, then $det(A + C) = det(B + C)$.