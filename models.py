import numpy as np
import time
import scipy.stats as si
import pandas as pd 
from values import values

start = time.time()


def black_scholes(values):
    
    #valeur de réference pour les options européennes
    
    S0, r, sigma, T, I, K, M,B ,dt= values
    d1 = (np.log(S0/K) + (r+sigma**2 / 2)*T ) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call = S0* si.norm.cdf(d1) - K *np.exp(-r*T) * si.norm.cdf(d2)
    put = K *np.exp(-r*T) * si.norm.cdf(-d2) - S0* si.norm.cdf(-d1)
    
    return call, put
    
    
def binomial_crr(values):
    
    S0, r, sigma, T, I, K, M,B ,dt= values
    dt = T/M
    u = np.exp(sigma* np.sqrt(dt))
    d = 1/u
    p = (np.exp(r*dt) - d) / (u - d)
    
    S = np.zeros((M+1,M+1))
    S[0,0]= S0

    z = 1

    for t in range(1,M+1):
        for i in range(z):
            S[i,t] = S[i , t-1]*u
            S[i+1,t] = S[i, t-1]* d
        z += 1

    # option call 
    C = np.zeros((M+1,M+1))
    C[:,M ]= np.maximum(S[:,M]-K, 0)

    for t in range(M-1 , -1 , -1):
        for i in range(t+1):
            C[i,t] = np.exp(-r*dt) * (p*C[i,t+1] + (1-p)*C[i+1,t+1])
            
            
    # option put européenne      
    P = np.zeros((M+1,M+1))
    P[:,M ]= np.maximum(K-S[:,M], 0)

    for t in range(M-1 , -1 , -1):
        for i in range(t+1):
            
            P[i,t] = np.exp(-r*dt) * (p*P[i,t+1] + (1-p)*P[i+1,t+1])
            
            
            
    A = np.zeros((M+1,M+1))
    A[:,M ]= np.maximum(K-S[:,M], 0)
    
    for t in range(M-1 , -1 , -1):
        for i in range(t+1):
            
            continuation = np.exp(-r*dt) * (p*A[i,t+1] + (1-p)*A[i+1,t+1])
            
            exercise = np.maximum(K - S[i, t], 0)
            A[i, t] = max(continuation, exercise)
            




    return C[0,0],  P[0,0],  
    
    
def american(values):
    S0, r, sigma, T, I, K, M, B, dt = values
    dt = T / M

    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    S = np.zeros((M + 1, M + 1))
    S[0, 0] = S0

    z = 1
    for t in range(1, M + 1):
        for i in range(z):
            S[i, t] = S[i, t-1] * u
            S[i+1, t] = S[i, t-1] * d
        z += 1

    A = np.zeros((M + 1, M + 1))
    A[:, M] = np.maximum(K - S[:, M], 0)

    for t in range(M - 1, -1, -1):
        for i in range(t + 1):
            continuation = np.exp(-r * dt) * (
                p * A[i, t+1] + (1 - p) * A[i+1, t+1]
            )

            exercise = np.maximum(K - S[i, t], 0)

            A[i, t] = max(continuation, exercise)

    return A[0, 0]
    
    
    
    
    
def monte_carlo (values):
    
    S0, r, sigma, T, I, K, M,B ,dt= values
    dt = T/M

    S = np.zeros((M+1,I))
    S[0]= S0

    rn = np.random.normal(0,1,(M+1,I))

    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2) * dt+ sigma * np.sqrt(dt) * rn[t])
            

    C0 = np.exp(-r*T)* np.mean(np.maximum(S[-1]-K,0))
    P0 = np.exp(-r*T)* np.mean(np.maximum(K - S[-1],0))
    
    return C0 , P0, S
    

def monte_carlo_asian (values):
    
    S0, r, sigma, T, I, K, M,B ,dt= values
    dt = T/M

    S = np.zeros((M+1,I))
    S[0]= S0

    rn = np.random.normal(0,1,(M+1,I))

    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2) * dt+ sigma * np.sqrt(dt) * rn[t])
                
    average = np.mean(S[1:],axis= 0)

    C0 = np.exp(-r*T)* np.mean(np.maximum(average-K,0))
    P0 = np.exp(-r*T)* np.mean(np.maximum(K - average,0))
        
    return C0 , P0


def up_and_out(values):
    S0, r, sigma, T, I, K, M,B,dt = values

    S = np.zeros((M+1,I))
    S[0]= S0

    rn = np.random.normal(0,1,(M+1,I))

    for t in range(1, M + 1):
        S[t] = S[t-1] * np.exp((r - 0.5 * sigma**2) * dt+ sigma * np.sqrt(dt) * rn[t])
                


    maxpath = np.max(S , axis=0, )
    barrier = maxpath >= B 


    payoffcall = np.maximum(S[-1]-K,0)
    payoff = np.where(barrier,0 , payoffcall)
    call = np.exp(-r*T)*np.mean(payoff)


    payoffput = np.maximum(K - S[-1],0)
    payoff = np.where(barrier,0 , payoffput)
    put = np.exp(-r*T)*np.mean(payoff)
    
    return call, put


def callputparity(values):
    S0, r, sigma, T, I, K, M,B ,dt= values
    call , put = black_scholes(values)
    part1 = call - put 
    part2 = S0 - K*np.exp(-r*T)
    if np.isclose(part1 , part2):
        print("Parity Ok")
    else:
        print("Parity Not Ok")

      
    
"""print("-"*60)
print("-"*60)

callputparity(values())
print("-"*60)

print(black_sholes(values()), "Valeur de reférence")
print("-"*60)

print(binomial_crr(values()), "Arbre_CCR")
print("-"*60)

print(monte_carlo(values()), "Monte Carlo")
print("-"*60)

print(monte_carlo_asian(values()), "Monte Carlo Asian")
print("-"*60)

print(up_and_out(values()), "Up and Out")
print("-"*60)

print(time.time() - start, "secondes")"""