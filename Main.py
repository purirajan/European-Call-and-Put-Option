Purpose:  This program will find the value of the European call and put option according to the 
                 Finite difference method.
	            
	Algorithm: Finite difference (FD) methods are used to numerically approximate the solutions of 
                 partial differential equations. We start by establishing a rectangular solution domain
                 in the two variables, S and t. We then form finite difference approximations to each of
                 the derivative terms in the PDE. FD methods create a mathematical relationship which links
                 together every point on the solution domain, like a chain. The first links in the chain 
                 are the boundary conditions and from these, we discover what every other point in the 
                 domain has to be. We used FD Explicit Euler, Implicit Euler, and the Crank-Nicolson method.
                 The easiest scheme of the three to implement is the Explicit Euler method. Implicit Euler
                 and Crank-Nicolson are implicit methods, which require a system of linear equations to be
                 solved at each time step, which can be computationally intensive on a fine mesh. The Explicit
                 Euler is that it is unstable for certain choices of domain discretization. Though Implicit 
                 Euler and Crank-Nicolson involve solving linear systems of equations, they are each
                 unconditionally stable with respect to the domain discretization. Crank-Nicolson exhibits the
                 greatest accuracy of the three for a given domain discretization.

	
	Arguments: S =120 # Stock Price
                 K = 100 # Strike price
                 X_max = 2.5# X-domain Max value
                 X_min = -2.5 # X-domain min value
                 T    = 1 # maturity date
                 mu = 0.05 # mean return
                 dx   = 0.05 # space step
                 r = 0.02 # risk free interest rate
                 delta  = 0.01 # dividend yield
                 vol = 0.5 # volatility
                 dt = 0.00125 # time steps
                
     Analytical Solution: 
                 The main disadvantage to using Explicit Euler is that it is unstable for certain 
                 choices of domain discretisation.Though Implicit Euler and Crank-Nicolson involve 
                 solving linear systems of equations,they are each unconditionally stable with respect
                 to the domain discretisation. 
	---------------------------------------------------------------------------------------------"""
 
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from ExplicitFDM import*
from CrankNicholsonBrenSchwartz import*
from CrankNicholsonProjectedSOR import*
from CrankNicholsonThomas import*
from Thomas import*
from SOR import*
from ImplicitFDM import*
from ImplicitFDMThomas import*
from ImplicitFDMSOR import*
from ImplicitFDMProjectedSOR import*
from ImplicitFDMBrennanSchwartz import*
from MonteCarlo import*
from Payoff import*
from RegressionI import*
from RegressionII import*
from Tridiagonal import*
from FFT import*
from FourierSeries import*


def main():
    S =120 # Stock Price
    K = 100 # Strike price
    X_max = 2.5# X-domain Max value
    X_min = -2.5 # X-domain min value
    T     = 1 # maturity date
    mu = 0.05 # mean return
    dx   = 0.05 # space step
    r = 0.02 # risk free interest rate
    delta  = 0.01 # dividend yield
    vol = 0.5 # volatility
    dt = 0.00125 # time steps
    w = 1.10 # relaxation parameter
    tol= 10**(-6)
    Kmax = 1000 # iteration
    N = 500 # sample paths
    M = 800
    print("\n\n*************** Finite Differnce Method *************************")
    print ('\nParameters:\n')
    print ('     S=%g, K=%g, T=%g, r=%g, delta=%g, vol=%g' % (S, K, T, r, delta, vol))
    print ('\n%14s %20s   %12s' %('Finite Difference Method','Eur Call Price', 'Eur Put Price'))
    #######################################################################
    vc= 33.320944 # closed form solution for call option
    vp= 12.534831# closed from solution for put option
    V_call_value,V_put_value = ExplicitFDM(X_max,X_min,dx,T,dt,K,r,vol,delta,S)
    print ('\n%16s %26.6f %16.6f' % ('ExplicitFDM',V_call_value,V_put_value))
    print ('\n%16s %26.6f %16.6f' % ('Error      ',abs(V_call_value-vc),abs(V_put_value-vp)))
    #############################################################################
    V_call_value,V_put_value = ImplicitFDM(X_max,X_min,dx,T,dt,K,r,vol,delta,S)
    print ('\n%16s %26.6f %16.6f' % ('ImplicitFDM',V_call_value,V_put_value))
    print ('\n%16s %26.6f %16.6f' % ('Error      ',abs(V_call_value-vc),abs(V_put_value-vp)))
    ###########################################################################
    V_call_value,V_put_value = ImplicitFDMThomas(X_max,X_min,dx,T,dt,K,r,vol,delta,S)
    print ('\n%16s %25.6f %16.6f' % ('ImplicitFDMTHomas',V_call_value,V_put_value))
    print ('\n%16s %26.6f %16.6f' % ('Error      ',abs(V_call_value-vc),abs(V_put_value-vp)))
    ###########################################################################
    V_call_value,V_put_value = ImplicitFDMSOR(X_max,X_min,dx,T,dt,K,r,vol,delta,S,w,Kmax)
    print ('\n%16s %26.6f %16.6f' % ('ImplicitFDMSOR',V_call_value,V_put_value))
    print ('\n%16s %26.6f %16.6f' % ('Error      ',abs(V_call_value-vc),abs(V_put_value-vp)))
    ###########################################################################
    V_call_value,V_put_value = CrankNicholsonThomas(X_max,X_min,dx,T,dt,K,r,vol,delta,S)
    print ('\n%16s %22.6f %16.6f' % ('CrankNIcholsonTHomas',V_call_value,V_put_value))
    print ('\n%16s %26.6f %16.6f' % ('Error      ',abs(V_call_value-vc),abs(V_put_value-vp)))
    print("\n**************************************************************")
    print ('\n%14s %23s   %12s' %('Finite Difference Method','Amr Call Price', 'Amr Put Price'))
    #########################################################################
    V_call_value,V_put_value = ImplicitFDMBrennanSchwartz(X_max,X_min,dx,T,dt,K,r,vol,delta,S)
    print ('\n%16s %17.6f %16.6f' % ('ImplicitFDMBrennanSchwartz',V_call_value,V_put_value))
    ##########################################################################
    V_call_value,V_put_value = CrankNicholsonBrenSchwartz(X_max,X_min,dx,T,dt,K,r,vol,delta,S)
    print ('\n%16s %14.6f %16.6f' % ('CrankNicholsonBrennanSchwartz',V_call_value,V_put_value))
    #########################################################################
    V_call_value,V_put_value = CrankNicholsonProjectedSOR(X_max,X_min,dx,T,dt,K,r,vol,delta,S,w,Kmax)
    print ('\n%16s %17.6f %16.6f' % ('CrankNicholsonProjectedSOR',V_call_value,V_put_value))
    ########################################################################
    V_call_value,V_put_value = ImplicitFDMProjectedSOR(X_max,X_min,dx,T,dt,K,r,vol,delta,S,w,Kmax)
    print ('\n%16s %20.6f %16.6f' % ('ImplicitFDMOrojectedSOR',V_call_value,V_put_value))
    #########################################################################

main()
################################################################################

print("\n\n************ Regression and MonteCarlo Method *********************")
# Author: Rajan Puri
# Date: 12/05/2015
#Email: rpuri7@uncc.edu
"""---------------------------------------------------------------------------------------------
	Purpose:  
                We are going to program Monte Carlo simulation in Python for computing the values of an
                American call and put. The call or put option is written on an underlying asset, which follows a
                geometric Brownian motion,

	                 dSt = (mu-delta)*St*dt + sigma*St*dW
	           
                where St is the time t value of the underlying asset, mu is mean return, delta is a continuously compounded
                dividend yield, sigma is volatility, and Wt is a Wiener process with W0 = 0.
                Then values of the two American options are determined by their discounted risk-neutral expectations:
	            
	Algorithm: The computation involves a built-in fucntion, scipy.stats.norm.cdf(x), to compute standard cumulative normal
	           distribution  and change in weiner process. 
                We generate sample paths for St,and we  have used explicit Euler method.
                
	
	Arguments: S - Price of underlying asset at time t = 0.
	           K - Strike price
	           T - Maturity date, measured in fraction (or a multiple) of a year. T > 0
	           sigma - Standard deviation of log (S)
	           delta - Dividend yield rate (dividends are paid continuously over time)
                 r - interest rate
	
	Usage:	   
                   S0 = 120 # initial stock price
                   K = 100  # strike price
                   T = 1.0 # maturity time
                   sigma = 0.5 # volatility
                   delta= 0.01 # time continous dividend yield
                   r = 0.02 # interest rate
                   mu = 0.05 #return rate
             
	---------------------------------------------------------------------------------------------"""
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from RegressionII import*
from RegressionI import*
from MonteCarlo import*

def main():
    N=500
    S =120 # Stock Price
    K = 100 # Strike price
    T = 1 # maturity date
    mu = 0.05 # mean return
    r = 0.02 # risk free interest rate
    delta  = 0.01 # dividend yield
    vol = 0.5 # volatility
    dt = 0.00125 # time steps
    M=int((T)/dt)
    np.random.seed(100)
    
    print ('\nParameters:\n')
    print ('     S=%g, K=%g, T=%g, r=%g, delta=%g, vol=%g' % (S, K, T, r, delta, vol))
    print ('\n%14s %20s   %12s' %('Regression Method','Amr Call Price', 'Amr Put Price'))
    V_call_value,V_put_value = RegressionII(S,r,K,delta,vol,dt,T,N,M)
    print ('\n%16s %20.6f %16.6f' % ('RegressionII',V_call_value,V_put_value))
    V_call_value,V_put_value = RegressionI(S,r,K,delta,vol,dt,T,N,M)
    print ('\n%16s %20.6f %16.6f' % ('Regression I',V_call_value,V_put_value))
    
    print ('\n%14s %22s   %12s' %('Method','Eur Call Price', 'Eur Put Price'))
    vc= 33.320944 # closed form solution for call option
    vp= 12.534831# closed from solution for put option
    V_call_value,V_put_value = MonteCarlo(S,r,K,delta,vol,dt,T,N,M)
    print ('\n%16s %20.6f %16.6f' % ('MonteCarlo',V_call_value,V_put_value))
    print ('\n%16s %19.6f %16.6f' % ('Error      ',abs(V_call_value-vc),abs(V_put_value-vp)))
    
main()

print("\n\n******************* Fast Fourier Transform ************************")
#File: mainFFT.py
# Author: Rajan Puri
# Date: 12/3/2015
#Email: rpuri7@uncc.edu
"""---------------------------------------------------------------------------------------------
	Purpose:  This program will find the value of the european call option and put option on the underlyting assest S that 
               follows a geometric brownian motion through the fourier series by using Fast Fourier Transform.
	            
	Algorithm: Using Fast fourier transform to find the European call option or put option based on the 
                 dumping parameters(alpha value) as positive or negative.Positive value of alpha implies the European call
                 option and negative value of alpha denotes the European put option.
                
	
	Arguments: S - Price of underlying asset at time t = 0.
	           K - Strike price
	           T - Maturity date, measured in fraction (or a multiple) of a year. T > 0
	           sigma - Standard deviation of log (S)
	           r - interest rate
	Usage:	   
                S0 = 120 # initial stock price
                K = 100  # strike price
                T = 1.0 # maturity time
                sigma = 0.5 # volatility
                r = 0.02 # interest rate  
                
    Analytical Solutions:
            Positive  and Negative value of damping parameters respectively give the 
            values of European Call option and Put option. Their role is not significant,
            but plugging the very small and big dammping parameters affect the result very
            significantly. In our problem, we are getting the same outputs although damping 
            parametrs are different.
                     
                     
	---------------------------------------------------------------------------------------------"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from FourierSeries import*
