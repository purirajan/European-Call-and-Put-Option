import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from Tridiagonal import*
from Payoff import*
from SOR import*

def CrankNicholsonSOR(X_max,X_min,dx,T,dt,K,r,vol,delta,S,w,Kmax):
    N = int((X_max-X_min)/dx)
    print "\nNumber of asset steps: ", N
    M = int(T/dt)
    print "Number of time steps: ", M
    X = np.zeros(N-1)
    V_call = np.zeros(N-1)# Column matrix
    V_put = np.zeros(N-1)# column matrix
    F = np.zeros(N-1) # column Matrix
   
    for i in xrange(N-1):
        X[i] = K* np.exp(X_min + (i+1)*dx) # Stock Discretization
        V_call[i] =np.exp(-i*dt)* call_payoff(X[i], K)
        V_put[i] = np.exp(-i*dt)* put_payoff(X[i], K)
    A_co = 1*((np.ones(N-1) * (vol**2 /(2*dx**2)) - ((r-delta)/(2*dx))+ (vol**2/ (4*dx)))*dt/2)# A Vector for the Matrix
    B_co = 1*((np.ones(N-1) * -(vol**2/dx**2) -(r-delta)) *dt/2) +1 # B vector for the Matrix
    C_co = (np.ones(N-1) * vol**2 /(2*dx**2) + ((r-delta)/(2*dx)- (vol**2/ (4*dx))))*dt/2 # C vector for the Matrix
    Matrix = Tridiagonal(B_co,C_co,A_co) # Tridiagonal Matrix
    Matrix1 = Tridiagonal(2-B_co,-C_co,-A_co)
    F[N-2]= (C_co[N-2]*dt)*np.exp(-i*dt)*call_payoff(-K*np.exp(X_max)+K,0)# this is the only one element of this matrix which is non zero,but its value iterates on the time step.
    #print(Matrix)
    b1= np.zeros((N-1,N-1))
    b2= np.zeros((N-1,N-1))
    for i in xrange(0,M):
        b1 = np.dot(Matrix,V_call) + F
        b2 = np.dot(Matrix,V_put) + F
        V_call =SOR(Matrix1,V_call,b1,N-1,w,Kmax) 
        V_put = SOR(Matrix1,V_put,b2,N-1,w,Kmax)
        
    #print(V_call)
    V_call_value= np.interp(S,X,V_call)# interpolation to find the value of S
    V_put_value= np.interp(S,X,V_put)# interploation to find the value of S
    return V_call_value,V_put_value

    
         
  


    
