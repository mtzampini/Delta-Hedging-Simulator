import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from option_model import EuropeanCall


# import the market
ticker = 'SPY'
data = yf.download(ticker, start="2023-01-01", end="2024-01-01")['Close']
stock_prices = data.values.flatten()

# parameters
S0 = stock_prices[0]                # initial stock price
K = stock_prices[0]                 # strike price
T = 1.0                             # time to expiration (years)
r = 0.05                            # risk-free rate
n_steps =  len(stock_prices) - 1    # hedge rebalanced daily

dt = T / n_steps

log_returns = np.log(data/data.shift(1)).dropna()
realized_vol = log_returns.std().values[0] * np.sqrt(252)

# initializing the portfolio selling an option
option_at_start = EuropeanCall(S0, K, T, r, realized_vol)
initial_option_price = option_at_start.price()
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
    opt = EuropeanCall(current_S, K, current_time_left, r, realized_vol)
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