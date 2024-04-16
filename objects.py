import os
import numpy as np

class matrix:
    m = 0
    n = 0
    
    xstart = 0
    ystart = 0

    xend = 0
    yend = 0

    

    def __init__(self,m,n,xstart,ystart,xend,yend,entry):
        for i in range(m):
            for j in range (n):
                self.mat[i][j] = entry[m][n]

    def print():
