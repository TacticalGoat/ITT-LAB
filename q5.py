#! C:/Python27/pyhton.exe
def sumton(n):
	if n == 0:
		return 0
	else:
		return n+sumton(n-1)


n = int(raw_input())
print sumton(n)