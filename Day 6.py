print("")
print("Task 1: Read a file")
print("")
"""
Open prices.csv, read every line, and print each row with its line number:
1: date,ticker,close
2: 2026-01-02,MSFT,415.20
...
8: 2026-01-10,MSFT,425.00
Always with open(). Clean every line.

"""
with open("prices.csv", "r") as f:
    for line in f:
         line.strip()
with open("prices.csv", "r") as f:
    for i, line in enumerate(f, start=1):
        print(i, line.strip())

print("")
print("Task 2: Parse the CSV and compute returns")
print("")
"""
5. Print each one:
2026-01-03: +0.79%
2026-01-06: -1.36%
...
Think about which date belongs to each return. The first day has no return.
"""
dates = []
prices = []
with open("prices.csv", "r") as f:
    next(f)
    for line in f:
        line.strip()
        date,ticker,price = line.split(",")
        dates.append(date)
        prices.append(float(price))
returns = []
for i in range(1,len(prices)):
    ret = (prices[i]-prices[i-1])/prices[i-1]
    returns.append(ret)
dates.pop(0)
print("Returns:")
with open("report.csv", "w") as f:
    for date, r in zip(dates,returns):
        f.write(f"{date}: {r:.2f}%\n")
with open("report.csv", "r") as f:
    for line in f:
        print(line.strip())




