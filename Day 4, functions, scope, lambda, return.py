
"""
def daily_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        r = (prices[i] - prices[i - 1]) / prices[i - 1]
        returns.append(r)
    return returns

def mean_return(prices):
    returns = daily_returns(prices)  # calls daily_returns
    return sum(returns) / len(returns)

def volatility(prices):
    returns = daily_returns(prices)  # calls daily_returns again
    mean = sum(returns) / len(returns)
    variance = sum((r - mean) ** 2 for r in returns) / len(returns)
    return variance ** 0.5
"""
"""
daily_returns is written once. Both mean_return and volatility reuse it.
If the return calculation ever needs to change, you fix it in one place.
"""

"""
Task 1 — Basic functions (45 min)
  
  Write these 4 functions. Test each with 3 different inputs. Print results formatted to 2dp.

  def simple_return(current, previous):
      # returns (current - previous) / previous

  def compound_interest(principal, rate, years):
      # returns final amount after compound growth

  def annualise(daily_return, trading_days=252):
      # returns annualised return from daily return

  def position_value(price, shares):
      # returns total position value
"""

print("")
print("Task 1 — Basic functions")
print("")

def simple_return(current, previous):
    return (current - previous)/previous
print("Simple returns calculated using this short list of prices: [188,190,193,185] - all calculated using function and the parameters are entered manually:")
print(f"{simple_return(190,188):.2%}")
print(f"{simple_return(193,190):.2%}")
print(f"{simple_return(185,193):.2%}")

def compound_interest(principal, rate, years):
    return principal * (1+rate)**years

print(f"Tests of the compounding growth formula creation using a def:")
print(f"${compound_interest(100,0.07, 5):.2f}")
print(f"${compound_interest(350, 0.04, 10):.2f}")
print(f"${compound_interest(10_000, 0.08, 0.6):.2f}")

def annualise(daily_return, trading_days=252):
    return daily_return * trading_days

print(f"Annualised returns from daily return:")
print(f"{annualise(0.00012, 365):.2%}")
print(f"{annualise(0.0015):.2%}")
print(f"{annualise(0.0017, 252):.2%}")


def position_value(price, shares):
    return price * shares

print(f"Totals position values for selected manually stocks:")
print(f"'MSFT': ${position_value(67, 50):,.2f}")
print(f"'AAPL': ${position_value(150, 23):,.2f}")
print(f"'TSLA': ${position_value(78, 13):,.2f}")




"""
 Task 2 — Default parameters + math (30 min)
  
  import math

  def sharpe_ratio(returns_list, risk_free=0.02, trading_days=252):
      # mean
      # variance
      # std = math.sqrt(variance)
      # ann_return = mean * trading_days
      # ann_vol = std * math.sqrt(trading_days)
      # sharpe = (ann_return - risk_free) / ann_vol
      # return sharpe

  test with: [0.01, -0.005, 0.02, 0.003, -0.01, 0.015, 0.008]
  print: "Sharpe Ratio: X.XX"
"""
print("")
print("Task 2 — Default parameters + math")
print("")

import math

def sharpe_ratio(returns_list, risk_free=0.02, trading_days=252):
    mean = sum(returns_list)/len(returns_list)
    variance = (sum((r-mean)**2 for r in returns_list)) / (len(returns_list))
    std = math.sqrt(variance)
    ann_return = mean * trading_days
    ann_vol = std * math.sqrt(trading_days)
    sharpe = (ann_return - risk_free) / ann_vol
    return sharpe

returns = [0.01, -0.005, 0.02, 0.003, -0.01, 0.015, 0.008]
sharpe = sharpe_ratio(returns)
print(f"Sharpe ratio of returns: {sharpe:.2f}")

"""
 Task 3 — Functions calling functions (45 min)

  def daily_returns(prices):
      # takes list of prices, returns list of daily returns

  def mean_return(prices):
      # calls daily_returns() inside

  def volatility(prices):
      # calls daily_returns() inside

  prices = [100, 102, 99, 105, 103, 108, 107, 110, 108, 112]
  
  print mean return, daily vol, annualised vol (* math.sqrt(252))
"""

