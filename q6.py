def fib(n):
   if n <= 2:
      return 1
   else:
      return fib(n-1) + fib(n-2)

x = int(raw_input())
for i in range(1,x):
	print fib(i)