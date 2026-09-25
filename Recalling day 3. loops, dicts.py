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