from FFT import*

def main():
    alpha1 = -2.5 ## dumping parameters
    alpha = 2.5
    B = 100.0 
    N = 2**12 
    S0 = 120.0 # initial Stock Price
    x0 = np.log(S0)
    K = 100.0 # Strike Price
    K0 =20
    delta = 0.01
    r = 0.02 # rate of interest
    sig = 0.50 # Volatility
    T = 1.0 # Maturity Date
    h = float(B)/(N-1) 
    k0 =np.log(K0) # mimimum value of K
    delta_k =float( 2*(np.pi)/(h*N))
    V = []
    k_n=[]
    for i in range(N):
        k_n.append(k0 + i*delta_k)

    print ('Parameters:\n')
    print ('     S0=%g, K=%g, T=%g, r=%g, delta =%g, sigma=%g, B=%g, N=%g' % (S0, K, T, r, delta, sig, B, N))
    print ('\n%15s   %16s ' %('Alpha Value', 'Eur Put Price'))
  ############################################################################  
    #for alpha in Alpha:
    V = value(k0, S0, K, r,delta, sig, T, h, alpha1,N)
    f = P(k0, S0, K, r,delta, sig, T, h, alpha1,N)
    k = A(k0, S0, K, r,delta, sig, T, h, alpha1,N)
    print ('%12.1f %16.6f' % (alpha1,f(np.log(K))))
    
