print("")
print("Task 1: Read")
print("")
"""
Print every line of tel1l.csv in this format:
Line 1 -> date,ticker,close,volume
Line 2 -> 2026-02-02,TEL1L,2.150,12500
...
Then print the total number of lines in the file:
Total lines: X
"""

with open("tel1l.csv", "r") as f:
    for i,line in enumerate(f,start=1):
        print(f"Line {i} -> {line.strip()}")
    print(f"Total lines: {i}")



print("")
print("Task 2: Parse and compute")
print("")

"""
1. Store the dates, closes and volumes in three lists.
2. Compute the daily returns.
3. Print each day in this format:
2026-02-03 | return: +X.XX% | volume: X
4. Print:
Total volume: X
Best day: YYYY-MM-DD (+X.XX%)
Worst day: YYYY-MM-DD (-X.XX%)
"""

dates = []
closes = []
volumes = []

with open("tel1l.csv", "r") as f:
    next(f)
    for line in f:
        line = line.strip()
        date, ticker, close, volume = line.split(",")
        dates.append(date)
        closes.append(float(close))
        volumes.append(int(volume))
print(dates)
print(closes)
print(volumes)
returns = []
for i in range(1, len(closes)):
    returns.append((closes[i]-closes[i-1])/closes[i-1])

for date, ret, volume in zip(dates[1:], returns, volumes[1:]):
    print(f"{date} | return: {ret:+.2%} | volume: {volume}")
print(f"Total volume: {sum(volumes)}")

best_ret = float('-inf')
best_date = ""
worst_ret = float('inf')
worst_date = ""

for date,ret in zip(dates[1:],returns):
    if ret > best_ret:
        best_ret = ret
        best_date = date
    if ret < worst_ret:
        worst_ret = ret
        worst_date = date
print(f"Best day: {best_date} ({best_ret:+.2%})")
print(f"Worst day: {worst_date} ({worst_ret:+.2%})")



print("")
print("Task 3: Write")
print("")

"""
Write tel1l_report.txt with:
=== TEL1L Daily Report ===
2026-02-03: +X.XXXX%
...
Mean return: +X.XXXX%
Best day: YYYY-MM-DD
Worst day: YYYY-MM-DD
Read the file back and print it.

Then, in a separate step, add one more line to the end of the same file without deleting its content:
Report checked
Read it back again and print it.
"""

with open("tel1l_report.txt", "w") as f:
    f.write("=== TEL1L Daily Report ===\n")
    for date,r in zip(dates[1:],returns):
       f.write(f"{date}: {r:+.4%}\n")
    mean_return = sum(returns)/len(returns)
    f.write(f"Mean return: {mean_return:+.4%}\n")
    f.write(f"Best day: {best_date}\n")
    f.write(f"Worst day: {worst_date}\n")

with open("tel1l_report.txt", "r") as f:
    header = f.readline().strip()
    print(header)
    for line in f:
        print(line.strip())
print("")
with open("tel1l_report.txt", "a") as f:
    f.write("Report checked\n")
with open("tel1l_report.txt", "r") as f:
    header = f.readline().strip()
    print(header)
    for line in f:
        print(line.strip())

print("")
print("Task 4: pathlib")
print("")

"""
base = your Python learning folder.

1. Create a folder data inside base, and put a copy of tel1l.csv there (manually, in Finder or PyCharm).
2. Check whether tel1l.csv exists in data. Print "Found" or "Not found".
3. Read tel1l.csv from data and print only the closes as a list.
4. Create a folder reports inside base, and write tel1l_report.txt (the same content as Task 3, without the "Report checked" line) into it.
5. Print the names of all .txt files in base, one per line, then: Found X TXT files.
6. Count the .py files in base, then in base including subfolders. Print both numbers, labelled.
"""

from pathlib import Path
base = Path("/Users/denisceban/Python learning/")
data = base / "data"
data.mkdir(exist_ok=True)
tel1l_csv = data / "tel1l.csv"
if tel1l_csv.exists():
    print("Found")
else:
    print("Not found")
closes1 = []
with open( data / "tel1l.csv", "r") as f:
    next(f)
    for line in f:
        line = line.strip()
        date1, ticker1, close1, volume1 = line.split(",")
        closes1.append(float(close1))
print(closes1)

reports = base / "reports"
reports.mkdir(exist_ok=True)
with open(reports / "tel1l_report.txt", "w") as f:
    f.write("=== TEL1L Daily Report ===\n")
    for date, r in zip(dates[1:], returns):
        f.write(f"{date}: {r:+.4%}\n")
    mean_return = sum(returns) / len(returns)
    f.write(f"Mean return: {mean_return:+.4%}\n")
    f.write(f"Best day: {best_date}\n")
    f.write(f"Worst day: {worst_date}\n")
txt_amount = 0
for file in base.glob("*.txt"):
    txt_amount += 1
    print(file.name)
print(f"Found {txt_amount} TXT files")

py_in_base = len(list(base.glob("*.py")))
py_in_base_sub = len(list(base.rglob("*.py")))
print(f"Found {py_in_base} .py files in base")
print(f"Found {py_in_base_sub} .py files in base including subfolders")






