"""
Task 1 — Functions from scratch

  Write these 4 functions, test each with 3 inputs:

  simple_return(current, previous)
  → (current - previous) / previous

  annualise_vol(daily_vol)
  → daily_vol * sqrt(252)

  is_profitable(pnl)
  → True if pnl > 0

  future_value(principal, rate, years)
  → principal * (1 + rate)^years
"""
print("")
print("Task 1 — Functions from scratch")
print("")
import math
def simple_return(current, previous):
    return (current-previous)/previous
print("---")
print(f"Simple return of [10, 12]: {simple_return(12,10):,.4f}")
print(f"Simple return of [10, 7]: {simple_return(7,10):,.4f}")
print(f"Simple return of [10, 20]: {simple_return(20,10):,.4f}")

def annualise_vol(daily_vol):
    return daily_vol * math.sqrt(252)
print("---")
print(f"Annualised daily volatility of 2.3: {annualise_vol(2.3):.2f}")
print(f"Annualised daily volatility of 1.0: {annualise_vol(1.0):.2f}")
print(f"Annualised daily volatility of 3.3: {annualise_vol(3.3):.2f}")

def is_profitable(pnl):
    return pnl > 0
print("---")
print(f"Is portfolio profitable if pnl = 0.4: {is_profitable(0.4)}")
print(f"Is portfolio profitable if pnl = 0.6: {is_profitable(0.6)}")
print(f"Is portfolio profitable if pnl = -0.4: {is_profitable(-0.4)}")

def future_value(principal, rate, years):
    return principal * (1+rate)**years
print("---")
print(f"Future value of initial investment 10_000, rate 0.03, years 3: {future_value(10_000, 0.03, 3):.2f}")
print(f"Future value of initial investment 1_000, rate 0.12, years 0.25: {future_value(1_000, 0.12, 0.25):.2f}")
print(f"Future value of initial investment 100_000, rate 0.04, years 10: {future_value(100_000, 0.04, 10):.2f}")
print("---")
"""
Task 2 — float('inf') sentinel pattern
  
  returns = [0.032, -0.015, 0.048, -0.072, 0.019, 0.055, -0.003, 0.041]

  Find:
  - best return and its index
  - worst return and its index

  Print:
  "Best return:  4.80% at index 2"
  "Worst return: -7.20% at index 3"
"""
print("")
print("Task 2 — float('inf') sentinel pattern")
print("")

returns = [0.032, -0.015, 0.048, -0.072, 0.019, 0.055, -0.003, 0.041]
best_return = float('-inf')
best_return_index = 0
worst_return = float('inf')
worst_return_index = 0
for r in range(len(returns)):
    if returns[r] > best_return:
     best_return = returns[r]
     best_return_index = r
    if returns[r] < worst_return:
        worst_return = returns[r]
        worst_return_index = r
print(f"Best return: {best_return:.2%}, its index: {best_return_index}")
print(f"Worst return: {worst_return:.2%}, its index: {worst_return_index}")


"""
Task 3 — Lambda
  
  Write lambdas for:
  pct_gain     → (current - previous) / previous
  is_winner    → True if return > 0
  round2       → rounds a number to 2 decimal places  (use round(x, 2))
  weight       → position_value / total
  
  Then:
  stocks = [("IGN1L", 0.041), ("SAB1L", -0.023), ("TEL1L", 0.067), ("OMXV", -0.011)]
  
  - Sort by return ascending
  - Sort by absolute return descending
  - Print ticker with best return using max()
  - Print ticker with worst return using min()
"""
print("")
print("Task 3 — Lambda")
print("")

pct_change = lambda current, previous: (current-previous)/previous
is_winner = lambda ret: ret > 0
round2 = lambda n: round(n,2)
weight = lambda position_value, total: position_value / total

stocks = [("IGN1L", 0.041), ("SAB1L", -0.023), ("TEL1L", 0.067), ("OMXV", -0.011)]
ascending = sorted(stocks, key=lambda p: p[1])
abs_return_descending = sorted(stocks, key=lambda p: abs(p[1]), reverse=True) #p[1] sort the list looking at the all numbers at index 1
# in each tuple+ additional argument: abs() - makes all numbers positive,
# overall telling the sorted(stocks, the argument= look up the 1st indexed values in each tuple making the firstly all positive, sort from higher to less.
#small fix: abs() does not make the output values positive. It only uses them for comparison. The original tuples with signs are returned.
best_ret = max(stocks, key=lambda s: s[1])
worst_ret = min(stocks, key=lambda s: s[1])
print(f"Ascended list of tuples: {ascending}")
print(f"Descended list of tuples ignoring the sign: {abs_return_descending}")
print(f"Best return: {best_ret[0]}")
print(f"Worst return: {worst_ret[0]}")
"""
Task 4 — Functions calling functions + list of dicts

  portfolio = [
      {"ticker": "IGN1L", "price": 15.80, "shares": 100},
      {"ticker": "SAB1L", "price": 29.40, "shares": 50},
      {"ticker": "TEL1L", "price": 9.75,  "shares": 200},
      {"ticker": "OMXV",  "price": 910.0, "shares": 10},
  ]

  Write:
  position_value(stock)     → price × shares for one stock dict
  total_value(portfolio)    → calls position_value() for each, returns sum
  weight(stock, portfolio)  → position_value(stock) / total_value(portfolio)
  largest(portfolio)        → max() with lambda, returns ticker of largest position
  smallest(portfolio)       → min() with lambda
  
  Print each ticker, value, weight.
  Print total value. 
  Print largest and smallest.
"""

print("")
print("Task 4 — Functions calling functions + list of dicts")
print("")

portfolio = [
      {"ticker": "IGN1L", "price": 15.80, "shares": 100},
      {"ticker": "SAB1L", "price": 29.40, "shares": 50},
      {"ticker": "TEL1L", "price": 9.75,  "shares": 200},
      {"ticker": "OMXV",  "price": 910.0, "shares": 10},
  ]

def position_value(stock): # the input stock means the indexed dict like:
    # portfolio[n] the function gets a dict then and calculates the position value accessing by dict syntax the values by its keys
    return stock["price"] * stock["shares"]

def total_value(portfolio):
    total_v = 0
    for stock in portfolio:#same logic, stock here is a whole dict from 0 index till the last one,
        # then position_value receives under "stock" - portfolio[0,1,2,3] and then doing its work returning the amount and it is just sums to a ttotal
        total_v += position_value(stock)
    return total_v

def weight(stock,portfolio):
    return position_value(stock)/ total_value(portfolio)

def largest(portfolio):
    return max(portfolio, key=lambda stock: position_value(stock))

def smallest(portfolio):
    return min(portfolio, key=lambda stock: position_value(stock))

for stock in portfolio:
    print(f"Ticker: {stock['ticker']}, Position value: {position_value(stock):,.2f}, Weight: {weight(stock,portfolio):.2%}")
print("")
print(f"Total value: ${total_value(portfolio):,.2f}")
print("")
print(f"Largest: {largest(portfolio)['ticker']}")
print(f"Smallest: {smallest(portfolio)['ticker']}")












