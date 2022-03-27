import numpy as np
# Thomas algorithm 
def Thomas(alpha, beta, gama, b):# alpha is the main diagonal
# beta is the super diagonal, and gama is the sub diagonal
    N = len(alpha)  # dimension of the matrix    
    alpha = np.array(alpha)#np.zeros((N))
    beta =np.array(beta) # np.zeros((N))
    gama = np.array(gama)
    b = np.array(b)
    alphahat = np.zeros((N))
    bhat = np.zeros((N))
    alphahat[0]= alpha[0]
    bhat[0]= b[0]

    for i in range(1, N, 1):
        ratio = gama[i]/alphahat[i-1]
        alphahat[i] = alpha[i] - ratio *beta[i-1] 
        bhat[i] = b[i] - ratio *bhat[i-1]

    x = np.zeros(N)
    x[N-1] = bhat[N-1]/alphahat[N-1]

    for i in range(N-2, -1, -1):
        x[i] = (bhat[i]-beta[i]* x[i+1])/alphahat[i]

    return x
   
    

    
