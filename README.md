# Dynamic Delta Hedging Simulator & Backtester

## Overview
This project implements a comprehensive **Dynamic Delta Hedging** engine for European Call Options. It bridges theoretical finance with real-world application by offering two distinct modes:
1.  **Monte Carlo Simulation:** Models underlying assets using **Geometric Brownian Motion (GBM)** to test hedging performance under ideal conditions.
2.  **Historical Backtesting:** Tests the strategy against **real market data** (e.g., S&P 500 via Yahoo Finance) to quantify the impact of real-world friction, such as volatility clustering and discrete rebalancing gaps.

The simulation quantifies the **Hedging Error** (P&L variance) caused by Gamma risk and validates the Black-Scholes-Merton assumptions against empirical data.

## Key Features
- **Dual Mode Engine:**
    - *Simulation Mode:* Generates stochastic price paths via GBM to analyze theoretical convergence.
    - *Backtest Mode:* Fetches historical data (OHLC) using `yfinance` to stress-test strategies on actual market scenarios (e.g., SPY, AAPL).
- **Pricing Core:** Modular Black-Scholes pricer calculating implied Greeks (Delta, Gamma, Theta) in real-time.
- **Risk Management:** Simulates dynamic portfolio rebalancing to maintain delta-neutrality, tracking P&L attribution.
- **Volatility Estimation:** Implements realized volatility calculations from log-returns to calibrate the hedging model.

## Tech Stack
- **Language:** Python 3.x
- **Core Libraries:** NumPy (Vectorized calc), SciPy (Stats).
- **Data & Viz:** yfinance (Market API), Matplotlib (Performance visualization).

## Project Structure
The project is designed with a modular architecture to separate the pricing logic from the execution environment.

```text
Delta-Hedging-Simulator/
├── option_models.py       # Core Library: Black-Scholes class & Greeks calculations
├── run_montecarlo.py      # Simulation: Tests hedging on generated GBM paths
├── run_backtest.py        # Backtest: Tests hedging on real historical data (e.g., SPY)
├── requirements.txt       # Dependencies
└── README.md              # Documentation
```

## Mathematical Framework
The simulation relies on the discrete approximation of the Stochastic Differential Equation (SDE):
$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

In the backtesting module, volatility $\sigma$ is estimated via the standard deviation of historical log-returns:
$$R_{log} = \ln\left(\frac{S_t}{S_{t-1}}\right), \quad \sigma_{realized} = \text{std}(R_{log}) \times \sqrt{252}$$

## Future Improvements
- [ ] Implementation of **Gamma Hedging** to neutralize convexity risk.
- [ ] Integration of **GARCH(1,1)** for dynamic volatility forecasting.
- [ ] Transaction cost modeling (Bid-Ask spread simulation).

## Usage

### 1. Run Theoretical Simulation
Simulate a perfect market environment to visualize Delta convergence.
```bash
python run_montecarlo.py
```

### 2. Run Historical Backtest
Test how the strategy would have performed on the S&P 500 (SPY) during 2023.
```bash
python run_backtest.py
```
