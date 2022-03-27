#File: ClosedForm.py
# Author: Rajan Puri

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
