TreeConv
========
This Program takes bootstrap trees as input and generates a descesion tree on the basis of unique bipartition matrix
The depth of tree tells us the convergence level of bootsrap run.

Instructions

Step1: Rename bootstrap tree file as "tree.nex"
Step2: Run Rscript Matrix.R
Step3: Run python MatrixCol.py
Step4: Run python ID3call.py

(Number of attribute displayed in the tree - 1) is the total depth. 

Description of the workflow was taken from paper "Grant Brammer and Tiffani L. Williams. Using Decision Trees to Study the Convergence of Phylogenetic Analyses. 2010 IEEE Symposium. DOI: 10.1109/CIBCB.2010.5510326"

http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=5510326&url=http%3A%2F%2Fieeexplore.ieee.org%2Fxpls%2Fabs_all.jsp%3Farnumber%3D5510326
