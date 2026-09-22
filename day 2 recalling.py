"""
Write if / elif / else that
prints:
- "STRONG BUY"  → price > MA50 and rsi < 30
- "BUY"         → price > MA50 and rsi < 50
- "HOLD"        → price == MA50 or 30 <= rsi <= 70
- "SELL"        → rsi > 70
- "STRONG SELL" → price < MA50 and rsi > 70
Test
with 5 different combinations of values.Change the variables each time, run each time.
"""
print("")
print("Task 1 Trading signal")
print("")

current_price = 152.50
moving_avg_50 = 150.00
rsi = 28.0

if current_price > moving_avg_50 and rsi < 30:
    print("STRONG BUY")
elif current_price > moving_avg_50 and rsi < 50:
    print("BUY")
elif current_price == moving_avg_50 or 30 <= rsi <= 70:
    print("HOLD")
elif current_price < moving_avg_50 and rsi > 70:
    print("STRONG SELL")
elif rsi > 70:
    print("SELL")
else:
      print("NO SIGNAL")

"""
In order, print result after each step:
  1. Print first and last price
  2. Print prices from index 2 to index 5
  3. Append 110
  4. Insert 98 at position 0
  5. Remove item at index 3
  6. Print total count
  7. Print min and max without min() and max() — use a loop
  8. Reverse the list using slicing
"""
print("")
print("Task 2 List operations")
print("")

prices1 = [100, 102, 99, 105, 103, 108, 107]

print(f"First price: {prices1[0]}, Last price:{prices1[-1]}")
print(f"Prices from index 2 to index 5: {prices1[2:5]}")
prices1.append(110)
print(f"Added one value at the end: {prices1}")
prices1.insert(0,98)
print(f"Inserted one additional number 98 at the index 0: {prices1}")
prices1.pop(3)
print(f"Removed the value at index 3: {prices1}")
print(len(prices1))
lowest = prices1[0]
print(prices1)
for m in prices1:
    if m < lowest:
        lowest = m
print(f"min: {lowest}")

highest = prices1[0]
for p in prices1:
    if p > highest:
        highest = p
print(f"max: {highest}")

print(prices1[::-1])

"""
  Manually compute daily returns without a loop — one by one:
  ret_1 = (prices[1] - prices[0]) / prices[0]
  # do this for all pairs

  Store all in a list called returns.

  Then:
  - Count positive days and negative days
  - Find best day and worst day — index and value
  - Print formatted summary
"""
print("")
print("Task 3 Returns from prices ")
print("")

prices2= [100, 102, 99, 105, 103, 108, 107, 110]

ret_1 = (prices2[1] - prices2[0]) / prices2[0]
ret_2 = (prices2[2] - prices2[1]) / prices2[1]
ret_3 = (prices2[3] - prices2[2]) / prices2[2]
ret_4 = (prices2[4] - prices2[3]) / prices2[3]
ret_5 = (prices2[5] - prices2[4]) / prices2[4]
ret_6 = (prices2[6] - prices2[5]) / prices2[5]
ret_7 = (prices2[7] - prices2[6]) / prices2[6]

returns = [ret_1, ret_2, ret_3, ret_4, ret_5, ret_6, ret_7]

positive = 0
negative = 0
for i in range(len(returns)):
    if returns[i] > 0:
        positive = positive  + 1
    elif returns[i] < 0:
        negative = negative + 1


best_day_index = 0
best_day_value = returns[0]
for p in range(len(returns)):
    if best_day_value < returns[p]:
        best_day_value = returns[p]
        best_day_index = p

worst_day_index = 0
worst_day_value = returns[0]
for k in range(len(returns)):
    if worst_day_value > returns[k]:
        worst_day_value = returns[k]
        worst_day_index = k


print("---Summary---")
print(f"Total days: {len(returns)}")
print(f"Positive returns amount is: {positive}")
print(f"Negative returns amount is: {negative}")
print(f"Best day index and value: ({best_day_index} ,{best_day_value:.2%})")
print(f"Worst day index and value: ({worst_day_index} ,{worst_day_value:.2%})")













