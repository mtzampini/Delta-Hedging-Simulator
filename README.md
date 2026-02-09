# Dynamic Delta Hedging Simulator

## Overview
This project simulates a dynamic hedging strategy for European Call Options. It models the underlying asset using **Geometric Brownian Motion (GBM)** and implements a discrete-time **Delta Hedging** strategy based on the **Black-Scholes-Merton** framework.

The simulation quantifies the **Hedging Error** introduced by discrete rebalancing (gamma risk) and visualizes the P&L distribution of the hedged portfolio over time.

## Key Features
- **Market Simulation:** Generates stochastic price paths via GBM.
- **Pricing Engine:** Implements closed-form Black-Scholes pricing and Greeks derivation (Delta).
- **Risk Management:** Simulates weekly portfolio rebalancing to maintain delta-neutrality.
- **Analytics:** Visualizes the convergence of the hedged portfolio vs. theoretical risk-free growth.

## Tech Stack
- **Language:** Python 3.x
- **Libraries:** NumPy (Vectorized calc), SciPy (Stats), Matplotlib (Visualization)

## Mathematical Framework
The simulation relies on the discrete approximation of the SDE:
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$
Where hedging positions are updated at discrete intervals $\Delta t$, leading to a non-zero P&L variance due to convexity (Gamma).

## Future Improvements
- [ ] Integration of Transaction Costs models.
- [ ] Implementation of Reinforcement Learning (DQN) for optimal hedging under friction.
- [ ] Comparison with localized volatility models.
