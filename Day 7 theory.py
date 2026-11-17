for text in ["415.20", "N/A"]:
    print("Checking:", text)
    try:
        price = float(text) #if try true we skip except
    except ValueError:
        print("  Bad price") # we skip it if the try worked, if no, and there is an ValueError it will run the line below and then prints only finally:
    else:
        print("  OK:", price) #runs only if try is True(for python the code goes next and just skips the except
    finally:
        print("  Row done") # runs every round as the line ends

rows = [
    "2026-01-02,MSFT,415.20",
    "2026-01-03,MSFT",           # missing a column
    "2026-01-06,MSFT,N/A",       # price not a number
    "2026-01-07,MSFT,420.10",
]
skipped = 0
checked = 0
clear_rows = []
for row in rows:
    parts = row.split(",")

    if len(parts) != 3:
        print(f"Warning, the row has different length: ", parts)
        skipped += 1
        continue
    try:
        price = float(parts[2])
    except ValueError:
        print(f"The price is not a number in row: ", parts)
        skipped += 1
    else:
        clear_rows.append((parts[0], price))
        checked += 1

print(f"Clear rows: ")
print(clear_rows)
print(f"The number of skipped rows: ", skipped)
print(f"The number of rows that are accepted: ", checked)

'''
else vs finally in your code

- else runs only for rows where float() worked: the 2 good rows. That's why your append is correctly there.
- finally would run for every row that reached try, good or bad. If you added
finally:
    print("Row checked:", parts[0])
  it would print 3 times: both good rows and the N/A row.

It would not print for the 2-column row. That row hit continue at line 27 and never reached try, so its finally doesn't exist for that round. finally only guarantees "always" for code that entered the try.
'''

"""
raise: create an error yourself

Use it when a value is valid for Python but wrong for your rules. The function stops immediately.
"""
prices = [12,24,35]
for p in prices:
    if p <=0:
        raise ValueError("Price must be > 0")
#continue: skip to the next round of a loop
#The rest of the current round is skipped. Only used inside loops.
for p in prices:
    if p <= 0:
        continue        # bad price → go to the next one
    print(p)

    """
    None: Python's value for "nothing / no result"
    
    Typically returned when a function fails.
    """
def safe_price(text):
    try:
        return float(text)
    except ValueError:
        return None
if safe_price("N/A") is None:
    print("No price")

#as e:
def position_weight(value, total):
    try:
        return value / total
    except ZeroDivisionError as e:          # only division by 0
        print("ZeroDivisionError:", e)
    except (ValueError, TypeError) as e:    # either of these two
        print(f"{type(e).__name__}:", e)
    except Exception as e:                  # anything else (always last)
        print("Unexpected", type(e).__name__, ":", e)
    return None
"""
Common error types:
- ValueError: the right type but a bad value, e.g. float("N/A"), or unpacking the wrong number of columns
- TypeError: the wrong type for the operation, e.g. "5000" / 20000, f.write(3.5)
- ZeroDivisionError: dividing by 0
- FileNotFoundError: opening a file that doesn't exist
- IndexError: a list index that doesn't exist, e.g. prices[7] with 7 items
- KeyError: a dict key that doesn't exist, e.g. portfolio["TSLA"]
- NameError: using a variable that was never defined (usually a typo)
- Exception: the parent of almost all of the above, so it catches any of them


"""