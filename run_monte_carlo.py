import numpy as np
import matplotlib.pyplot as plt
from option_model import EuropeanCall

def generate_asset_path(S0, T, r, sigma, n_steps):
    # generate an asset path assuming geometric brownian motion
    dt = T / n_steps
    prices = [S0]

    for _ in range(n_steps):
        # generate a random number from a Normal(0, 1)
        z = np.random.normal(0, 1)

        S_prev = prices[-1]

        S_new = S_prev * np.exp((r - 0.5 * (sigma ** 2))* dt + sigma * np.sqrt(dt) * z)
        prices.append(S_new)
    
    return np.array(prices)

import matplotlib.pyplot as plt

# parameters
S0 = 100      # initial stock price
K = 100       # strike price
T = 1.0       # time to expiration (years)
r = 0.05      # risk-free rate
sigma = 0.2   # volatility
n_steps = 52  # hedge rebalanced every week, 53 weeks

dt = T / n_steps

# generate the market
stock_prices = generate_asset_path(S0, T, r, sigma, n_steps)

# initializing the portfolio selling an option
option_at_start = EuropeanCall(S0, K, T, r, sigma)
initial_option_price = option_at_start.price()

# hedging portfolio
cash_account = initial_option_price
stock_holding = 0

# lists for graphs
portfolio_values = []
times = np.linspace(0, T, n_steps + 1)

print("Starting hedging simulation...")

# hedging loop
for i in range(n_steps):
    current_S = stock_prices[i]
    current_time_left = T - times[i]

    # today's delta
    opt = EuropeanCall(current_S, K, current_time_left, r, sigma)
    current_delta = opt.delta()


    desired_stock = current_delta
    trade_size = desired_stock - stock_holding

    cost = trade_size * current_S
    cash_account -= cost
    stock_holding += trade_size

    hedge_value = (stock_holding * current_S) + cash_account
    option_market_value = opt.price()

    total_pnl = hedge_value - option_market_value
    portfolio_values.append(total_pnl)

# last step (expiry date)
final_S = stock_prices[-1]
final_payoff = max(final_S - K, 0)
final_pnl = (stock_holding * final_S) + cash_account - final_payoff

portfolio_values.append(final_pnl)

print(f"Final P&L (Hedging Error): {final_pnl: .4f}")

# graph
plt.figure(figsize=(10, 6))
plt.plot(portfolio_values, label='Hedging P&L')
plt.axhline(0, color='red', linestyle='--', label='Target (0)') # reference line
plt.title('Delta Hedging Simulation (Weekly Rebalancing)')
plt.xlabel('Weeks')
plt.ylabel('P&L ($)')
plt.legend()
plt.grid(True)
plt.show()