"""
Extra Task 1 — Functions from scratch (no hints)

  Write these 4 functions, test each with 3 inputs:

  log_return

  annualise_sharpe

  is_above_threshold(value, threshold=0.05)
  → returns True if value > threshold, False otherwise

  compound_growth
"""
print("")
print("Task 1 Functions from scratch")
print("")
import math
def log_return(current, previous):
    log_ret = math.log(current/previous)
    return log_ret
prices = [120,121,124,123,120,128,134]
log_returns = []
for i in range(1, len(prices)):
    value = log_return(prices[i], prices[i-1])
    log_returns.append(value)
print(f" The log returns of the first tested price list:")
print([f'{p:.4f}' for p in log_returns])
print("---")

prices1 = [99,97,95,106,120]
log_returns1 = []
for i in range(1, len(prices1)):
    value1 = log_return(prices1[i], prices1[i-1])
    log_returns1.append(value1)
print("List of log returns from the second tested list off prices:")
print([f'{p:.4f}' for p in log_returns1])
print("---")

prices2 = [12,20,50,20,70]
log_returns2 = []
for i in range(1, len(prices2)):
    value2 = log_return(prices2[i], prices2[i-1])
    log_returns2.append(value2)
print(f"The log returns list test from the tested prices list")
print([f'{p:.2f}' for p in log_returns2])
print(f"----")

def annualise_sharpe(daily_sharpe):
    return daily_sharpe * math.sqrt(252)

print(f"annualised sharpe of daily sharpe of 0.05: {annualise_sharpe(0.05):.2f}")
print(f"annualised sharpe of daily sharpe of 0.12: {annualise_sharpe(0.12):.2f}")
print(f"annualised sharpe of daily sharpe of 0.16: {annualise_sharpe(0.16):.2f}")

print("---")
#  is_above_threshold(value, threshold=0.05)
#   → returns True if value > threshold, False otherwise
def is_above_threshold(value, threshold = 0.05):
    return value > threshold
print(f"is a value 0.07 above threshold?: {is_above_threshold(0.07)}")
print(f"is a value 0.17 above threshold?: {is_above_threshold(0.17)}")
print(f"is a value 0.01 above threshold?: {is_above_threshold(0.01)}")
print("---")

def compound_growth(principal, rate, time):
    return principal*(1+rate)**time
print(f"compound growth of the investment with principal = $100, rate = 0.05, 1 year: ${compound_growth(100, 0.05, 1):,.2f}")
print(f"compound growth of the investment with principal = $3_000, rate = 0.04,  6 months: ${compound_growth(3_000, 0.04, 0.5):,.2f}")
print(f"compound growth of the investment with principal = $10_000, rate = 0.06, 3 year: ${compound_growth(10_000, 0.06, 3):,.2f}")
print("---")



"""
Extra Task 2 — float('inf') sentinel pattern
  
  pnl = [320, -150, 870, -420, 610, -80, 1200, -330]

  Using float('inf') and float('-inf'), write a loop that finds:
  - best trade value and its index
  - worst trade value and its index
  
  Print:
  "Best trade:  $1,200 at index 6"
  "Worst trade: $-420 at index 3"

  ---"""
print("")
print("Task 2 — float('inf') sentinel pattern")
print("")

pnl = [320, -150, 870, -420, 610, -80, 1200, -330]

best_trade_v = float('-inf')
best_trade_index = 0
worst_trade_v = float('inf')
worst_trade_index = 0

for i in range(len(pnl)):
    if best_trade_v < pnl[i]:
       best_trade_v = pnl[i]
       best_trade_index = i
for p in range(len(pnl)):
    if worst_trade_v > pnl[p]:
        worst_trade_v = pnl[p]
        worst_trade_index = p
print(f"Best trade: ${best_trade_v:,.2f}, at index {best_trade_index}")
print(f"Worst trade: ${worst_trade_v:,.2f} at index {worst_trade_index}")

