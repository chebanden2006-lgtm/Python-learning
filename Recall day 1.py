"""Task 1
Task 1 — Variables + types (20 min)
  ticker = "MSFT"
  price = 420.75
  volume = 18_500_000
  is_listed = True
  shares_held = None
  - Print each variable with type()
  - Check with isinstance(): is price a float? is volume an int? is ticker a float?
  - Print: "Current price: $420.75" and "Volume: 18,500,000"
"""
print("")
print("Task 1")
print("")
ticker = ("MSFT")
price = 420.75
volume = 18_500_000
is_listed = True
Shares_held = None

print(f"the type of variable ticker is {type(ticker)}")
print(f"the type of variable price is {type(price)}")
print(f"the type of variable volume is{type(volume)}")
print(f"the type of variable is_listed is {type(is_listed)}")
print(f"the type of variable Shares_held is {type(Shares_held)}")

print(isinstance(ticker, str))
print(isinstance(price, float))
print(isinstance(volume, int))
print(isinstance(is_listed, bool))
print(isinstance(Shares_held, type(None) ))

print(f"Current price: ${price:.2f}")
print(f"Volume: {volume:,}")


"""Task 2 
Task 2 — Arithmetic (30 min)
  entry_price = 400.0
  current_price = 420.75                                                                                                                                      
  shares = 50
  Calculate and print with labels, formatted to 2dp:
  - Daily P&L: (current_price - entry_price) * shares
  - Return %: (current_price - entry_price) / entry_price * 100
  - Position value: current_price * shares
"""
print("")
print("Task 2")
print("")
entry_price = 400.0
current_price = 420.75
shares = 50

print(f"Daily P&L: {((current_price - entry_price) * shares):.2f}")
print(f"Return %: {(current_price - entry_price) / entry_price * 100:.2f}")
print(f"position value: {(current_price * shares):.2f}")


"""
Task 3 — Compound interest (45 min)
  principal = 10_000
  annual_rate = 0.07
  years = 10
  No functions — just variables and math:
  - final_amount = principal * (1 + annual_rate) ** years
  - total_gain = final_amount - principal
  - gain_pct = total_gain / principal

  Print:
  Initial investment: €10,000.00
  Final amount:       €19,671.51
  Total gain:         €9,671.51
  Gain:               96.72%
"""
print("")
print("Task 3")
print("")
principal = 10_000
annual_rate = 0.07
years = 10

final_amount = principal * (1 + annual_rate) ** years
total_gain = final_amount - principal
gain_pct = total_gain / principal

print(f"initial investment: ${principal:,.2f}")
print(f"final amount: ${final_amount:,.2f}")
print(f"Total gain: ${total_gain:,.2f}")
print(f"Gain: {gain_pct:.2%}")



print("")
print("Task 4")
print("")
"""
Task 4 — f-string mastery (30 min)

  ret = 0.03271
  price = 18432.5
  ticker = "NVDA"
  Print these exact outputs:
  "NVDA daily return: 3.2710%"
  "NVDA price: $18,432.50"
  "Position value: €18,432.50"
  "Return rounded: 3.27%"
"""

Ret = 0.03271
Price = 18432.5
Ticker = "NVDA"

print(f"{Ticker} daily return: {Ret:.4%}")
print(f"{Ticker} price: ${Price:,.2f}")
print(f"Position value: ${Price:,.2f}")
print(f"Return rounded: {Ret:.2%}")


print("")
print("Task 5")
print("")
"""
 pe_ratio = 14.5
  dividend_yield = 3.2
  rsi = 28.0
  price = 152.5
  moving_avg_50 = 150.0
  Write conditions that evaluate to True or False:
  - Is P/E below 15 AND dividend above 3?
  - Is RSI below 30 (oversold)?
  - Is price above moving average?
  - Is it a "buy signal"? (price > MA50 AND RSI < 30)
"""
pe_ratio = 14.5
dividend_yield = 3.2
rsi = 28.0
price1 = 152.5
moving_avg_50 = 150.0

print(f"Is P/E below 15 AND dividend above 3?: {pe_ratio < 15 and dividend_yield > 3}")
print(f"Is RSI below 30 (oversold)?: {rsi<30}")
print(f"Is price above moving average?: {price1>moving_avg_50}")
print(f"Is it a buy signal?: {price1>moving_avg_50 and rsi<30}")