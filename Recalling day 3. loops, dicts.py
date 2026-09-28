"""
Task 1 — for + range (30 min)
  Print first 10 years of compound growth:
  principal = 10_000
  rate = 0.07
 Use for loop with range(1, 11).
  Expected output:
  Year  1: $10,700.00
  Year  2: $11,449.00
  ...
  Year 10: $19,671.51
"""
print("")
print("Task 1 for + range")
print("")
principal = 10_000
for i in range(1,11):
    compound_balance = principal + principal * 0.07
    principal = compound_balance
    print(f"Year {i:2d}: ${compound_balance:,.2f}")

"""
Task 2 — while loop (30 min)
  
  You invest €1,000 at 8% annual return. Use a while loop to find how many years until you have €3,000. Print:
  It takes X years to triple your investment.
  Then repeat for 5% and 12% — print all three results.
"""
print("")
print("Task 2 while loop")
print("")
investment = 1_000
limit = 3_000
years = 0
while investment < limit:
    amount =investment + investment * 0.08
    investment = amount
    years +=1
print(f"It takes {years} years to triple your investment with annual rate of 8%")

investment2 = 1_000
years2 = 0
while investment2 <  limit:
    amount2 = investment2 + investment2 * 0.05
    investment2 = amount2
    years2 +=1
print(f"It takes {years2} years to triple your investment with annual rate of 5%")

investment3 = 1_000
years3 = 0
while investment3 < limit:
    amount3 = investment3 + investment3 * 0.12
    investment3 = amount3
    years3 +=1
print(f"It takes {years3} years to triple your investment with annual rate of 12%")

"""
Task 3 — FizzBuzz Finance (30 min)
  
  Loop 1 to 100 using range() and a for loop:
  - Divisible by 3 → print "Bull"
  - Divisible by 5 → print "Bear"
  - Divisible by both → print "Crash"
  - Otherwise → print the number
  
  No while. Use range().
"""
print("")
print("Task 3 FizzBuzz Finance")
print("")
for n in range(1,101):
    if n % 3 == 0 and n % 5 ==0:
        print("Crash")
    elif n % 3 == 0:
        print("Bull")
    elif n % 5 == 0:
        print("Bear")
    else:
        print(n)

"""
Task 4 — Dict operations (1 hr)

  Build this dict from scratch by adding stocks one by one — do not write it all at once:
  MSFT: 4200, AAPL: 3780, NVDA: 4375, TSLA: 1850, AMZN: 3600

  Then:
  1. Print all tickers + values using .items() — format: "MSFT: $4,200.00"
  2. Calculate total portfolio value
  3. Calculate each stock's weight — format: "MSFT weight: 23.45%"
  4. Find largest and smallest position
  5. Remove TSLA
  6. Add "GOOG": 2900
  7. Check if "AAPL" is in the portfolio using in
  """

print("")
print("Task 4 Dict operation")
print("")

portfolio = {}
portfolio["MSFT"] = 4200
portfolio["AAPL"] = 3780
portfolio["NVDA"] = 4375
portfolio["TSLA"] = 1850
portfolio["AMZN"] = 3600

for ticker,value in portfolio.items():
    print(f"{ticker}: ${value:,.2f}")

total = 0
for value in portfolio.values():
    total += value
print(f"Total portfolio value: ${total:,.2f}")

for ticker,value in portfolio.items():
    weight = value / total
    print(f"{ticker} weight: {weight:.2%}")

ticker2 = ""
largest = 0
for ticker1,value1 in portfolio.items():
    if value1 > largest:
        largest = value1
        ticker2 = ticker1
print(f"Largest value of the portfolio: {ticker2}: ${largest:,.2f}")


ticker4 = ""
smallest = float('inf')
for ticker3,value2 in portfolio.items():
    if value2 < smallest:
        smallest = value2
        ticker4 = ticker3
print(f"Smallest value of the portfolio: {ticker4}: ${smallest:,.2f}")


del portfolio["TSLA"]

portfolio["GOOG"] = 2900

check = "AAPL" in portfolio
print(f"AAPL in portfolio?: {check}")



"""
 Task 5 — Loop + list + zip (45 min)
  
  tickers = ["MSFT", "AAPL", "NVDA", "AMZN"]
  prices  = [420.5,  189.3,  875.0,  192.4]
  shares  = [10,     20,     5,      15   ]

  Using zip() and a for loop:
  - Compute value for each position (price * shares)
  - Sum total portfolio value
  - Print which stock has the highest value
"""

print("")
print("Task 5 Loop + list + zip")
print("")

p_tickers = ["MSFT", "AAPL", "NVDA", "AMZN"]
p_prices  = [420.5,  189.3,  875.0,  192.4]
p_shares  = [10,     20,     5,      15   ]
p_total = 0
print(f"Values for each position:")
for p_ticker, p_price, p_shares_held in zip(p_tickers,p_prices,p_shares):
    p_value = p_price * p_shares_held
    p_total += p_value
    print(f"{p_ticker}: {p_shares_held} shares @ ${p_price:,.2f} = ${p_value:,.2f}")
print("")
print(f"Sum total portfolio value: ${p_total:,.2f}")

p_highest = 0
p_highest_ticker = ""
p_lowest = float('inf')
p_lowest_ticker = ""
for p_ticker, p_price, p_shares_held in zip(p_tickers,p_prices,p_shares):
    p_value = p_price * p_shares_held
    if p_value > p_highest:
        p_highest = p_value
        p_highest_ticker = p_ticker
    if p_value < p_lowest:
        p_lowest = p_value
        p_lowest_ticker = p_ticker
print(f"Highest value of the portfolio:")
print(f"{p_highest_ticker}: ${p_highest:,.2f}")
print(f"Lowest value of the portfolio:")
print(f"{p_lowest_ticker}: ${p_lowest:,.2f}")

