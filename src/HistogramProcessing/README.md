# 直方图处理
- 直方图均衡化
> 简单来说，是为了增强图像以满足人眼视觉或其它用途，例如过亮图像，过暗图像，低对比度图像，高对比度图像，完全自动化处理的函数，不需要额外的输入。<br/>
> 精确数学表达式 ![](https://latex.codecogs.com/svg.latex?\inline&space;\fn_jvn&space;s=T(r)=(L-1)\int_{0}^{r}p_r(w)dw)<br/> 实际离散情况![](https://latex.codecogs.com/svg.latex?\inline&space;\fn_jvn&space;s_k=T(r_k)=(L-1)\sum_{j=0}^{k}p_r(r_j)=\frac{(L-1)}{MN}\sum_{j=0}^{k}n_j)<br/>
> 其中L为图像中可能的灰度级数量（8比特对应256)，T为对应的变换函数，p为灰度级r出现的概率。
- 直方图规定化
> 有时候我们希望处理后的图像具有规定的直方图图像，这种方法称为直方图规定化<br/>
> 精确数学表达式 ![](https://latex.codecogs.com/svg.latex?\inline&space;\fn_jvn&space;G(z)=(L-1)\int_{0}^{z}p_z(t)dt=s=(L-1)\int_{0}^{r}p_r(w)dw)<br/> 实际离散情况 ![](https://latex.codecogs.com/svg.latex?\inline&space;\fn_jvn&space;G(z_q)=(L-1)\sum_{i=0}^{q}p_z(z_j)=s_k=T(r_k)=(L-1)\sum_{j=0}^{k}p_r(r_j)=\frac{(L-1)}{MN}\sum_{j=0}^{k}n_jgit )</br>
> 参数和上面一样，p(z)为给定的给定的概率密度函数。
- 局部直方图均衡化
> 增强图像中小区域的细节需要，以图像中每个像素的邻域中的灰度分布为基础设计变换函数。例如3x3邻域或者5x5邻域。