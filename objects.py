import numpy as np

class matrix:
    m = 0
    n = 0
    
    xstart = 0
    ystart = 0

    xend = 0
    yend = 0

    

    def __init__(self,matrix,dimensions):
        self.m = dimensions[0]
        self.n = dimensions[1]
        self.xstart = dimensions[2]
        self.ystart = dimensions[3]
        self.xend = dimensions[4]
        self.yend = dimensions[5]
        self.data = np.array(matrix)

    #def print():