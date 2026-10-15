# CS5187 — Vision & Image
## Reconstructed Practice Examination

**Time allowed:** 60 minutes *(practice-paper estimate)*  
**Total marks:** 50 *(suggested marks for practice; not recovered from the original exam)*

**Candidate name:** ____________________________________  
**Student ID:** _________________________________________

### Instructions

1. Answer all questions.
2. Show the main steps in calculations. Unsupported final answers may receive limited credit.
3. Give numerical answers to **two decimal places** where appropriate.
4. Unless otherwise stated, assume grayscale intensity values are real numbers.
5. This paper reconstructs remembered topics and details. Some numerical values and sub-questions have been added to make it a complete, solvable practice paper; it is **not the original examination paper**.

---

## Question 1 — Structure Tensor and Harris Corner Detection (18 marks)

Four image-gradient pairs \((I_x,I_y)\) are measured at four pixels in a local image window.

| Pixel | \(I_x\) | \(I_y\) |
|---:|---:|---:|
| 1 | 4 | 0 |
| 2 | 0 | 4 |
| 3 | 2 | 2 |
| 4 | 2 | 1 |

**(a) (4 marks)** Calculate the structure tensor (second-moment matrix) \(H\), where

\[
H=\begin{bmatrix}
\sum_i I_{x,i}^{2} & \sum_i I_{x,i}I_{y,i}\\
\sum_i I_{x,i}I_{y,i} & \sum_i I_{y,i}^{2}
\end{bmatrix}.
\]

**(b) (5 marks)** Calculate the two eigenvalues, \(\lambda_1\) and \(\lambda_2\), of \(H\). Give your answers to two decimal places.

**(c) (4 marks)** Calculate the Harris corner response

\[
R=\det(H)-k[\operatorname{trace}(H)]^2,
\]

where \(k=0.04\).

**(d) (5 marks)** Based on the eigenvalues and the Harris response, classify the image region as a **corner**, **edge**, or **flat region**. Explain briefly why the eigenvalues of the structure tensor help distinguish these cases.

**Answer:**

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

---

## Question 2 — Homography and Grayscale Interpolation (18 marks)

A grayscale source image contains the following four known pixel intensities:

| Source coordinate | Grayscale intensity \(I(x,y)\) |
|---|---:|
| \((0,0)\) | 10 |
| \((1,0)\) | 30 |
| \((0,1)\) | 50 |
| \((1,1)\) | 90 |

A homography matrix \(H\) maps a point in the **target image** to its corresponding coordinate in the **source image**:

\[
H=\begin{bmatrix}
1&0&0\\
0&1&0\\
0.5&0&1
\end{bmatrix}.
\]

For a target point \(p=(x,y)\), use homogeneous coordinates

\[
\begin{bmatrix}x'\\y'\\w'\end{bmatrix}
=H\begin{bmatrix}x\\y\\1\end{bmatrix},
\qquad
(x_s,y_s)=\left(\frac{x'}{w'},\frac{y'}{w'}\right).
\]

If the mapped source coordinate is not an integer pixel location, use **bilinear interpolation** to estimate its grayscale intensity. Assume the mapped coordinates in this question lie within the region covered by the four listed source pixels.

**(a) (5 marks)** For the target coordinate \((2,1)\), calculate the mapped source coordinate \((x_s,y_s)\), and then calculate the grayscale intensity to be assigned to target pixel \((2,1)\) using bilinear interpolation.

**(b) (5 marks)** Repeat the process for target coordinate \((1,1)\): calculate its mapped source coordinate and estimate its grayscale intensity using bilinear interpolation.

**(c) (4 marks)** The source coordinate \((0.5,0.5)\) is known. Use the inverse homography

\[
H^{-1}=\begin{bmatrix}
1&0&0\\
0&1&0\\
-0.5&0&1
\end{bmatrix}
\]

to find the corresponding target-image coordinate. Show the homogeneous-coordinate calculation and normalization.

**(d) (4 marks)** For target coordinate \((1,1)\), suppose **nearest-neighbour interpolation** is used instead of bilinear interpolation. Determine the assigned grayscale intensity and briefly state how it differs from the bilinear-interpolation result in part (b).

**Answer:**

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

---

## Question 3 — SSD, Disparity, and Depth-Estimation Error (14 marks)

A rectified stereo image pair is used to estimate the depth of a scene point. A three-pixel patch in the left image is centred at horizontal coordinate \(x_L=10\). Three candidate patches in the right image have centre coordinates \(x_R=8\), \(x_R=7\), and \(x_R=6\).

The intensities in each patch are listed in order: **left neighbour, centre pixel, right neighbour**.

| Patch | Centre coordinate | Left neighbour | **Centre pixel** | Right neighbour |
|---|---:|---:|---:|---:|
| Left-image patch | \(x_L=10\) | 10 | 20 | 30 |
| Right candidate A | \(x_R=8\) | 11 | 18 | 31 |
| Right candidate B | \(x_R=7\) | 8 | 21 | 28 |
| Right candidate C | \(x_R=6\) | 10 | 19 | 30 |

Use the sum of squared differences (SSD) over all three pixels to compare each right-image candidate with the left-image patch.

**(a) (6 marks)** Calculate the SSD for candidates A, B, and C. Identify the best matching candidate and explain your choice.

\[
SSD=\sum_i (L_i-R_i)^2
\]

**(b) (3 marks)** Using the best match, calculate the disparity

\[
d=x_L-x_R.
\]

**(c) (5 marks)** The stereo camera has focal length \(f=100\) pixels and baseline \(B=0.20\,\text{m}\). Estimate the depth using

\[
z_{\mathrm{est}}=\frac{fB}{d}.
\]

If the true depth is \(z=4.5\,\text{m}\), calculate the **signed depth-estimation error**

\[
e=z_{\mathrm{est}}-z.
\]

State the units of your final answer.

**Answer:**

____________________________________________________________________________

____________________________________________________________________________

____________________________________________________________________________

---

## End of Practice Examination

---

## Reconstruction Notes *(not part of the examination paper)*

- **Question 1:** The remembered structure—four pairs of \(I_x,I_y\), followed by calculating \(H\), its eigenvalues, the Harris response, and a conceptual question—is based on the student's recollection. The numerical values, value of \(k\), and exact wording of the final part are constructed for practice.
- **Question 2:** The four coordinates, target coordinate \((2,1)\), and homography matrix are based on the student's recollection. The grayscale values and parts (b)–(d) are newly created practice questions because the original follow-up parts are not remembered. The mapping direction is stated explicitly to make the calculations unambiguous.
- **Question 3:** SSD, disparity, a depth-error expression involving \(z_{\mathrm{est}}-z\), and a table with a “centre” label are based on the recollection. The table values, camera parameters, true depth, and exact wording are constructed for practice.
