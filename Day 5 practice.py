"""
Task 1 — List comprehensions (45 min)

  prices = [100, 102, 99, 105, 103, 108, 107, 110, 108, 112]

  Write as one-line comprehensions — no for loops:

  1. All prices above 105
  2. Every price multiplied by 1.1
  3. Daily returns: (prices[i] - prices[i-1]) / prices[i-1] for all pairs
  4. String labels: ["Price: $100.00", "Price: $102.00", ...]
  5. Boolean list: is each return positive?
  6. Only the positive returns (filter with condition inside comprehension)
"""
import math
print("")
print("Task 1 — List comprehensions")
print("")

prices = [100, 102, 99, 105, 103, 108, 107, 110, 108, 112]
prices_above_105 = [p for p in prices if p > 105]
print(f"Prices above 105:")
print([f"${x:.2f}" for x in prices_above_105])
prices_multiplied = [p * 1.1 for p in prices]
print(f"Prices multiplied by 1.1:")
print([f"${p:,.2f}" for p in prices_multiplied])
daily_returns = [((prices[i] - prices[i-1])/(prices[i-1])) for i in range(1, len(prices))]
print(f"Daily returns:")
print([f"{r:.2%}" for r in daily_returns])
print("")
print([f"Price: ${p:,.2f}" for p in prices])
print("")
is_positive = [r > 0 for r in daily_returns]
print(f"Is each return positive: {is_positive}")
print("")
print("Positive daily returns: ")
print([f"{r:,.2%}" for r in daily_returns if r > 0])

"""
Task 2 — Tuples + sets (30 min)
  
  trade = ("MSFT", "BUY", 420.5, 10, "2026-10-07")

  1. Unpack all 5 fields into named variables
  2. Print each with a label

  all_trades = ["MSFT", "AAPL", "MSFT", "NVDA", "AAPL", "MSFT", "TSLA", "AAPL"]

  3. Build a set of unique tickers
  4. Print how many unique tickers
  5. Print them sorted alphabetically
  6. Build a second set: traded_today = {"AAPL", "NVDA", "GOOG"}
  7. Print: tickers in both sets, tickers only in all_trades set
"""

print("")
print("Task 2 — Tuples + sets")
print("")

trade = ("MSFT", "BUY", 420.5, 10, "2026-10-07")
ticker, signal, price, shares, date = trade
print(f"Ticker: {ticker}")
print(f"Signal: {signal}")
print(f"Price: ${price:,.2f}")
print(f"Shares: {shares}")
print(f"Date: {date}")
print("")


all_trades = ["MSFT", "AAPL", "MSFT", "NVDA", "AAPL", "MSFT", "TSLA", "AAPL"]

unique_t = set(all_trades)
print(f"Amount of all unique tickers: {len(unique_t)}")

sorted_t = sorted(unique_t)
print(f"Unique trades sorted alphabetically: {sorted_t}")
traded_today = {"AAPL", "NVDA", "GOOG"}
print(f"Traded today: {traded_today}")
print(f"All tickers in both sets: {unique_t & traded_today}")
print(f"Set of tickers only in all trades: {unique_t - traded_today}")


"""
Task 3 — map + filter + enumerate (45 min)

  prices = [100, 102, 99, 105, 103]
  days   = ["Mon", "Tue", "Wed", "Thu", "Fri"]

  1. Use map() to compute log of each price (import math)
  2. Use map() to convert each price to a formatted string: "$100.00"
  3. Use filter() to keep only prices above the mean
  4. Use zip() to pair prices with days, print: "Mon: $100.00"
  5. Use enumerate() on these, print numbered:
  tickers = ["MSFT", "AAPL", "NVDA", "AMZN"]
  prices2 = [420.5, 189.3, 875.0, 192.4]
  1. MSFT: $420.50
  2. AAPL: $189.30
  3. NVDA: $875.00
  4. AMZN: $192.40
"""

print("")
print("Task 3 — map + filter + enumerate")
print("")

prices1 = [100, 102, 99, 105, 103]
days   = ["Mon", "Tue", "Wed", "Thu", "Fri"]
log_prices = list(map(math.log, prices1))
print(f"Log prices:")
print([f"{p:,.2f}" for p in log_prices])
converted_prices = list(map(lambda p: f"${p:,.2f}", prices1))
print(f"Prices converted to the strings: {converted_prices}")
mean = sum(prices1)/len(prices1)
prices_above_mean = list(filter(lambda p: p > mean, prices1))
print(f"Prices above mean: ")
print([f"${p:,.2f}" for p in prices_above_mean])
prices1_days = list(zip(days,prices1))
print([f"{d}: ${p:,.2f}" for d,p in prices1_days])
tickers = ["MSFT", "AAPL", "NVDA", "AMZN"]
prices2 = [420.5, 189.3, 875.0, 192.4]
tickers_prices2 = list(zip(tickers,prices2))
for i, value in enumerate(tickers_prices2, start=1):
    print(f"{i}. {value[0]}: ${value[1]:,.2f}")