print("")
print("Task 3 — Functions calling functions")
print("")
def daily_returns(prices_list):
    d_returns = []
    for p in range (1,len(prices_list)):
        returns = (prices_list[p]-prices_list[p-1])/(prices_list[p-1])
        d_returns.append(returns)
    return d_returns
def mean_return(price_list):
    returns = daily_returns(price_list)
    return sum(returns)/len(returns)

def volatility(prices_list):
      returns = daily_returns(prices_list)
      mean = mean_return(prices_list)
      total = 0
      for p in returns:
          f = (p - mean)**2
          total += f
      var = total / len(returns)
      std = math.sqrt(var)
      return std
prices = [100, 102, 99, 105, 103, 108, 107, 110, 108, 112]
"""
print mean return, daily vol, annualised vol (* math.sqrt(252))
"""
print(f"Mean return: {mean_return(prices):.2%}")
print(f"Daily vol: {volatility(prices):.2f}")
print(f"Annual volatility: {(volatility(prices) * math.sqrt(252)):.2f}")



"""
Task 4 — lambda (30 min)
  
  Write these as lambdas, then call each:

  square      →  square(5)            = 25
  pct_change  →  pct_change(110, 100) = 0.10
  annualise_v →  annualise_v(0.01)    = ~0.1587  (multiply by sqrt(252))
  is_positive →  is_positive(-0.02)   = False

  Then use lambda with sorted():
  stocks = [("MSFT", 420), ("AAPL", 189), ("NVDA", 875)]
  sort by price ascending, then descending
  print both sorted lists

"""
print("")
print("Task 4 — lambda")
print("")

square = lambda x: x**2
print(square(5))
pct_change = lambda new, old: (new-old)/old
print(f"{pct_change(110,100):.2%}")
annualise_v = lambda daily_return: daily_return * math.sqrt(252)
print(f"{annualise_v(0.01):.2f}")
is_positive = lambda value: value > 0
print(is_positive(-0.02))

stocks = [("MSFT", 420), ("AAPL", 189), ("NVDA", 875)]
ascending_sorted = sorted(stocks, key= lambda p: p[1])
print(ascending_sorted)
descending_sorted = sorted(stocks, key= lambda p: p[1], reverse=True)
print(descending_sorted)


"""
Task 5 — Full portfolio function (45 min)
                                                                                                                               
  def portfolio_stats(tickers, prices, shares, risk_free=0.02):
      # for each stock compute position value and weight
      # print formatted table:

      === PORTFOLIO SUMMARY ===
      MSFT  | Shares: 10 | Price: $420.50 | Value: $4,205.00 | Weight: 23.4%
      AAPL  | Shares: 20 | Price: $189.30 | Value: $3,786.00 | Weight: 21.1%
      ...
      TOTAL VALUE: $17,966.00

  Call it with your own 4 tickers, prices, shares.
  
  Formulas you need:
  position_value = price × shares
  weight         = position_value / total_portfolio_value
  total          = sum of all position values
"""
print("")
print("Task 5 — Full portfolio function")
print("")

portfolio = [
    {"ticker": "MSFT", "price": 420, "shares": 10},
    {"ticker": "AMZN", "price": 370, "shares": 17},
    {"ticker": "AAPL", "price": 250, "shares": 13},
    {"ticker": "TSLA", "price": 335, "shares": 7}
]

def portfolio_stats(portfolio, risk_free = 0.02):
    total = 0
    for stock in portfolio:
        total += stock["price"] * stock["shares"]
    print("===Portfolio Summary===")
    for stock in portfolio:
        position_value = stock["price"] * stock["shares"]
        weight = position_value/total
        print(f"{stock['ticker']} | Shares: {stock['shares']} | Price: ${stock['price']} | Value: ${position_value:,.2f} | Weight: {weight:.2%}")
    print(f"TOTAL VALUE: ${total:,.2f}")
portfolio_stats(portfolio)







