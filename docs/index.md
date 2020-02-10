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

The spatial discretization implies
$$
\Delta z = \frac{1}{N}, \qquad u_i = u(z_i), \qquad i=0,1,\cdots,N 
$$
for a 1D domain with a unit width. Note that if we have a domain with a depth $$ d $$, then $$ \Delta z = \frac{d}{N} $$. We also need temporal discretization as consolidation is a time dependent problem. A uniform time stepping from $$ t_0 $$ up to $$ t_n $$ is assumed and an illustration of this is shown below. For a selected time step $$ \Delta t $$, we have
$$
t_n = n\Delta t
$$
The partial derivatives in the governing PDE, in equation \eqref{eq:1D_consolidation}, can be approximated in various ways with respect to time and space. The most common approximations are discussed here.
