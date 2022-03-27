import numpy as np
from scipy.stats import norm
def MonteCarlo(S,r,K,delta,vol,dt,T,N,M):     
    g=np.zeros((N,M+1)) # creating a matrix of order N X M+1 to simulate paths
    h_call=np.zeros(N) #  creating the array for call option
    h_put = np.zeros(N) # creating the array for put option
    g[:,0]=S
    for i in range(M):
        for j in range(N):
            g[j][i+1]=g[j][i]+(r-delta)*g[j][i]*dt+vol*g[j][i]*np.sqrt(dt)*norm.rvs(0,1,1) # Euler method
    for i in range(N):        
        h_call[i]=max(g[i][M]-K,0) # call  payoff 
        h_put[i]= max(-g[i][M]+K,0) # put  payoff
        
    V0_call=(np.exp(-r*T))*sum(h_call)/N # getting average of the call function
    V0_put=(np.exp(-r*T))*sum(h_put)/N # getting avargage of the put function
    return V0_call,V0_put 
        
     
