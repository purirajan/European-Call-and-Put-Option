import numpy as np
from scipy.sparse import spdiags
def Tridiagonal(alpha,beta,gama):
    N = len(alpha)
    data = np.array([alpha,gama,beta])
    triset =np.array([0,-1,1])
    A = spdiags(data,triset,N,N).toarray()
    return A
   # B=[]
    #for i in range(N):
       # B.append(N)
    #print("Matrix A is:")
   # print(A)
    #x=np.linalg.solve(A,B)
    
    #print(x)
    #print(np.allclose(np.dot(A, x), B))
