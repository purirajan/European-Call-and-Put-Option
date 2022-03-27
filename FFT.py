import numpy as np
from scipy import interpolate
from FourierSeries import*



def A(k0, S0, K, r,delta, sig, T, h, alpha,N):
    a = np.zeros((N))
    k =[]  # List for the Strike Price
    omega =[] # List for the  omega which is obtained by multiplying with "h".
    A =[] # A deontes the  fourier function, integral function. 
    delta_k =float( 2*(np.pi)/(h*N))
    for i in range(N):
        if i==0:
            domega= 0.5*h # doomega is the change in omega.
        else: 
            domega = h
        k.append(k0 + i*delta_k)
        omega.append(i*h)
        A.append(np.exp(1j *omega[i] * k0) * nuhat(omega[i], S0, K, r,delta, sig, T, h, alpha) * domega * N )
    a= np.fft.ifft(A)
    return a,k
def value(k0, S0, K, r,delta, sig, T, h, alpha,N):
    a,k = A(k0, S0, K, r,delta, sig, T, h, alpha,N)
    F=[] # F denotes fourier transform of the A vector.
    V=[] # V denotes the payoff of the European call or put option based on the dumping parameters.
    for i in range(N):
        F.append(a[i])
        V.append(np.real(F[i]) * np.exp(-alpha*k[i]) / pi)
    return V
def P(k0, S0, K, r,delta, sig, T, h, alpha,N):
    a,k = A(k0, S0, K, r,delta, sig, T, h, alpha,N)
    V = value(k0, S0, K, r,delta, sig, T, h, alpha,N)
    f = interpolate.interp1d(k,V) # Generating the function by the interpolation method.
    return f
