print "Enter Input:"

x = str(raw_input())
x = x.lower()

x_rev = reversed(x)

if list(x) == list(x_rev):
	print "PALINDROME!"
else:
	print "NOPE!"