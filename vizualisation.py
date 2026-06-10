import numpy as np
import matplotlib.pyplot as plt

from models import monte_carlo, binomial_crr, black_scholes
from values import values


def plot_gbm_paths(values, n_paths=20):
    C0, P0, S = monte_carlo(values)

    plt.figure(figsize=(12, 8))
    plt.plot(S[:, :n_paths])

    plt.title("Simulated GBM Paths")
    plt.xlabel("Time steps")
    plt.ylabel("Underlying price")
    plt.grid(True)
    plt.show()




def monte_carlo_vs_BSM(values):
    S0, r, sigma, T, I, K, M, B, dt = values

    call_bs, put_bs = black_scholes(values)

    monte_carlo_price = []
    simulations_list = [50,100,300, 500, 800, 1000,2000,3500, 5000,7000, 9000, 10000,12000]

    for I_new in simulations_list:
        I = I_new
        new_values = S0, r, sigma, T, I, K, M, B, dt
        C0 , PO , S = monte_carlo(new_values)
        monte_carlo_price.append(C0)
   
    
    
    plt.figure(figsize=(12, 8))

    plt.plot(simulations_list, monte_carlo_price, marker="o", label="Monte Carlo Call")
    plt.axhline(call_bs, linewidth=3, label="Black-Scholes Call")

    plt.title("Monte Carlo convergence toward Black-Scholes")
    plt.xlabel("Number of simulations")
    plt.ylabel("Call price")
    plt.grid(True)
    plt.legend()
    plt.show()
    

def CRR_vs_BSM(values):
    S0, r, sigma, T, I, K, M, B, dt = values

    call_bs, put_bs = black_scholes(values)

    crr_prices = []
    steps_list = [5, 10, 25, 50, 100, 250, 500, 1000]

    for M_new in steps_list:
        dt_new = T / M_new
        new_values = S0, r, sigma, T, I, K, M_new, B, dt_new

        call_crr, put_crr = binomial_crr(new_values)

        crr_prices.append(call_crr)

    plt.figure(figsize=(12, 8))

    plt.plot(steps_list, crr_prices, marker="o", label="CRR Call")
    plt.axhline(call_bs, linewidth=3, label="Black-Scholes Call")

    plt.title("CRR convergence toward Black-Scholes")
    plt.xlabel("Number of time steps")
    plt.ylabel("Call price")
    plt.grid(True)
    plt.legend()
    plt.show()


CRR_vs_BSM(values())
monte_carlo_vs_BSM(values())
plot_gbm_paths(values())