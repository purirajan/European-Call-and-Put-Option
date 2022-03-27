import numpy as np
from math import pi
def nuhat(omega, S0, K, r, delta, sig, T, h, alpha):
    a  = np.exp(-r * T) * qhat(omega, S0, K, r,delta, sig, T,alpha)
    b = (alpha - 1j * omega) * (alpha - 1j * omega + 1.0)
    return a / b
def qhat(omega, S0, K, r,delta, sig, T,alpha): 
    x0 = np.log(S0)
    k = np.log(K)
    omega2 = omega + (alpha + 1.0) * 1j
    a = x0 + ((r-delta) - sig*sig / 2.0) * T
    b = sig * sig * T /2.0

    return np.exp(-1j * a * omega2 - b * omega2 **2)
