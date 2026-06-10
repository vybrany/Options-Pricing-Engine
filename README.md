# Options Pricing Engine

Python project for pricing financial options using analytical and numerical methods commonly used in quantitative finance.

## Objective

The goal of this project is to develop a mini pricing engine capable of valuing vanilla and exotic derivatives while comparing several pricing approaches:

* Black-Scholes analytical pricing
* Cox-Ross-Rubinstein (CRR) binomial tree
* Monte Carlo simulation under Geometric Brownian Motion (GBM)

The project focuses on:

* numerical pricing methods
* convergence analysis
* stochastic simulation
* option sensitivities (Greeks)
* comparison between vanilla and path-dependent products

---

## Implemented Models

| Model             | Products                        |
| ----------------- | ------------------------------- |
| Black-Scholes     | European vanilla options        |
| CRR Binomial Tree | European vanilla + American put |
| Monte Carlo       | Vanilla + Asian + Barrier       |

---

## Features

* Black-Scholes pricing
* Monte Carlo pricing
* Binomial CRR pricing
* American option pricing
* Asian option pricing
* Barrier option pricing
* Greeks calculation
* GBM path simulation
* Monte Carlo convergence analysis
* CRR convergence toward Black-Scholes

---

## Project Structure


├── main.py
├── models.py
├── products.py
├── Greeks.py
├── vizualisation.py
├── values.py
└── README.md


---

## Technologies

* Python
* NumPy
* SciPy
* Pandas
* Matplotlib

---

The user can choose:

* product type
* pricing model
* call or put option

---

## Current Improvements in Progress

* cleaner architecture
* additional Greeks
* improved visualizations
* performance optimization
* extended exotic products
* implied volatility tools