##############################################################################
    print ('\n%15s   %16s ' %('Alpha Value', 'Eur Call Price'))     
    #for alpha in Alpha1:
    V = value(k0, S0, K, r,delta, sig, T, h, alpha,N)
    f = P(k0, S0, K, r,delta, sig, T, h, alpha,N)
    k = A(k0, S0, K, r,delta, sig, T, h, alpha,N)
    print ('%12.1f %16.6f' % (alpha,f(np.log(K))))
 
   
   
   
main()

print("\n\n***************** Closed Form Solution ***************************")
#File: ClosedForm.py
# Author: Rajan Puri
# Date: 12/05/2015
#Email: rpuri7@uncc.edu
"""---------------------------------------------------------------------------------------------
	Purpose:  
                We are going to find the closed form solutions of the European call option values.
                The call or put option is written on an underlying asset, which follows a
                geometric Brownian motion,

	                 dSt = (mu-delta)*St*dt + sigma*St*dW
	           
                where St is the time t value of the underlying asset, mu is mean return, delta is a continuously compounded
                dividend yield, sigma is volatility, and Wt is a Wiener process with W0 = 0.        
	            
	Algorithm: The computation involves a built-in fucntion, scipy.stats.norm.cdf(x), to compute standard cumulative normal
	           distribution  and change in weiner process. 

	
	Arguments: S - Price of underlying asset at time t = 0.
	           K - Strike price
	           T - Maturity date, measured in fraction (or a multiple) of a year. T > 0
	           sigma - Standard deviation of log (S)
	           delta - Dividend yield rate (dividends are paid continuously over time)
                 r - interest rate
	
	Usage:	   
                   S0 = 120 # initial stock price
                   K = 100  # strike price
                   T = 1.0 # maturity time
                   sigma = 0.5 # volatility
                   delta= 0.01 # time continous dividend yield
                   r = 0.02 # interest rate
                   mu = 0.05 #return rate                       
	---------------------------------------------------------------------------------------------"""

