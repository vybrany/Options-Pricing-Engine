import numpy as np
import scipy.stats as si
from values import values




def delta(values):
    S0, r, sigma, T, I, K, M,B ,dt= values
    d1 = (np.log(S0/K) + (r+sigma**2 / 2)*T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    delta_call = si.norm.cdf(d1)
    delta_put = delta_call -1
    return delta_call , delta_put

def gamma(values):
    S0, r, sigma, T, I, K, M,B ,dt= values
    d1 = (np.log(S0/K) + (r+sigma**2 / 2)*T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    gamma = si.norm.pdf(d1)/(S0*sigma*np.sqrt(T))
    return gamma

def vega(values):
    S0, r, sigma, T, I, K, M,B ,dt= values
    d1 = (np.log(S0/K) + (r+sigma**2 / 2)*T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    vega = S0 * si.norm.pdf(d1) * np.sqrt(T)
    return vega

def theta(values):
    S0, r, sigma, T, I, K, M,B ,dt= values
    d1 = (np.log(S0/K) + (r+sigma**2 / 2)*T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)   
    
    theta_call = (-(S0 * si.norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * si.norm.cdf(d2))

    theta_put = (-(S0 * si.norm.pdf(d1) * sigma) / (2 * np.sqrt(T))+ r * K * np.exp(-r*T) * si.norm.cdf(-d2))

    return theta_call, theta_put


