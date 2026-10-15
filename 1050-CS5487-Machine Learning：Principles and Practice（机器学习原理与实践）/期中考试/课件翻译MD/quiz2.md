(3) At a particular pixel location, the image gradients in a local window yield the following second moment matrix (also called the structure tensor);

$$ \mathsf{H}=[[sum(\mathsf{I x}^{\wedge}2),\quad sum(\mathsf{I x}^{*}\mathsf{I y})],\quad[sum(\mathsf{I x}^{*}\mathsf{I y}),\quad sum(\mathsf{I y}^{\wedge}2)]] $$

Suppose the accumulated values (summed over the window with Gaussian weighting) give:

$$ \mathrm{sum}(\mathrm{lx}^{\wedge}2)=800,\quad\mathrm{sum}(\mathrm{ly}^{\wedge}2)=750,\quad\mathrm{sum}(\mathrm{lx}*\mathrm{ly})=100 $$

$$ \mathrm{S o~H}=[[800,100],[100,750]]. $$

(a) [5 marks] Compute the two eigenvalues  $ \lambda_{1} $ and  $ \lambda_{2} $ of matrix H. (Hint: Use the characteristic equation  $ \det(H - \lambda I) = 0 $.)

(b) [5 marks] Based on the eigenvalues, classify this point as a corner, edge, or flat region. Justify your answer.

(c) [5 marks] Compute the Harris corner response using the formula  $ R = \det(H) - k \times (\text{trace}(H))^2 $, where  $ k = 0.05 $. Is this a strong corner response? Explain.
