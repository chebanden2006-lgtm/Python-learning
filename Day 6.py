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
    for i, line in enumerate(f, start=1):
        print(f"{i}: {line.strip()}")

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
        line = line.strip()
        date,ticker,price = line.split(",")
        dates.append(date)
        prices.append(float(price))
returns = []
for i in range(1,len(prices)):
    ret = (prices[i]-prices[i-1])/prices[i-1]
    returns.append(ret)
dates.pop(0)
print("Returns:")

for date, r in zip(dates,returns):
    print(f"{date}: {r:+.2%}")

print("")
print("Task 3  Write the results to a file")
print("")
'''
1. Open returns.txt in write mode.
2. Write the header: === MSFT Daily Returns ===
3. Write each return, formatted to 4 decimal places (one per line, with its date).
4. Write the footer: Mean return: X.XXXX%
5. Open it again and read it back. Print it to confirm it looks correct.
'''

with open("returns.txt", "w") as f:
    f.write("=== MSFT Daily Returns ===\n")
    for date, r in zip(dates,returns):
        f.write(f"{date}: {r:+.4%}\n")
    f.write(f"Mean return: {sum(returns)/len(returns):+.4%}\n") # - Reading: the data comes from the file, so you loop over f. f isn't being created there; it already exists from with open(...) as f. The loop just uses it as the source.
#- Writing: the data comes from your lists, so you loop over the lists. f is the destination, used inside the loop with f.write().

with open("returns.txt", "r") as f:
    for line in f:
        print(line.strip())


print("")
print("Task 4  pathlib")
print("")

'''
from pathlib import Path
base = Path("/Users/denisceban/Python learning ")
1. Check whether prices.csv exists in base. Print "Found" or "Not found".
2. Read prices.csv through base / "prices.csv" and print its lines.
3. Create a folder called output inside base.
4. Write returns.txt into the output folder.
5. Count the .pdf files in base. Print: Found X PDF files
6. Extra: count them again including subfolders, and print both numbers.

️For step 1 to print "Found", the copy of prices.csv must be in Python learning  itself. Last time I checked, it was in Done homeworks/. Run the check first and see what it says.
'''


from pathlib import Path
base = Path("/Users/denisceban/Python learning")
prices_csv = base / "prices.csv"
if prices_csv.exists():
    print("Found")
else:
    print("Not found")

with open(base / "prices.csv", "r") as f:
    for line in f:
        print(line.strip())

print("")
output = base / "output"
output.mkdir(exist_ok=True)
with open(output / "returns.txt", "w") as f:
    for date, r in zip(dates,returns):
        f.write(f"{date}: {r:+.4%}\n")
print("")
pdf_files = list(base.glob("*.pdf"))
print(f"Found {len(pdf_files)} PDF files")
"""
another way through the loop
pdf_files = []
for file in base.glob("*.pdf"):
    pdf_files.append(file.name)
print(f"Found {len(pdf_files)} PDF files")
"""

pdfs = list(base.rglob("*.pdf"))
print(f"Found {len(pdfs)} PDF files including subfolders")