import numpy as np
import scipy.stats as ss 

def d1(S, K, r, delta, sigma, T):
    return (np.log(S/K) + (r -delta + sigma**2 / 2) * T)/(sigma * np.sqrt(T))
 
def d2(S, K, r, delta, sigma, T):
    return (d1(S, K, r,delta, sigma, T) - (sigma * np.sqrt(T)))
    
def main():
    
    S= 120.0 # S denotes the stock price.
    K= 100.0 # K denotes the strike price.
    T=1.0 # T denotes the maturity period.
    r= 0.02 # r denotes the rate of interest.
    delta = 0.01 # delta denotes the time continous divident yield.
    sigma = 0.5 # sigma is volatility.
    # F() is the standard normal cumulative distribution = ss.norm.cdf()
    # vc denotes the European call option at the present time( t=0).
    # vp denotes the European put option at the present time(t=0).
    vc= S * ss.norm.cdf(d1(S, K, r, delta, sigma, T)) * np.exp((-delta) * T) - K * np.exp(-r * T) * ss.norm.cdf(d2(S, K, r,delta, sigma, T))
    vp= -S * ss.norm.cdf(-d1(S, K, r, delta, sigma, T)) * np.exp((-delta) * T) + K * np.exp(-r * T) * ss.norm.cdf(-d2(S, K, r,delta, sigma, T))
    print ('\nParameters:\n')
    print ('     S=%g, K=%g, T=%g, r=%g, delta= %g, sigma=%g' % (S, K, T, r, delta, sigma))
    print ('\n%15s   %12s   %12s' %('Volatility', 'Eur Call Price', 'Eur Put Price'))
    print ('%12.1f %16.6f %16.6f' % (sigma,vc, vp))


main()

print("\n********************************************************************")

 #############################################################################   
