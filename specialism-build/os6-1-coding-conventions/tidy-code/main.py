# This code works, but nobody can read it. Tidy it.
# Make four small functions with good names and a docstring in each. The last one uses another:
#   total_price(prices, voucher)  the sum of prices, minus the voucher, never below 0
#   is_adult(age)                 True if age is 18 or more
#   average_mark(marks)           the sum of marks divided by how many, or 0 for an empty list
#   format_report(name, marks)    text like: Aisha: average 70   (round the average to a whole number)
# A docstring is a text in triple quotes on the first line inside the function.

def f(a,b):
  x=0
  for i in a:
    x=x+i
  if x-b<0:return 0
  return x-b
def g(a):
  return a>=18
def h(l):
  if len(l)==0:return 0
  return sum(l)/len(l)
