## Usage Modes

This project includes two distinct execution modes to compare theory vs. reality:

### 1. Market Simulation (Theoretical)
Run `run_montecarlo.py` to simulate hedging under ideal Geometric Brownian Motion conditions.
- **Goal:** Verify the convergence of Delta Hedging to zero P&L in a friction-less, continuous environment.
- **Outcome:** Validates the Black-Scholes assumptions.

### 2. Historical Backtest (Empirical)
Run `run_backtest.py` to test the strategy against real market data (e.g., SPY 2023-2024) via `yfinance`.
- **Goal:** Quantify the impact of discrete rebalancing (Gamma risk) and real-world volatility clustering.
- **Outcome:** Reveals the "Gamma Leakage" (e.g., ~$15 residual P&L on SPY) due to weekly rebalancing gaps.
