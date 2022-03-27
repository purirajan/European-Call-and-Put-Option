Author: Rajan Puri
"""---------------------------------------------------------------------------------------------
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
