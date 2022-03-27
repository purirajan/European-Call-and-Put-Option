import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from Tridiagonal import*
from Payoff import*
from Thomas import*

def ImplicitFDMThomas(X_max,X_min,dx,T,dt,K,r,vol,delta,S):
    N = int((X_max-X_min)/dx)
    M = int(T/dt)
    X = np.zeros(N-1)
    V_call = np.zeros(N-1)# Column matrix
    V_put = np.zeros(N-1)# column matrix
    F = np.zeros(N-1) # column Matrix
   
    for i in xrange(N-1):
        X[i] = K* np.exp(X_min + (i+1)*dx) # Stock Discretization
        V_call[i] = np.exp(-i*dt)* call_payoff(X[i], K)
        V_put[i] = np.exp(-i*dt)* put_payoff(X[i], K)
    A_co = -1*((np.ones(N-1) * (vol**2 /(2*dx**2)) - ((r-delta)/(2*dx))+ (vol**2/ (4*dx)))*dt)# A Vector for the Matrix
    B_co = -1*((np.ones(N-1) * -(vol**2/dx**2) -(r-delta)) *dt) +1 # B vector for the Matrix
    C_co = (np.ones(N-1) * vol**2 /(2*dx**2) + ((r-delta)/(2*dx)- (vol**2/ (4*dx))))*-dt # C vector for the Matrix
    Matrix = Tridiagonal(B_co,C_co,A_co) # Tridiagonal Matrix
    F[N-2]= (C_co[N-2]*dt)*np.exp(-i*dt)*call_payoff(-K*np.exp(X_max)+K,0)# this is the only one element of this matrix which is non zero,but its value iterates on the time step.
    #print(Matrix)
    for i in range(M):
        V_call = Thomas(B_co, C_co, A_co, V_call+ F) 
        V_put = Thomas(B_co, C_co, A_co, V_put+ F) 
   # print(V_call)
    V_call_value= np.interp(S,X,V_call)# interpolation to find the value of S
    V_put_value= np.interp(S,X,V_put)# interploation to find the value of S
    return V_call_value,V_put_value

    
        
        

    


    
