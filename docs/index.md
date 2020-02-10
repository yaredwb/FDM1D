## One-dimensional Consolidation

The partial differential equation governing one-dimensional consolidation is given by

$$
\frac{\partial u}{\partial t} - c_v \frac{\partial^2 u}{\partial z^2} = 0
\label{eq:1D_consolidation}
$$

where $$ u $$ is the excess pore water pressure, $$ t $$ stands for time, $$ z $$ represents depth and $$ c_v $$ is the coefficient of consolidation which can be expressed as

$$
c_v = \frac{k}{m_v \gamma_w}
$$

with $$ k $$ being the coefficient of permeability, $$ m_v $$ the coefficient of volumetric compressibility and $$ \gamma_w $$ the unit weight of water.

## Spatial and Temporal Discretization

We will solve the consolidation problem over a 1D domain which is spatially discretized into $$ N $$ equally spaced units as shown in the figure below.

$$\usepackage{tikz}
\usetikzlibrary{arrows,calc,shapes,automata,positioning,decorations.markings}	
\begin{tikzpicture}
\draw[thick] (0,0) -- (10,0);
\draw[] (0,0.3) -- (0,0.7);
\draw[->,-stealth] (0,0.5) -- (1,0.5);
\node [right] at (1,0.5) {$ z $};
\filldraw[blue] (0,0) circle (2pt);
\filldraw[blue] (1,0) circle (2pt);
\filldraw[blue] (4,0) circle (2pt);
\filldraw[blue] (5,0) circle (2pt);
\filldraw[blue] (6,0) circle (2pt);
\filldraw[blue] (9,0) circle (2pt);
\filldraw[blue] (10,0) circle (2pt);
\node [below] at (0,-0.25) {$ z_0 $};
\node [below] at (1,-0.25) {$ z_1 $};
\node [below] at (2.5,-0.25) {$ \cdots $};
\node [below] at (4,-0.25) {$ z_{i-1} $};
\node [below] at (5,-0.25) {$ z_i $};
\node [below] at (6,-0.25) {$ z_{i+1} $};
\node [below] at (7.5,-0.25) {$ \cdots $};
\node [below] at (9,-0.25) {$ z_{N-1} $};
\node [below] at (10,-0.25) {$ z_N $};
\end{tikzpicture}$$

$$\usetikzlibrary{decorations.pathmorphing}
\begin{tikzpicture}[line width=0.2mm,scale=1.0545]\small
\tikzset{>=stealth}
\tikzset{snake it/.style={->,semithick,
decoration={snake,amplitude=.3mm,segment length=2.5mm,post length=0.9mm},decorate}}
\def\h{3}
\def\d{0.2}
\def\ww{1.4}
\def\w{1+\ww}
\def\p{1.5}
\def\r{0.7}
\coordinate[label=below:$A_1$] (A1) at (\ww,\p);
\coordinate[label=above:$B_1$] (B1) at (\ww,\p+\h);
\coordinate[label=below:$A_2$] (A2) at (\w,\p);
\coordinate[label=above:$B_2$] (B2) at (\w,\p+\h);
\coordinate[label=left:$C$] (C1) at (0,0);
\coordinate[label=left:$D$] (D) at (0,\h);
\draw[fill=blue!14](A2)--(B2)-- ++(\d,0)-- ++(0,-\h)--cycle;
\draw[gray,thin](C1)-- +(\w+\d,0);
\draw[dashed,gray,fill=blue!5](A1)-- (B1)-- ++(\d,0)-- ++(0,-\h)-- cycle;
\draw[dashed,line width=0.14mm](A1)--(C1)--(D)--(B1);
\draw[snake it](C1)--(A2) node[pos=0.6,below] {$c\Delta t$};
\draw[->,semithick](\ww,\p+0.44*\h)-- +(\w-\ww,0) node[pos=0.6,above] {$v\Delta t$};
\draw[snake it](D)--(B2);
\draw[thin](\r,0) arc (0:atan2(\p,\w):\r) node[midway,right,yshift=0.06cm] {$\theta$};
\draw[opacity=0](-0.40,-0.14)-- ++(0,5.06);
\end{tikzpicture}$$



The spatial discretization implies
$$
\Delta z = \frac{1}{N}, \qquad u_i = u(z_i), \qquad i=0,1,\cdots,N 
$$
for a 1D domain with a unit width. Note that if we have a domain with a depth $$ d $$, then $$ \Delta z = \frac{d}{N} $$. We also need temporal discretization as consolidation is a time dependent problem. A uniform time stepping from $$ t_0 $$ up to $$ t_n $$ is assumed and an illustration of this is shown below. For a selected time step $$ \Delta t $$, we have
$$
t_n = n\Delta t
$$
The partial derivatives in the governing PDE, in equation \eqref{eq:1D_consolidation}, can be approximated in various ways with respect to time and space. The most common approximations are discussed here.
