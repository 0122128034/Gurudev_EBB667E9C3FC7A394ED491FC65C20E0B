def factorial(n):
  if n == 1:
    return n
  else:
    return n * factorial(n - 1)
num = int(input("Enter any number: "))
res=factorial(num)
print(res)
