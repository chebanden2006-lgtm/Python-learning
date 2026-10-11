"""
 One complete script that does all of this:

  1. Define a list of 5 tickers, prices, and shares (make them up)
  2. Using zip() + loop: compute value and weight for each stock
  3. Label each position: "Large" (weight > 30%), "Medium" (10–30%), "Small" (< 10%)
  4. Print a formatted portfolio table
  5. Using a list comprehension: extract only stocks with weight > 20%
  6. Define compound_interest(p, r, n) — apply it to each position at 7% for 5 years
  7. Print: "Total portfolio value: €XX,XXX.XX"

  Must run clean. Zero errors. Zero looking at earlier code.
"""
print("")
print("-----Formatted portfolio table------")

tickers = ["MSFT", "AAPL", "TSLA", "NVDA", "NSDQ"]
prices = [120, 190, 150, 130, 170]
shares = [15, 30, 10, 25, 35]

total_value = 0
for price,share in list(zip(prices,shares)):
    total_value += price * share

sizes = []
position_values = []
weights =[]
for ticker,price,share in list(zip(tickers,prices,shares)):
    position_value = price * share
    position_values.append(position_value)
    weight = position_value/total_value
    weights.append(weight)
    if weight > 0.3:
        sizes.append("Large")
        print(f"Ticker: {ticker}, position value: ${position_value:,.2f}, weight: {weight:.2%}, Large")
    elif 0.1 < weight < 0.3:
        sizes.append("Medium")
        print(f"Ticker: {ticker}, position value: ${position_value:,.2f}, weight: {weight:.2%}, Medium")
    elif weight < 0.1:
        sizes.append("Small")
        print(f"Ticker: {ticker}, position value: ${position_value:,.2f}, weight: {weight:.2%}, Small")
print("")
portfolio = list(zip(tickers,prices,shares,position_values,weights,sizes))
weight_above20 = ([weight for weight in portfolio if weight[4] > 0.2])
print("")
print("Positions with the weight above 20%:")
print([f"{item[0]}" for item in weight_above20])
print("")
def compound_interest(principal,rate,time):
    return principal * (1 + rate)**time

for t in range(len(portfolio)):
    print(f"Expected profit of compound growth of {portfolio[t][0]} at a rate of 7% for 5 years is ${compound_interest(portfolio[t][3], 0.07, 5):,.2f}")
print("")
print(f"Total portfolio value: ${total_value:,.2f}")

