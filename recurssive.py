# day 30
# recursions in python is the process of calling a function inside the same function
# example
# factorial of 6 =6x5x4x3x2x1 or we can say that 6xfactorial of 5


def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)


n = int(input("enter the number for finding factorial: "))
print(factorial(n))


def sequenceSeries(m):
  if m == 0 or m == 1:
    return 1
  else:
    return m + sequenceSeries(m - 1)


m = int(input("enter the number for sum of arithmetic sequence: "))
print(sequenceSeries(m))


def fibonacci_seq(k):
  if k <= 1:
    return k
  else:
    return fibonacci_seq(k - 1) + fibonacci_seq(k - 2)


k = int(
  input("enter the number of element from the sequence you want to know: "))
print(fibonacci_seq(k))


def sum_list(lst):
  if len(lst) == 0:
    return 0
  else:
    return lst[0] + sum_list(lst[1:])


lst = []
n = int(input("enter the number of elements in the list: "))
for i in range(n):
  ele = int(input(f"enter the  {i+1}  element: "))
  lst.append(ele)
print(lst)
print(sum_list(lst))
# Key Points to Remember
# Base Case: Every recursive function must have a base case that stops the recursion to prevent infinite loops.
# Recursive Case: The function calls itself with a simpler or smaller input.
# Stack Overflow: Excessive recursion can lead to a stack overflow error due to too many nested function calls. This can be mitigated by using iterative approaches or tail recursion optimization (where supported).
# By using recursion appropriately, you can solve complex problems in a more intuitive and concise manner.
