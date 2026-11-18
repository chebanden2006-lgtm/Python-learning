print("")
print("Task 1: Basic try/except")
print("")

"""
def safe_divide(a, b):
    # try to return a / b
    # if b is zero: print "Error: division by zero" and return None

def safe_open(filepath):
    # try to open the file and return its contents
    # if the file is not found: print f"Error: {filepath} not found" and return None
Test each one with inputs that trigger the error and inputs that work.
"""
print("---1pt---")
def safe_divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print(f"Error: division by zero")
    return None
print((safe_divide(1,0)))
print((safe_divide(300,5)))
print("---2pt---")
def safe_open(filepath):
    try:
        with open(filepath, "r") as f:
            return [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error : {filepath} not found")
        return None

content = safe_open('/Users/denisceban/PyCharmMiscProject/report.txt')
for line in content:
    print(line)
content = safe_open('/Users/denisceban/PyCharmMiscProject/repor.txt')


print("")
print("Task 2: Safe Sharpe ratio")
print("")

"""
def sharpe(returns, rf=0.02, trading_days=252):
Annualised Sharpe = (mean daily return × 252 − rf) / (daily std × √252).

Handle with try/except:
- empty list → print "Error: no returns provided"
- zero std → print "Error: zero volatility"
- any other error → print the exception type and message

Return None for errors and the Sharpe value (float) for success.

Test with:
- a normal returns list → a number
- [] → the error message
- [0.01, 0.01, 0.01] → the zero-volatility message
"""
import math
def sharpe(returns, rf = 0.02, trading_days = 252):
    try:
        mean = sum(returns) / len(returns)
        variance = sum((r - mean) ** 2 for r in returns) / (len(returns) - 1)
        std = math.sqrt(variance)
        if std < 1e-10:
            raise ValueError("Error: zero volatility")
        return (mean * trading_days - rf) / (std * math.sqrt(trading_days))
    except ZeroDivisionError:
        print(f"Error: no returns provided")
        return None
    except ValueError as e:
        print(e)
        return None
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        return None
returns = [0.01, -0.005, 0.02, 0.003, -0.01, 0.015, 0.008]
returns2 = []
returns3 = [0.1, 0.1, 0.1]
print(f"{sharpe(returns)}")
print(f"{sharpe(returns2)}")
print(f"{sharpe(returns3)}")
"""
RAISE → EXCEPT: how Python reads it

1. My condition is checked inside try:
       if std == 0:
           raise ValueError("zero volatility")
   - For Python, std = 0 is fine (no error).
   - raise turns "fine for Python, bad for my rules" into a REAL error.

2. raise creates ONE error object:
       ValueError        → TYPE (existing Python template, I can't invent names)
       "zero volatility" → MESSAGE (my own text, packed inside the object)
   Each raise makes a new, separate copy. Other ValueErrors are not affected.

3. Python stops the try immediately:
   - lines BEFORE raise already ran
   - lines AFTER raise in try are skipped (never run)

4. Python checks the except blocks from TOP to BOTTOM:
       except ZeroDivisionError:   → type matches? no → skip
       except ValueError as e:     → type matches? yes → catch here
   - except compares ONLY the type (not my condition, not my message)
   - as e → puts my object into e (e lives only inside this block)
   - print(e) → shows my message
   - return None → what the function returns (not e)

5. If no except matches the type → nobody catches it → program crashes.

Parts and their roles:
   condition → decides WHETHER to raise (then forgotten)
   type      → the label that except matches
   message   → rides inside the object, e carries it

ValueError vs TypeError (quick test: would another value of the SAME type work?)
   ValueError → right kind, bad content (yes):  float("N/A"), price <= 0, std == 0
   TypeError  → wrong kind of thing (no):       "420" + 5, len(415.2), sharpe()

Rule: raise stops the try. Python catches the error in the first except block
whose TYPE matches, checking from top to bottom.
"""





print("")
print("Task 3: Input validation")
print("")

"""
def validate_trade(ticker, price, shares, direction):
Validate:
- ticker: a string, 1–5 uppercase letters
- price: must be > 0
- shares: must be a positive integer
- direction: must be "BUY" or "SELL"

If invalid: raise ValueError with a clear message.
If valid: print "Trade validated: BUY 10 MSFT @ $420.50" and return True.

Call it inside try/except to catch the ValueError. Test with 1 valid input and 4 different invalid inputs (one for each rule).
"""

def validate_trade(ticker, price, shares, direction):
        if not (ticker.isalpha() and ticker.isupper() and 1 <= len(ticker) <=5):
            raise ValueError(f"Error: wrong name of ticker {ticker}")
        elif not price > 0:
            raise ValueError(f"Error: Wrong price {price}")
        elif not (isinstance(shares, int) and shares > 0):
            raise ValueError(f"Error: shares are wrong {shares}")
        elif direction not in ("BUY", "SELL"):
            raise ValueError(f"Error: wrong direction {direction}")
        else:
            print(f"Trade validated: {direction} {shares} {ticker} @ ${price:.2f}")
        return True
tests = [
    ("MSFT", 120, 17, "BUY"),
    ("mSFT", 120, 17, "BUY"),
    ("MSFT", -120, 17, "BUY"),
    ("MSFT", 120, -17, "BUY"),
    ("MSFT", 120, 17, "UY")
]
for ticker, price, shares, direction in tests:
    try:
        validate_trade(ticker, price, shares, direction)
    except ValueError as e:
        print(e)


print("")
print("Task 4: Full file reader with error handling")
print("")

"""
def load_prices(filepath):
Handle:
- file not found → FileNotFoundError, with a message
- empty file → return [] plus a warning message
- a row with the wrong column count → skip it and print a warning
- a price that isn't a number → skip it and print a warning
- success → return a list of (date, float) tuples

Print a summary at the end:
Loaded 7 rows. Skipped 0 rows with errors.

Test with:
1. the valid prices.csv
2. a path that doesn't exist
3. a CSV with corrupted rows: make a copy called prices_bad.csv, then break one row (remove a column) and another (replace a price with text)
"""

def load_prices(filepath):
    try:
        loaded = 0
        skipped = 0
        content = []
        with open(filepath, "r") as f:
            next(f,None)
            for i,line in enumerate(f, start=2):
                parts = line.strip().split(",")
                if len(parts) != 3:  # ← parts, and 3 columns (date, ticker, close)
                    skipped +=1
                    print(f"Warning: row {i} has wrong number of columns: {line.strip()}")  # ← print, not raise
                    continue
                try:
                    price = float(parts[2])
                except ValueError:
                    print(f"Warning: row {i} price is not a number: {parts[2]}")
                    skipped += 1
                    continue
                content.append((parts[0], price))
                loaded += 1
        if len(content) == 0 and skipped == 0:
            print(f"Warning: file {filepath} is empty")
            return []
        print(f"Loaded {loaded} rows. Skipped {skipped} rows with errors.")
        return content
    except FileNotFoundError:
        print(f"Error: {filepath} not found")
        return None
print(load_prices("prices.csv"))
print(load_prices("no_such_file.csv"))
print(load_prices("prices_bad.csv"))