"""
Extra Task 3 — Lambda

  Write lambdas for:
  abs_return  → absolute value of a return
  log_ret     → log return from two prices
  is_loss     → True if return is negative
  weight      → position_value / total (two parameters)

  Then:
  trades = [("MSFT", 0.032), ("AAPL", -0.018), ("NVDA", 0.071), ("TSLA", -0.044)]

  - Sort by return ascending
  - Sort by absolute return descending (biggest move first, sign ignored)
  - Print ticker with best return using max()
  - Print ticker with worst return using min()
"""

print("")
print("Task 3 — Lambda")
print("")

abs_return = lambda r: abs(r)
log_ret = lambda current,previous: math.log(current/previous)
is_loss = lambda n: n < 0
weight = lambda position_value,total_value: position_value / total_value

trades = [("MSFT", 0.032), ("AAPL", -0.018), ("NVDA", 0.071), ("TSLA", -0.044)]
print(f"Trades: {trades}")
print('')
print("Sorted by return ascending:")
ascending = sorted(trades, key= lambda n: n[1])
print(ascending)

print(f"First option of writing descending removing the sign using abs(): ")
descending = sorted(trades, key=lambda p: abs(p[1]), reverse = True)
print(descending)
print('')
absolute_return_trades = []
for p in trades:
    absolute_return_trades.append((p[0], abs(p[1])))

print("Second option of writing descending removing the sign using abs() in one line:")
descending2 = sorted(absolute_return_trades, key=lambda p:p[1], reverse=True)
print(descending2)
print('')

maximum = max(trades, key=lambda p: p[1])
print(f"Ticker with maximum trade is: {maximum[0]}")
minimum = min(trades, key=lambda p: p[1])
print(f"Ticker with minimum trade is: {minimum[0]}")

"""
Extra Task 4 — Functions calling functions + list of dicts
  portfolio = [
      {"ticker": "IGN1L", "buy_price": 14.20, "current_price": 15.80, "shares": 100},
      {"ticker": "SAB1L", "buy_price": 31.50, "current_price": 29.40, "shares": 50},
      {"ticker": "TEL1L", "buy_price": 8.90,  "current_price": 9.75,  "shares": 200},
      {"ticker": "OMXV",  "buy_price": 890.0, "current_price": 910.0, "shares": 10},
  ]
  Write:
  - pnl(stock)            → (current_price - buy_price) × shares  for one stock dict
  - total_pnl(portfolio)  → calls pnl() for each stock, returns sum
  - best_stock(portfolio)  → uses max() with lambda, returns dict of best performer
  - worst_stock(portfolio) → uses min() with lambda
  Print each ticker, its P&L, which is best and which is worst.
"""

print("")
print("Task 4 — Functions calling functions + list of dicts")
print("")
portfolio = [
      {"ticker": "IGN1L", "buy_price": 14.20, "current_price": 15.80, "shares": 100},
      {"ticker": "SAB1L", "buy_price": 31.50, "current_price": 29.40, "shares": 50},
      {"ticker": "TEL1L", "buy_price": 8.90,  "current_price": 9.75,  "shares": 200},
      {"ticker": "OMXV",  "buy_price": 890.0, "current_price": 910.0, "shares": 10},
  ]
def pnl(stock):
   return (stock["current_price"] - stock["buy_price"]) * stock["shares"]

def total_pnl(portfolio):
    total = 0
    for stock in portfolio:
        total += pnl(stock)
    return total

def best_stock(portfolio):
    best = max(portfolio, key=lambda stock: pnl(stock))
    return best["ticker"]


def worst_stock(portfolio):
    worst = min(portfolio, key=lambda stock: pnl(stock))
    return worst["ticker"]
print("---")
print(f"Tickers + P&l")
for stock in portfolio:
    print(f"{stock['ticker']}: ${pnl(stock):,.2f}")
print("")
print(f"Total P&L: ${total_pnl(portfolio):,.2f}")
print(f"Best: {best_stock(portfolio)}")
print(f"Worst: {worst_stock(portfolio)}")




